import java.util.Scanner;
import java.io.File;
import java.io.IOException;

public class D2P1{

    public static boolean validPass(int lower, int upper, String letter, String password) {
        int count = 0; 
        for(int i = 0; i < password.length(); i++){
            if(password.charAt(i) == letter.charAt(0)){
                count++;
            }
        }
        return (count >= lower && count <= upper);
    }
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(new File("Inputs.dat"));
        int numOfValidPasswords = 0;
        while(input.hasNext()){
            String[] parts = input.nextLine().replaceAll(":", "").replaceAll("-", " ").split(" ");
            numOfValidPasswords += validPass(Integer.parseInt(parts[0]), Integer.parseInt(parts[1]), parts[2], parts[3]) ? 1 : 0;           
        }
        System.out.println(numOfValidPasswords);
        input.close();

    }
}