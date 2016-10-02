#include <lcthw/dbg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stronghold/gc_content.h>


double compute_gc_content(char *dna, int dna_len)
{
    check(dna != NULL, "DNA is NULL");
    check(dna_len > 0, "Can't have 0 length dna strand.");

    int i = 0;
	int count = 0;

	for(i = 0; i < dna_len; i++) {
		if(toupper(dna[i]) == 'C' || toupper(dna[i] == 'G')) {
			count += 1;
		}
	}

    double result = ((double)count / (double)dna_len) * 100;

	return result;

error:
    return -1.0;
}
