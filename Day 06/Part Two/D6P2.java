import java.util.Scanner;
import java.util.Set;
import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class D6P2{
        public static void main(String[] args) throws IOException {
        Scanner inputs = new Scanner(new File("Inputs.dat")); 
        int num = 0;
        String answers = "";    
        Map<Character, Integer> letFreq = new HashMap<Character, Integer>();
        while(inputs.hasNextLine()){
            String line = inputs.nextLine();
            if(line.equals("")){
                String[] ans = answers.split(" ");
                
                for(int i = 0; i < ans.length; i++){
                    String answer = ans[i];
                    for(int j = 0; j < answer.length(); j++) {
                        if(letFreq.containsKey(answer.charAt(j))){
                            letFreq.put(answer.charAt(j), letFreq.get(answer.charAt(j)) + 1);
                        }else {
                            letFreq.put(answer.charAt(j), 1);
                        }
                    }
                }
                int count = 0;
                System.out.println(letFreq.keySet());
                    Set letters = letFreq.keySet();
                    for (Object letter : letters) {
                        int value = letFreq.get(letter);
                        if(value == ans.length){
                            System.out.println(value);
                            count++;
                        }
                    }
                num += count;
                answers = "";
                letFreq.clear();
            }
            else{
                answers += line + " ";
            }
        }
        System.out.println(num);
    }
}