import java.util.Scanner;
import java.io.File;
import java.io.IOException;

public class D3P1 {
    public static void main(String[] args) throws IOException {
        Scanner inputs = new Scanner(new File("Inputs.dat"));
        String[] map = new String[323];
        int numOfTrees = 0;

        int i = 0;
        while(inputs.hasNext()){
            map[i] = inputs.nextLine();
            i++;
        }
        
        for(i = 0; i < map.length; i++){
            String line = map[i];
            numOfTrees += (line.charAt((i * 3) % 31) == '#') ? 1 : 0;
        }
        System.out.println(numOfTrees);
    }
}
