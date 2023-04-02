/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package hackathon_23;

/**
 *
 * @author ranjani
 */
public class Student {
    Degree major;
    Degree minor;
    int year;
    int max_credits;
    boolean summer;
    public Student(String major_name, String minor_name, int year, int max_credits, boolean summer){
        major = new Degree(major_name);
        major.ismajor = true;
        if (minor_name.equals("Enter a minor") == false){
            minor = new Degree(minor_name);
            minor.isminor = true;
        }
        
    }
    public Student(){
        major = new Degree("CMPSC");
        minor = null;
        year = 1;
        max_credits = 12;
        summer = false;
    }
         
}
