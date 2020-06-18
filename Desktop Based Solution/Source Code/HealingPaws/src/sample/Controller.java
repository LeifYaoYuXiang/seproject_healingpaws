package sample;
import javafx.scene.web.WebView;
public class Controller {
    public WebView webview;
    public static String homePageUrl = "http://118.190.152.62:5000/login";


    /**
     * 初始化
     */
    public void init() {
        home();
    }

    public void home() {
        // 跳转默认首页
        goTo(homePageUrl);
    }

    /**
     * 跳转的通用方法
     */
    public void goTo(String urlString) {
        webview.getEngine().load(urlString);
    }
}
