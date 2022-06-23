import java.awt.*;
import java.awt.event.*;

class TemperatureConverter extends WindowAdapter implements ActionListener{

    Frame mainFrame;

    TextField fahrenheit,celsius;

    Label fahrenheitLabel,celsiusLabel;

    Button fahrenheitButton,celsiusButton;

    public TemperatureConverter(){

        mainFrame=new Frame();
        mainFrame.setSize(300,300);

        mainFrame.setBackground(Color.cyan);
        mainFrame.addWindowListener(this);

        GridLayout gl1=new GridLayout(3,1);

        GridLayout gl2=new GridLayout(1,2);

        Font fon=new Font("Arial",Font.BOLD,20);
        
        mainFrame.setLayout(gl1);

        Panel p1=new Panel();
        p1.setLayout(gl2);

        fahrenheitLabel=new Label("Fahrenheit  ");
        fahrenheitLabel.setFont(fon);
        p1.add(fahrenheitLabel);

        fahrenheit=new TextField("");
        fahrenheit.setFont(fon);
        fahrenheit.setText("32.0");
        p1.add(fahrenheit);

        mainFrame.add(p1);

        p1=new Panel();
        p1.setLayout(gl2);
        celsiusLabel=new Label("Celsius  ");
        celsiusLabel.setFont(fon);
        p1.add(celsiusLabel);

        celsius=new TextField("");
        celsius.setFont(fon);
        celsius.setText("0.0");
        p1.add(celsius);

        mainFrame.add(p1);

        p1=new Panel();
        p1.setLayout(gl2);
        celsiusButton=new Button(">>>>    ");
        celsiusButton.setFont(fon);
        p1.add(celsiusButton);

        fahrenheitButton=new Button("<<<<    ");
        fahrenheitButton.setFont(fon);
        p1.add(fahrenheitButton);

        mainFrame.add(p1);

        celsiusButton.addActionListener(this);
        fahrenheitButton.addActionListener(this);

        mainFrame.setVisible(true);
    }
    public void actionPerformed(ActionEvent e){
        if(e.getActionCommand().equals(">>>>    ")){

            String c = celsius.getText();
            double cel = Double.parseDouble(c);

            double fah = (cel*9)/5 + 32;

            fahrenheit.setText((""+fah));
        }

        else if(e.getActionCommand().equals("<<<<    ")){
  
            String f = fahrenheit.getText();
            double fah = Double.parseDouble(f);

            double cel = ((fah - 32) * 5)/9;

            celsius.setText((""+cel));
        }
    }
    public void windowClosing(WindowEvent e){
        Window w=e.getWindow();
        w.setVisible(false);
        w.dispose();
        System.exit(1);
    }
    public static void main(String arg[]){
        TemperatureConverter tc=new TemperatureConverter();
    }
}