import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.Random;

public class RandomPasswordGenerator extends JFrame {
    private JTextField lengthField;
    private JTextArea passwordArea;
    private JButton generateButton;

    public RandomPasswordGenerator() {
        setTitle("Random Password Generator");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 200);
        setLayout(new GridLayout(3, 1));

        JPanel lengthPanel = new JPanel();
        lengthPanel.setLayout(new FlowLayout());
        JLabel lengthLabel = new JLabel("Password Length:");
        lengthField = new JTextField(10);
        lengthPanel.add(lengthLabel);
        lengthPanel.add(lengthField);

        JPanel generatePanel = new JPanel();
        generateButton = new JButton("Generate Password");
        generateButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                generatePassword();
            }
        });
        generatePanel.add(generateButton);

        JPanel passwordPanel = new JPanel();
        passwordArea = new JTextArea(5, 20);
        passwordPanel.add(new JScrollPane(passwordArea));

        add(lengthPanel);
        add(generatePanel);
        add(passwordPanel);
    }

    private void generatePassword() {
        int length;
        try {
            length = Integer.parseInt(lengthField.getText());
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "Invalid input. Please enter a valid number.");
            return;
        }

        if (length < 8) {
            JOptionPane.showMessageDialog(this, "Password length should be at least 8 characters.");
            return;
        }

        String symbols = "!@#$%^&*()-_=+[]{}|;:'\",.<>?";
        String digits = "0123456789";
        String lowercaseLetters = "abcdefghijklmnopqrstuvwxyz";
        String uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        String allCharacters = symbols + digits + lowercaseLetters + uppercaseLetters;
        StringBuilder password = new StringBuilder();

        Random random = new Random();
        for (int i = 0; i < length; i++) {
            int index = random.nextInt(allCharacters.length());
            password.append(allCharacters.charAt(index));
        }

        passwordArea.setText(password.toString());
        passwordArea.selectAll();
        passwordArea.copy();
        JOptionPane.showMessageDialog(this, "Password copied to clipboard!");
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new RandomPasswordGenerator().setVisible(true);
            }
        });
    }
}
