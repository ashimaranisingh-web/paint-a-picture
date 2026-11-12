import PostHog
import UIKit

/// A plain UIKit app with one scene and one screen, the web view, so the status bar can follow the page.
@main
final class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(_: UIApplication, didFinishLaunchingWithOptions _: [UIApplication.LaunchOptionsKey: Any]? = nil) -> Bool {
        let environment = ProcessInfo.processInfo.environment
        let info = Bundle.main.infoDictionary
        guard let projectToken = environment["POSTHOG_PROJECT_TOKEN"] ?? info?["POSTHOG_PROJECT_TOKEN"] as? String,
              !projectToken.isEmpty else {
#if DEBUG
            assertionFailure("POSTHOG_PROJECT_TOKEN variable required by PostHog is missing or un-configured, this causes events to be silently missed. This error stops appearing once POSTHOG_PROJECT_TOKEN is configured")
#endif
            return true
        }

        guard let host = environment["POSTHOG_HOST"] ?? info?["POSTHOG_HOST"] as? String,
              !host.isEmpty else {
#if DEBUG
            assertionFailure("POSTHOG_HOST variable required by PostHog is missing or un-configured, this causes events to be silently missed. This error stops appearing once POSTHOG_HOST is configured")
#endif
            return true
        }

        let config = PostHogConfig(projectToken: projectToken, host: host)
        config.errorTrackingConfig.autoCapture = true
        config.logs.serviceName = "paint-a-picture-ios"
        PostHogSDK.shared.setup(config)
        PostHogSDK.shared.logger?.info("app_launch_completed")
        return true
    }

    func application(_ application: UIApplication, configurationForConnecting session: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration {
        let config = UISceneConfiguration(name: "Default", sessionRole: session.role)
        config.delegateClass = SceneDelegate.self
        return config
    }
}

final class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options: UIScene.ConnectionOptions) {
        guard let scene = scene as? UIWindowScene else { return }
        let window = UIWindow(windowScene: scene)
        window.backgroundColor = UIColor(named: "LaunchBackground")
        window.rootViewController = WebViewController()
        window.makeKeyAndVisible()
        self.window = window
    }
}
