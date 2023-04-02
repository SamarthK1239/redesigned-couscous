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

public class WelcomePage extends JFrame{
    JButton start = new JButton("Ready to begin?");
    JLabel welcome = new JLabel("Welcome to GenEasy!");
    JLabel welcome2 = new JLabel("Making choosing classes easier since... what's today again?");
    JPanel top = new JPanel();
    JPanel main;
    public WelcomePage(){
        try {
            top.setLayout(new GridLayout(3,0));
            top.add(welcome);
            top.add(welcome2);
            top.add(start);
            //add(top, SwingConstants.NORTH);
            setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            String file_name = "frame_02_delay-0.07s";
            setContentPane(new JLabel(new ImageIcon(ImageIO.read(new File("C:\\Users\\91740\\OneDrive\\Documents\\CMPSC221\\animation pics\\"+file_name+".jpg")))));
            setLayout(new FlowLayout());
            repaint();
            pack();
            setVisible(true);
            
            for(int i = 2; i<79; i++){
                if (i==70) i = 2;
                if (i==18) i++;
                if (i<10) 
                    file_name = "frame_0"+i+"_delay-0.07s";
                else
                    file_name = "frame_"+i+"_delay-0.07s";
                if (i==27||i ==24) 
                    file_name = "frame_"+i+"_delay-0.06s";
                setContentPane(new JLabel(new ImageIcon(ImageIO.read(new File("C:\\Users\\91740\\OneDrive\\Documents\\CMPSC221\\animation pics\\"+file_name+".jpg")))));
                //System.out.println(i);
                setVisible(true);
                repaint();
                pack();
                Thread.sleep(50);
                setVisible(true);
                
            }
        } catch (Exception e) {}
        //make the label stay while other stuff is going
    }
}
