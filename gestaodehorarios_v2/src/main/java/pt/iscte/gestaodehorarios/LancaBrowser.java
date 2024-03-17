package pt.iscte.gestaodehorarios;

import java.awt.Desktop;
import java.awt.event.*;
import java.io.IOException;
import java.net.URISyntaxException;
import javax.swing.*;    

public class LancaBrowser { 
	
	public static void main(String[] args) {  

		JFrame frame = new JFrame("A Minha Aplicação");  
	    JButton button = new JButton("Mostrar horário no Browser Web");  
	    button.setBounds(20,20,250,50);  
	    
	    button.addActionListener(new ActionListener(){  	
			public void actionPerformed(ActionEvent e){  
				Desktop desk = Desktop.getDesktop(); 
				try {
					desk.browse(new java.net.URI("http://localhost:8080/horario.html"));
				} catch (IOException | URISyntaxException e1) {e1.printStackTrace();} 
			}  
	    });
	    
	    frame.add(button);
	    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	    frame.setSize(400,400);  
	    frame.setLayout(null);  
	    frame.setVisible(true);   

	    System.out.println("Working Directory = " + System.getProperty("user.dir"));
	}  
}  

