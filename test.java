import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MainApp extends JFrame {
    private JButton openButton;
    private JLabel label;

    public MainApp() {
        setTitle("Java GUI App");
        setSize(400, 200);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        openButton = new JButton("Open File Dialog");
        label = new JLabel();

        openButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JFileChooser fileChooser = new JFileChooser();
                int returnValue = fileChooser.showOpenDialog(null);
                if (returnValue == JFileChooser.APPROVE_OPTION) {
                    String selectedFile = fileChooser.getSelectedFile().getPath();
                    label.setText("Selected file: " + selectedFile);
                }
            }
        });

        setLayout(new FlowLayout());
        add(openButton);
        add(label);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                MainApp app = new MainApp();
                app.setVisible(true);
            }
        });
    }
}
