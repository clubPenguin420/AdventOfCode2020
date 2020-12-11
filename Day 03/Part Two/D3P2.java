import java.util.Scanner;
import java.io.File;
import java.io.IOException;

public class D3P2 {

    public static long trees(int right, int down, String[] map) {
        int numOfTrees = 0;
        for(int i = 0, x = 0; i < map.length; i += down, x++){
            String line = map[i];
            // System.out.println(i + " - " + line.charAt((i * right) % 31));
            numOfTrees += (line.charAt((x * right) % 31) == '#') ? 1 : 0;
        }
        return numOfTrees;
    }
    public static void main(String[] args) throws IOException {
        Scanner inputs = new Scanner(new File("Inputs.dat"));
        String[] map = new String[323];
 
        int i = 0;
        while(inputs.hasNext()){
            map[i] = inputs.nextLine();
            i++;
        }
 
        System.out.println(trees(1, 1, map) * trees(3, 1, map) * trees(5, 1, map) * trees(7, 1, map) * trees(1, 2, map));

    }
}
