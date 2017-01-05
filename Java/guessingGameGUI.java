/*
*
* This program is a simple guessing game that has a user guess 
* a bounded randomly generated number and gives feed back based on 
* number of guesses
*
*/

import java.util.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;



public class guessingGameGUI extends JFrame
{
   private int range;
   private int tolerance;
   private int rand;
   private int count = 0;
   private String response;
   private Random random = new Random();
   private JPanel panel;
   private JPanel panel2; 
   private JPanel resultPanel;            
   private JLabel messageLabel;
   private JLabel messageLabel2; 
   private JLabel messageLabel3; 
   private JLabel responseLabel;
   private JLabel scoreLabel; 
   private JLabel lower; 
   private JLabel upper;
   private JTextField lowerText;
   private JTextField upperText; 
   private JTextField guessText;
   private JButton submit;
   private JButton enter;
   private JButton replay;
   private JButton quit;      
   private final int WINDOW_WIDTH = 600;  
   private final int WINDOW_HEIGHT = 100; 

   /*
      Constructor
   */

   public guessingGameGUI()
   {
      setTitle("Guessing Game") ;
      GridBagConstraints gbc = new GridBagConstraints();
      setSize(WINDOW_WIDTH, WINDOW_HEIGHT) ;
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE) ;
      setLocationRelativeTo(null);
      buildPanel();
      buildPanel2();
      add(panel) ;
      setVisible(true) ;

   /*
      The buildPanel method adds a label, text field, and
      and a button to a panel.
   */
}
   private void buildPanel()
   {
      JOptionPane.showMessageDialog(null, "Enter a lower and upper bound. I will choose a number at random in the range."); 
      lower = new JLabel("Lower Bound: ");
      upper = new JLabel("Upper Bound: ");
      lowerText = new JTextField(5);
      upperText = new JTextField(5);
      submit = new JButton("Submit");
      submit.addActionListener(new ButtonListenerS()) ;
      panel = new JPanel() ;
      panel.setLayout(new GridBagLayout());
      GridBagConstraints gbc = new GridBagConstraints();      
      panel.add(lower, gbc) ;
      panel.add(lowerText, gbc) ;
      panel.add(upper, gbc) ;
      panel.add(upperText, gbc) ;
      panel.add(submit) ;

   }
   private void buildPanel2()
   {
      messageLabel2 = new JLabel("Enter guesses until you guess the right number") ;
      guessText = new JTextField(5);
      enter = new JButton("Enter");
      enter.addActionListener(new ButtonListenerE());
      panel2 = new JPanel();
      panel2.add(messageLabel2);
      panel2.add(guessText) ;
      panel2.add(enter);
   }
   private void buildResultPanel()
   {
      if (count == 1)
      {
         response = "Wow only one try! You're ethier very lucky or you just picked a small range.";
      }
      else if (count < tolerance)
      {
         response = "Nice Job, you couldn't have done any better unless you guessed it in one try and thats just luck anyway,";
      }
      else if (count == tolerance)
      {
         response = "Pretty mediocre, dont quit your day job";
      }
      else 
      {  
         response = "Not very good, I would suggest you look up how binary search works";
      }
      messageLabel3 = new JLabel("You Guessed Correct!");
      scoreLabel = new JLabel(String.format("Tolerance: %d Guesses: %d", tolerance, count));
      responseLabel = new JLabel(response);
      replay = new JButton("Play Again");
      quit = new JButton("Quit Game");
      replay.addActionListener(new ButtonListenerR());
      quit.addActionListener(new ButtonListenerQ());
      resultPanel = new JPanel();
      resultPanel.setLayout(new BoxLayout(resultPanel, BoxLayout.Y_AXIS));
      resultPanel.add(messageLabel3);
      resultPanel.add(scoreLabel);
      resultPanel.add(responseLabel);
      resultPanel.add(replay);
      resultPanel.add(quit);
   }

   private class ButtonListenerS implements ActionListener
   {

      public void actionPerformed(ActionEvent e)
      {
         int lowerInput = Integer.parseInt(lowerText.getText());
         int upperInput = Integer.parseInt(upperText.getText());

         if (lowerInput >= upperInput)
         {
            JOptionPane.showMessageDialog(null, "Invalid range, lower bound must less than upper bound."); 
            new guessingGameGUI();  
            dispose();
         }
         else
         {
            range = upperInput - lowerInput;
            rand = random.nextInt(range + 1) + lowerInput;
            if (range == 1)
            {
               tolerance = 1;
            }
            else 
            {   
               tolerance = (int) (Math.log((double) range)/Math.log(2.0));
            }

            getContentPane().removeAll();
            getContentPane().add(panel2);
            validate();   
         }   

         
      }
   }
   private class ButtonListenerE implements ActionListener
   {
      private String encouragement = "Keep guessing!";

      public void actionPerformed(ActionEvent e)
      {
         count++;
         if (count > tolerance)
         {
           encouragement = "You're guessing quite a lot are you sure you know how to play?";
         }

         int guessInput = Integer.parseInt(guessText.getText());
         if (guessInput > rand)
         {
            JOptionPane.showMessageDialog(null, String.format("Guess too High. %s", encouragement)); 
         }
         else if (guessInput < rand)
         {
            JOptionPane.showMessageDialog(null, String.format("Guess too Low. %s", encouragement)); 
         }
         else
         {
            buildResultPanel();
            getContentPane().removeAll();
            getContentPane().add(resultPanel);
            validate();
         }   
      }

   }
   private class ButtonListenerR implements ActionListener
   {
      public void actionPerformed(ActionEvent e)
      {
         new guessingGameGUI();
         dispose();
      }
   }
   private class ButtonListenerQ implements ActionListener
   {
      public void actionPerformed(ActionEvent e)
      {

         System.exit(0);
      }
   }
   public static void main(String[] args)
   {
      new guessingGameGUI() ;
   }
}
