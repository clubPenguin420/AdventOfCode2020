import java.util.Scanner;
import java.io.File;
import java.io.IOException;

public class D2P2{

    public static boolean validPass(int firstLoc, int secondLoc, String letter, String password) {
        return (password.charAt(firstLoc - 1) == letter.charAt(0) ^ password.charAt(secondLoc - 1) == letter.charAt(0));
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