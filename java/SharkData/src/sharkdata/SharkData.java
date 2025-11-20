package sharkdata;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

public class SharkData {
    public static void main(String[] args) {
        File myObj = new File("shark-data.txt");

        // try-with-resources: Scanner will be closed automatically
        try (Scanner fileScanner = new Scanner(myObj)) {
            ArrayList<shark>
            
            while (fileScanner.hasNextLine()) {
                String data = fileScanner.nextLine();
                String[] parts = data.split(":");
                
                String commonName = parts[0];
                String latinName = parts[1];
                int maxLength = Integer.parseInt(parts[2]);
                int maxDepth = Integer.parseInt(parts[3]);
                int maxChildren = Integer.parseInt(parts[4]);
                int globalPresence = Integer.parseInt(parts[5]);
                String oceanRegion = parts[6];
                
                new Shark(commonName, latinName, maxLength, maxDepth, maxChildren, globalPresence, oceanRegion);
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
    int maxLength;
    int maxDepth;
    int maxChildren;
    int globalPresence;
    String oceanRegion;
    
    public Shark(String commonName, String latinName, int maxLength, int maxDepth, int maxChildren, int globalPresence, String oceanRegion) {
        this.commonName = commonName;
        this.latinName = latinName;
        this.maxLength = maxLength;
        this.maxDepth = maxDepth;
        this.maxChildren = maxChildren;
        this.globalPresence = globalPresence;
        this.oceanRegion = oceanRegion;
    }
}
