package pt.iscte.gestaodehorarios;

import java.awt.Desktop;
import java.awt.event.*;
import java.io.IOException;
import java.net.URISyntaxException;
import javax.swing.*;    

public class LancaBrowser { 
	
	public static void main(String[] args) {  

		JFrame frame = new JFrame("A Minha Aplicação");  
	    JButton button1 = new JButton("Mostrar horário no Browser Web");  
	    button1.setBounds(20,20,250,50); 
	    JButton button2 = new JButton("Mostrar salas no Browser Web");  
	    button2.setBounds(20,80,250,50); 
	    
	    button1.addActionListener(new ActionListener(){  	
			public void actionPerformed(ActionEvent e){  
				Desktop desk = Desktop.getDesktop(); 
				try {
					desk.browse(new java.net.URI("http://localhost:8080/horario.html"));
				} catch (IOException | URISyntaxException e1) {e1.printStackTrace();} 
			}  
	    });	   
	    
	    button2.addActionListener(new ActionListener(){  	
			public void actionPerformed(ActionEvent e){  
				Desktop desk = Desktop.getDesktop(); 
				try {
					desk.browse(new java.net.URI("http://localhost:8080/salas.html"));
				} catch (IOException | URISyntaxException e1) {e1.printStackTrace();} 
			}  
	    });
	    
	    frame.add(button1);
	    frame.add(button2);
	    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	    frame.setSize(400,400);  
	    frame.setLayout(null);  
	    frame.setVisible(true);   

	    System.out.println("Working Directory = " + System.getProperty("user.dir"));
	}  
}  

