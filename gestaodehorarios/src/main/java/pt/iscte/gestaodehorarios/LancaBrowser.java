package pt.iscte.gestaodehorarios;

import java.awt.Desktop;
import java.awt.event.*;
import java.io.File;
import java.io.IOException;
//import java.net.URISyntaxException;
import javax.swing.*;    

public class LancaBrowser { 
	
	public static void main(String[] args) {  

		JFrame frame = new JFrame("A Minha Aplicação");  
	    JButton button = new JButton("Mostrar Salas no Browser Web");  
	    button.setBounds(20,20,250,50);  
	    button.addActionListener(new ActionListener(){  	
			public void actionPerformed(ActionEvent e){  
				Desktop desk = Desktop.getDesktop(); 
				try {
					 // Constructing the file path based on the new directory structure
		            String filePath = System.getProperty("user.dir") + "/src/main/java/pt/iscte/gestaodehorarios/horario.html";
		            // Replacing backslashes with forward slashes in the file path
		            //filePath = filePath.replace("\\", "/");
		            desk.browse(new File(filePath).toURI());
				} catch (IOException e1) {e1.printStackTrace();} 
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

