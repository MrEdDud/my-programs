package sharkdata;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class SharkData {
    public static void main(String[] args) {
        File myObj = new File("shark-data.txt");

        // try-with-resources: Scanner will be closed automatically
        try (Scanner myReader = new Scanner(myObj)) {
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String[] parts = data.split(":");
                
                Shark shark = new Shark(parts);
            }
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}

class Shark {
    String commonName;
    String latinName;
    String maxLength;
    String maxDepth;
    String maxChildren;
    String globalPresence;
    String oceanRegion;
    
    Shark(String[] parts) {
        this.commonName = parts[0];
        this.latinName = parts[1];
        this.maxLength = parts[2];
        this.maxDepth = parts[3];
        this.maxChildren = parts[4];
        this.globalPresence = parts[5];
        this.oceanRegion = parts[6];
        
        System.out.println(this.commonName);
    }
}
