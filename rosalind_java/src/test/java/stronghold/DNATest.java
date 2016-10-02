import java.util.Arrays;

import org.junit.Test;
import static org.junit.Assert.*;

import stronghold.DNA;

public class DNATest {

    @Test public void testCountNucleotides() {
        DNA dnaTest = new DNA("actggg");
        int[] expected = { 1, 1, 3, 1 }; 
        int[] result = dnaTest.countNucleotides();
        assertTrue("should return 'true'", Arrays.equals(expected, result));
    
        dnaTest.setDNA("aaaaccccttttgggg");
        expected = new int[] { 4, 4, 4, 4 };
        result = dnaTest.countNucleotides(); 
        assertTrue("Should return `True`", Arrays.equals(expected, result)); 

        dnaTest.setDNA("a");
        expected = new int[] { 1, 0, 0, 0 };
        result = dnaTest.countNucleotides(); 
        assertTrue("Should return `True`", Arrays.equals(expected, result));

        dnaTest.setDNA("");
        expected = new int[] { 0, 0, 0, 0 };
        result = dnaTest.countNucleotides(); 
        assertTrue("Should return `True`", Arrays.equals(expected, result));  

        dnaTest.setDNA("oepw");
        expected = new int[] { 0, 0, 0, 0 };
        result = dnaTest.countNucleotides(); 
        assertTrue("Should return `True`", Arrays.equals(expected, result));  
    }

    @Test public void testTranscribeToRNA() {
        DNA dnaTest = new DNA("actggg");
        String expected = "acuggg".toUpperCase();
        String result = dnaTest.transcribeToRNA(); 
        assertTrue("testTranscribeToRNA should be true", result.equals(expected));

        dnaTest.setDNA("tttt"); 
        expected = "UUUU"; 
        result = dnaTest.transcribeToRNA(); 
        assertTrue("testTranscribeToRNA should be true", result.equals(expected));    
    }

    @Test public void testComplementDNA() {
        DNA dnaTest = new DNA("actggg");
        String expected = "CCCAGT"; 
        String result = dnaTest.complementDNA(); 
        assertTrue("testTranscribeToRNA should be true", result.equals(expected));

        dnaTest.setDNA(""); 
        expected = ""; 
        result = dnaTest.complementDNA(); 
        assertTrue("testTranscribeToRNA should be true", result.equals(expected));    
    }

    @Test public void testPractice() {
        assertTrue("This practice test should pass", true); 
    }
}
