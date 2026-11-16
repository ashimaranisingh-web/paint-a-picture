import numpy as np, sys, os
from PIL import Image
from scipy import ndimage as nd
SP=os.path.dirname(os.path.abspath(__file__))+'/'
OUT=sys.argv[1] if len(sys.argv)>1 else SP+'out/'
os.makedirs(OUT,exist_ok=True)
a=np.asarray(Image.open(SP+'sheet.webp').convert('RGBA')).astype(np.float32)
# sheet boxes; the sheet's "Left" faces right, so it is the app's walking-right picture
boxes={'male-front':(177,8,359,485),'male-back':(462,8,630,485),'male-side-right':(746,9,857,486),'male-side-left':(980,9,1089,486),
       'front':(190,533,368,977),'back':(468,534,626,978),'side-right':(752,536,850,979),'side-left':(993,536,1087,979)}
cuts={}
for k,(x0,y0,x1,y1) in boxes.items():
    c=a[max(0,y0-8):y1+10, max(0,x0-22):x1+22].copy()
    al=c[:,:,3]
    solid=al>140
    lab,n=nd.label(solid); sizes=nd.sum(solid,lab,range(1,n+1)); keep=lab==(1+int(np.argmax(sizes)))
    keep=nd.binary_dilation(keep,iterations=2)        # the figure and its soft edge, nothing stray (no shadow, no label)
    c[:,:,3]=np.where(keep,al,0)
    ys,xs=np.where(c[:,:,3]>60); c=c[ys.min():ys.max()+1, xs.min():xs.max()+1]
    H0=c.shape[0]; feet=c[int(H0*.86):int(H0*.94),:,3]>200; cols=nd.binary_dilation(feet.any(0),iterations=3)
    low=c[int(H0*.94):]; low[:,~cols,3]=0                    # the ground shadow between and beside the feet goes
    sh=low[:,:,:3]; grey=((sh.max(2)-sh.min(2)<16)&(sh.mean(2)<205)&(low[:,:,3]<235))|((sh.max(2)-sh.min(2)<40)&(low[:,:,3]<170)); low[grey,3]=0
    ys,xs=np.where(c[:,:,3]>60)
    cuts[k]=c[ys.min():ys.max()+1, xs.min():xs.max()+1]
# same height across a character's views: stand on the bottom edge, pad the top
for grp in (['front','back','side-left','side-right'],['male-front','male-back','male-side-left','male-side-right']):
    H=max(cuts[k].shape[0] for k in grp)
    for k in grp:
        c=cuts[k]; pad=H-c.shape[0]
        if pad: cuts[k]=np.concatenate([np.zeros((pad,c.shape[1],4),np.float32),c],0)
def hsv(rgb):
    r,g,b=[rgb[:,:,i]/255 for i in range(3)]; mx=np.max(rgb,2)/255; mn=np.min(rgb,2)/255; d=mx-mn+1e-6
    h=np.where(mx==r,((g-b)/d)%6,np.where(mx==g,(b-r)/d+2,(r-g)/d+4))*60
    s=np.where(mx>0,d/(mx+1e-6),0); return h,s,mx
report={}
for k,c in cuts.items():
    male=k.startswith('male-'); H,W=c.shape[:2]; rgb=c[:,:,:3]; al=c[:,:,3]; on=al>8
    h,s,v=hsv(rgb); y=np.arange(H)[:,None]/H*np.ones((1,W)); warm=rgb[:,:,0]-rgb[:,:,2]
    # rows where the black tank is: the band with the most neutral-black pixels between shoulders and waist
    black=on&(v<.46)&(warm<22)&(s<.45)
    rows=black.sum(1); band=(y>.10)&(y<.55)
    tr=[r for r in range(H) if .10*H<r<.55*H and rows[r]>max(3,W*.06)]
    t0,t1=(min(tr),max(tr)) if tr else (int(.18*H),int(.42*H))
    top=black&(y>=t0/H-.005)&(y<=t1/H+.01)
    gr=rgb[:,:,1]/(rgb[:,:,0]+1)
    olive=on&(gr>.83)&(gr<1.15)&(s>.15)&(v>.10)&(rgb[:,:,2]<rgb[:,:,1]-6)
    bot_rows=[r for r in range(H) if olive[r].sum()>W*.08]; b0,b1=min(bot_rows),max(bot_rows)
    bottoms=olive&(y>=b0/H)&(y<=b1/H+.01)
    skin=on&(gr>.55)&(gr<.83)&(s>.18)&(s<.8)&(v>.42)&~bottoms
    if male: shoes=on&(y>.90)&(s<.22)&(v>.55)&(al>120)         # white sneakers
    else:    shoes=on&(y>.90)&(v<.32)&(warm<20)&(al>120)        # black heeled sandals
    shoes&=~skin
    m=np.zeros((H,W),np.uint8)
    # fill each part solid (folds, seams, shading), on the figure only, without taking over another part
    def solidify(mask, it):
        mm=nd.binary_closing(mask,iterations=it); mm=nd.binary_fill_holes(mm); return mm&on
    S2=solidify(skin,2); T2=solidify(top,3); B2=solidify(bottoms,4); F2=solidify(shoes,2)
    def biggest(mm, share):
        lab,n=nd.label(mm)
        if not n: return mm
        sz=nd.sum(mm,lab,range(1,n+1)); return np.isin(lab, 1+np.where(sz>=sz.max()*share)[0])
    T2=biggest(T2,.25); B2=biggest(B2,.05); F2=biggest(F2,.15); S2=biggest(S2,.02)
    core=biggest(nd.binary_opening(T2,iterations=3),.5); T2=T2&nd.binary_dilation(core,iterations=3)   # the tank's main body only: hair shadows touching it stay hair
    # inside the tank's outline, row by row, anything dark that isn't skin is tank (shading, folds, strap edges)
    for r in range(H):
        xs=np.where(core[r])[0]
        if len(xs)>2: x0,x1=xs.min(),xs.max(); seg=on[r,x0:x1+1]&~S2[r,x0:x1+1]&(v[r,x0:x1+1]<.62); T2[r,x0:x1+1]|=seg
    m[S2]=1; m[T2]=2; m[B2]=3; m[F2]=4
    # the face and hands keep their skin, hair and accessories stay 0: drop skin specks inside hair-dark areas
    hairdark=on&(v<.42)&(warm>=14)
    m[(m==1)&hairdark]=0
    Image.fromarray(c.astype(np.uint8),'RGBA').save(OUT+k+'.webp','WEBP',lossless=False,quality=92,alpha_quality=100,method=6)
    Image.fromarray(m,'L').save(OUT+k+'-parts.png')
    report[k]=(W,H,{p:int((m==p).sum()) for p in range(5)},(t0,t1),(b0,b1))
for k,r in report.items(): print(k,r)
