#include <lcthw/bstrlib.h>
#include <lcthw/dbg.h>
#include <string.h>
#include <stronghold/count_nucleotides.h>

int *count_dna_nucleotides(char *dna)
{
	check(dna != NULL, "Invalid dna");

    char c;
    int i = 0;
	static int count[NUM_BASE_PAIRS]= {0, 0, 0, 0};

    while(dna[i] != '\0') {
        c = toupper(dna[i]);
        if(dna[i] == 'A') count[0]++;
        else if(dna[i] == 'C') count[1]++;
        else if(dna[i] == 'G') count[2]++;
        else if(dna[i] == 'T') count[3]++;
        i++;
    }

	return count;

error:
	return NULL;
}
