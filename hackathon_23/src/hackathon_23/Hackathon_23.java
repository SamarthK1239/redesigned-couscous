/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package hackathon_23;

/**
 *
 * @author ranjani
 */
import javax.swing.*;
import java.awt.*;

public class Hackathon_23 extends JFrame {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        /*testing_animation framex = new testing_animation();
        framex.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        framex.setExtendedState(JFrame.MAXIMIZED_BOTH);
        framex.setVisible(true);
         */
        //WelcomePage frame2 = new WelcomePage();
        //frame2.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        //frame2.setVisible(true);
        try {
            Process p = Runtime.getRuntime().exec("python master_recommender.py");
            Specs frame = new Specs();
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
            frame.setVisible(true);

        } catch (Exception e) {
            System.out.println("Error");
        }

        // TODO code application logic here
    }

}
