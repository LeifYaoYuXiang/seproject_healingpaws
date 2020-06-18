package sample;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;

public class Main extends Application {

    public void start(Stage primaryStage) throws Exception{

        FXMLLoader fxmlLoader = new FXMLLoader();
        fxmlLoader.setLocation(getClass().getResource("sample.fxml"));

        Parent root = fxmlLoader.load();
        primaryStage.setTitle("HealingPaws Control Panel");

        primaryStage.setScene(new Scene(root, 1280, 720));
        primaryStage.show();
        Controller controller = (Controller)fxmlLoader.getController();
        controller.init();
    }



    public static void main(String[] args) {
        launch(args);
    }
}
