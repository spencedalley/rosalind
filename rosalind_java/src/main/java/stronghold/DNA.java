package stronghold;

public class DNA {
    private String mDNA = null;
    private double mGcContent = 0.0;

    public DNA(String nucleotideString) {
        this.mDNA = nucleotideString.toUpperCase();
        this.mGcContent = this.computeGcContent();
    }

    public void setDNA(String newNucleotideString) {
        this.mDNA = newNucleotideString.toUpperCase();
        this.mGcContent = this.computeGcContent();
    }

    public String getDNA() {
        return mDNA; 
    }

    public int[] countNucleotides() {
        int aCount = 0; 
        int cCount = 0; 
        int gCount = 0; 
        int tCount = 0; 

        for (int i = 0; i < mDNA.length(); i++) {
            switch (mDNA.charAt(i)) {
                case 'A': 
                    aCount += 1; 
                    break; 
                case 'C': 
                    cCount += 1; 
                    break; 
                case 'G': 
                    gCount += 1; 
                    break; 
                case 'T': 
                    tCount += 1; 
                    break; 
                default: 
                    break; 
            }
        }

        return new int[] { aCount, cCount, gCount, tCount };
    }

    public String transcribeToRNA() {
        StringBuilder rna = new StringBuilder(); 

        for (char nucleotide: mDNA.toCharArray()) {
            if (nucleotide == 'T') {
                rna.append('U'); 
            } else {
                rna.append(nucleotide); 
            }
        }

        return rna.toString(); 
    }

    public String complementDNA() {
        // Returns the complement of the DNA strand
        String complement = new StringBuilder(mDNA).reverse().toString(); 
        StringBuilder result = new StringBuilder(); 

        for (int i = 0; i < complement.length(); i++) {
            char nucleotide = complement.charAt(i); 
            switch (nucleotide) {
                case 'A': 
                    result.append('T'); 
                    break; 
                case 'C': 
                     result.append('G'); 
                     break; 
                case 'G': 
                    result.append('C'); 
                    break; 
                case 'T': 
                    result.append('A'); 
                    break; 
                default: 
                    break; 
            }
        }

        return result.toString(); 
    }

    double computeGcContent() {

        return 0.0;
    }
}
