/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package hackathon_23;

/**
 *
 * @author ranjani
 */

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.event.ActionListener;
import java.io.File;
import javax.swing.*;
import java.util.ArrayList;
import java.util.Iterator;
import javax.imageio.ImageIO;

public class Preferencecs extends JFrame {
    
    JButton paint;
    JButton music;
    JButton science;
    JButton social;
    JButton tech;
    JButton reading;
    JButton physEd;
    
    JButton ready;
    JLabel answers;
    ArrayList<String> list_of_interests;

    public Preferencecs() {
        answers = new JLabel();
        this.setBackground(Color.BLACK);
        list_of_interests = new ArrayList();
        setLayout(new BorderLayout());
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ready = new JButton("Ready?");
        setBackground(Color.BLACK);
        ready.addActionListener(new ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                //System.out.println(list_of_interests);
                String result_string = "";
                Iterator i = list_of_interests.iterator();
                while(i.hasNext()){
                    result_string = result_string + i.next() + ", ";
                }
                System.out.println(result_string);
                JFrame frame = new JFrame();
                answers.setFont(new Font("EDWARDIAN", Font.PLAIN, 25));
                //Specs frame = new Specs();
               frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
               frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
               frame.setVisible(true);
        
                answers.setText("['PHIL 136N', 'CMPSC 101', 'ART 50', 'STAT 200', 'PHYS 250', 'PHYS 1H', 'PHIL 137N', 'LING 100', 'AIR 352', 'LTNST 315N']");
                frame.add(answers);
                frame.setVisible(true);
                
            }
        });
        //JPanel panel = new JPanel();
        try {
            paint = new JButton(new ImageIcon("C:\\Users\\91740\\OneDrive\\Documents\\CMPSC221\\New folder\\Paint.png"));
            paint.setOpaque(false);
            paint.addActionListener(new ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                list_of_interests.add("Painting");
            }
        });
            //paint.setLocation(400,600);
            music = new JButton(new ImageIcon("C:\\Users\\91740\\OneDrive\\Documents\\CMPSC221\\New folder\\Music.png"));
            music.setOpaque(false);
            music.addActionListener(new ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                list_of_interests.add("music");
            }
        });
            //music.setLocation(400,650);
            science = new JButton(new ImageIcon("C:\\Users\\91740\\OneDrive\\Documents\\CMPSC221\\New folder\\Science.png"));
            science.addActionListener(new ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                list_of_interests.add("science");
            }
        });
            tech = new JButton(new ImageIcon("C:\\Users\\91740\\OneDrive\\Documents\\CMPSC221\\New folder\\Technology.png"));
            tech.addActionListener(new ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                list_of_interests.add("tech");
            }
        });
            reading = new JButton(new ImageIcon("C:\\Users\\91740\\OneDrive\\Documents\\CMPSC221\\New folder\\Reading.png"));
            reading.addActionListener(new ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                list_of_interests.add("reading");
            }
        });
            physEd = new JButton(new ImageIcon("C:\\Users\\91740\\OneDrive\\Documents\\CMPSC221\\New folder\\PhysEd.png"));
            physEd.addActionListener(new ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                list_of_interests.add("sports");
            }
        });
            social = new JButton(new ImageIcon("C:\\Users\\91740\\OneDrive\\Documents\\CMPSC221\\New folder\\Social_Studies.png"));
            social.addActionListener(new ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                list_of_interests.add("history");
                list_of_interests.add("geography");
            }
        });
            JPanel panel1 = new JPanel();
            
            panel1.add(paint);
            panel1.add(music);
            panel1.add(science);
            panel1.add(tech);
            panel1.add(reading);
            panel1.add(physEd);
            panel1.add(social);
            panel1.add(ready);
            
            setPreferredSize(new Dimension(1800, 1000));
            setLayout(new BorderLayout());
            JLayeredPane lpane = new JLayeredPane();
            lpane.setBounds(-500,0,2000, 900);
            panel1.setBounds(0, 0, 1400,800);
            
            panel1.setOpaque(false);
            panel1.setVisible(true);
            JPanel panel2 = new JPanel();
            panel2.add(new JLabel(new ImageIcon(ImageIO.read(new File("C:\\Users\\91740\\OneDrive\\Documents\\CMPSC221\\bigbook.png")))));
            panel2.setBounds(-500, 0, 2000, 900);
            panel2.setVisible(true);
            panel2.setOpaque(true);
            lpane.add(panel1, 1, 0);
            lpane.add(panel2, 0, 0);
            pack();
            setVisible(true);
            add(lpane, BorderLayout.CENTER);
            
            setVisible(true);
            

        } catch (Exception e) {}

        
    }

}

