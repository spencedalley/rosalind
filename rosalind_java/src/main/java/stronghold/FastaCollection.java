package stronghold;

import java.util.ArrayList;
import java.util.HashMap;

public class FastaCollection {
    private HashMap<String, DNA> fastaHashMap = null;
    private String fastaFilePath = null;

    public FastaCollection(String fastaFilePath) {
        this.fastaFilePath = fastaFilePath;
        this.fastaHashMap = fastaToHashMap();
    }

    private HashMap<String, DNA> fastaToHashMap() {
        try {

        } catch (Exception e) {

        }

        return null;
    }

    private String[] readInFastaFile() {
        // Returns string array of lines of file
        ArrayList<String> result = new ArrayList<String>();

        return null;
    }

    private boolean isFastaTag(String line) {
        String fastaTagPattern = "(>)(.+)";
        boolean outcome = line.matches(fastaTagPattern);

        if (outcome) {
            return true;
        } else {
            return false;
        }
    }
}
