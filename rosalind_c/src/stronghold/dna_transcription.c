#include <lcthw/dbg.h> 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stronghold/dna_transcription.h>


void rna_create2(char *dna, char *rna, int dna_len)
{
	check(dna != NULL, "DNA is NULL");
	check(dna_len > 0, "Can't have a 0 length dna strand.");

	int i = 0;

	for(i = 0; i < dna_len; i++) {
		if(toupper(dna[i]) == 'T') rna[i] = 'U';
		else rna[i] = toupper(dna[i]);
	}

error:
	return;
}

char *rna_create(char *dna, int dna_len)
{
	check(dna != NULL, "DNA is NULL");
	check(dna_len > 0, "Can't have a 0 length dna strand.");

	int i = 0;
	char *rna = malloc(dna_len + 1);

	for(i = 0; i < dna_len; i++) {
		if(toupper(dna[i]) == 'T') rna[i] = 'U';
		else rna[i] = toupper(dna[i]);
	}

	return rna;

error:
	return NULL;
}

void rna_destroy(char *rna)
{
	if(rna != NULL) free(rna);
}
