import java.util.Scanner;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class D1P1{
    public static void main(String[] args) throws IOException {
        File file = new File("Part One/Inputs.adventofcodeinputs");
        Scanner inputs = new Scanner( file );
        ArrayList<Integer> nums = new ArrayList<>();
        while(inputs.hasNextLine()){
            int num = inputs.nextInt();
            if(num > 1793){
                continue;
            }
            else {
                nums.add(num);
            }
        }
        for(int i = 0; i < nums.size(); i++){
            for(int j = 0; j < nums.size(); j++){
                if(nums.get(i) + nums.get(j) == 2020){
                    System.out.println(nums.get(i) * nums.get(j));
                }
            }
        }
    }
}