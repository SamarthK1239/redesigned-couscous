/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package hackathon_23;

/**
 *
 * @author ranjani
 */
import javax.swing.*;
import java.awt.*;
import java.io.File;
import javax.imageio.ImageIO;

public class testing_animation extends JFrame {

    public testing_animation() {
        super("window");
        this.setLocationRelativeTo(null);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        try {
            String file_name = "frame1";
            setContentPane(new JLabel(new ImageIcon(ImageIO.read(new File("C:\\Users\\91740\\OneDrive\\Documents\\CMPSC221\\animation pics\\"+file_name+".jpg")))));
            setLayout(new FlowLayout());
            setResizable(false);
            pack();
            setVisible(true);
            for (int i = 1; i<=10; i++){
                file_name = "frame"+(i);
                setContentPane(new JLabel(new ImageIcon(ImageIO.read(new File("C:\\Users\\91740\\OneDrive\\Documents\\CMPSC221\\animation pics\\"+file_name+".jpg")))));
                repaint();
                setVisible(true);
                pack();
                Thread.sleep(1000);
            }
        } catch (Exception e) {}
        
    }
}
