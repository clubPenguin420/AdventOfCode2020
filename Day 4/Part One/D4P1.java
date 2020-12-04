import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.IOException;

public class D4P1 {
    public static void main(String[] args) throws IOException{
        Scanner inputs = new Scanner(new File("Inputs.dat"));
        String[] passports = new String[295];
        int i = 0;
        while(inputs.hasNext()){
            String line = inputs.nextLine();
            if(line.equals("")){i++; continue;}
            if(passports[i] == null){
                passports[i] = line + " ";
            }
            else{
                passports[i] += line + " ";
            }
        }
        int count = 0;
        for(i = 0; i < passports.length; i++){
            if(passports[i].contains("byr") && passports[i].contains("iyr") && passports[i].contains("eyr") && passports[i].contains("hgt") && passports[i].contains("hcl") && passports[i].contains("ecl") && passports[i].contains("pid")){
                count++;
            }
        }
        System.out.println(count);
}
}
