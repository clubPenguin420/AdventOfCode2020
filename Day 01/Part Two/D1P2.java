import java.util.Scanner;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class D1P2 {

    public static long solve(ArrayList<Integer> nums){
        for(int i = 0; i < nums.size(); i++){
            for(int j = 0; j < nums.size(); j++){
                for(int k = 0; k < nums.size(); k++){
                    if(nums.get(i) + nums.get(j) + nums.get(k) == 2020){
                        return nums.get(i) * nums.get(j) * nums.get(k);
                    }
                }
            }
        }
        return -1;
    }
    public static void main(String[] args) throws IOException {
        Scanner inputs = new Scanner( new File("Inputs.dat") );
        ArrayList<Integer> nums = new ArrayList<>();
        while(inputs.hasNextLine()){
            int num = inputs.nextInt();
                nums.add(num);
        }
        System.out.println(solve(nums));

    }
}
