import java.util.Scanner;
import java.io.File;
import java.io.IOException;

public class D6P1{
    private static String removeDupChars(String s) {
        char[] chrArray = s.toCharArray();
        String newS = "";

        for (char value : chrArray) {
            if (newS.indexOf(value) == -1) {
                newS += value;
            }
        }
        return newS;
    }
    public static void main(String[] args) throws IOException {
        Scanner inputs = new Scanner(new File("Inputs.dat")); 
        int num = 0;
        String answers = "";
        int x = 0;
        while(inputs.hasNextLine()){
            String line = inputs.nextLine();
            if(line.equals("")){
                num += removeDupChars(answers).length();
                answers = "";
            }
            else{
                answers += line;
            }
        }
        System.out.println(num);
    }
}