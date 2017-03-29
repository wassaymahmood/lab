/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication10;
import java.io.BufferedReader;
import java.io.FileReader;
import java.sql.*;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.IOException;

/**
 *
 * @author DELL
 */
public class JavaApplication10 {
    
    public static  String read(String a){
    BufferedReader reader = null;
    			String line = null;

		
		try {
			reader = new BufferedReader(new FileReader(a));
			
			// How to read file in java line by line?
			while ((line = reader.readLine()) != null) {
				System.out.println("Raw CSV data: " + line);
				//System.out.println("Converted ArrayList data: " + wCSVtoArrayList(line) + "\n");
			}
			
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if (reader != null) reader.close();
			} catch (IOException wException) {
				wException.printStackTrace();
			}
		}
        
        return line;
    
    
    }
    
    
   
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
    String r = read("GeoLiteCity-Location.csv");
    }
}
