/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package hackathon_23;

import java.awt.*;
import java.awt.event.ActionListener;
import java.io.File;
import javax.swing.*;
import java.util.ArrayList;
import javax.imageio.ImageIO;

//import uk.co.caprica.vlcj.binding.LibVlc;
//import uk.co.caprica.vlcj.player.MediaPlayerFactory;
//import uk.co.caprica.vlcj.player.embedded.EmbeddedMediaPlayer;
//import uk.co.caprica.vlcj.runtime.RuntimeUtil;
/**
 *
 * @author ranjani
 */
public class Specs extends JFrame{
    ArrayList<String> classes_list;
    Student student;
    JTextField major_name;
    JTextField minor_name;
    JTextField years;
    //JSpinner max_credits;
    //JCheckBox summer;
    JButton done;
    public Specs(){
        setLayout(new BorderLayout());
        //for the entered info
         classes_list = new ArrayList();
         student = new Student();
         major_name = new JTextField("Major. Ex: CMPSC");
         major_name.setLocation(400,900);
         minor_name = new JTextField("Minor. Ex: MATH");
         years = new JTextField("Current year. Ex:1");
         /*max_credits = new JSpinner(new SpinnerNumberModel(16, //initial value
                12, //minimum value
                24, //maximum value
                1)); //step)
         */
         JTextArea class_text = new JTextArea("Enter the classes you've taken! Ex: CMPSC131, ENGL15. If you havent taken any yet, just leave this as is.");
         //summer = new JCheckBox("Do you have no summer plans, ever?");
         done = new JButton("Done?"); 
         done.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                try{
                    student = new Student(major_name.getText(), minor_name.getText(), Integer.parseInt(years.getText()), 16, false);
                    System.out.println(student.major+""+ student.year+""+ student.max_credits+""+ student.summer);
                    setVisible(false);
                    Preferencecs frame2 = new Preferencecs();
                    frame2.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                    frame2.setExtendedState(JFrame.MAXIMIZED_BOTH);
                    frame2.setVisible(true);
                }
                catch(Exception e){
                    System.out.println("Whoops! Looks like something is missing. Check your answers!");
                }
                
            }
        });
        setLocationRelativeTo(null);
        
        try {
            String file_name = "frame_02_delay-0.1s";
            setContentPane(new JLabel(new ImageIcon(ImageIO.read(new File("C:\\Users\\91740\\OneDrive\\Documents\\CMPSC221\\animation pics\\"+file_name+".jpg")))));
            setLayout(new BorderLayout());
            setResizable(false);
            pack();
            setVisible(true);
            for (int i = 2; i<=99; i++){
                if (i<10) 
                    file_name = "frame_0"+i+"_delay-0.1s";
                else
                    file_name = "frame_"+i+"_delay-0.1s";
                setContentPane(new JLabel(new ImageIcon(ImageIO.read(new File("C:\\Users\\91740\\OneDrive\\Documents\\CMPSC221\\animation pics\\"+file_name+".jpg")))));
                repaint();
                setVisible(true);
                pack();
                Thread.sleep(50);
            }
        } catch (Exception e) {}
        
    
        //booleans
        setLayout(new FlowLayout());
        try{
        add(major_name);
        Thread.sleep(100);
        setVisible(true);
        add(minor_name);
        Thread.sleep(100);
        setVisible(true);
        add(years);
        Thread.sleep(100);
        setVisible(true);
        //add(max_credits);
        //Thread.sleep(100);
        setVisible(true);
        //add(summer);
        //Thread.sleep(100);
        setVisible(true);
        add(class_text);
        Thread.sleep(100);
        setVisible(true);
        add(done, BorderLayout.EAST);
        setVisible(true);
        }
        catch(Exception e){}
        
        String classes = class_text.getText()+",";
         String s = "";
             for(int i = 0; i<classes.length(); i++){
                 char c = classes.charAt(i);
                 if (c == ','){
                     classes_list.add(s);
                     s = "";
                }
                 else
                     s+=c;
             }
        repaint();
        setVisible(true);
        pack();
        
    }
}
