#include <lcthw/dbg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stronghold/dna_complement.h>


char *complement_create(char *dna, int dna_len)
{
	check(dna != NULL, "DNA is NULL");
	check(dna_len > 0, "Can't have a 0 length dna strand.");

	int i = 0;
	char *complement = malloc(sizeof(char) * dna_len);

	for(i = 0; i < dna_len; i++) {
		switch(toupper(dna[i])) {
			case 'A':
				complement[dna_len-i-1] = 'T';
				break;

			case 'C':
				complement[dna_len-i-1] = 'G';
				break;

			case 'G':
				complement[dna_len-i-1] = 'C';
				break;

			case 'T':
				complement[dna_len-i-1] = 'A';
				break;

			default:
				complement[dna_len-i-1] = dna[i];
				break;
		}
	}

	return complement;

error:
	return NULL;
}

void complement_create_alt(char *dna, char *dna_complement, int dna_len)
{
	check(dna != NULL, "DNA is NULL");
	check(dna_len > 0, "Can't have a 0 length dna strand.");
	check(dna_len == (sizeof(char) * strlen(dna)), "Given dna_len and computed length don't match");

	int i = 0;

	for(i = 0; i < dna_len; i++) {
		switch(toupper(dna[i])) {
			case 'A':
				dna_complement[dna_len-i-1] = 'T';
				break;

			case 'C':
				dna_complement[dna_len-i-1] = 'G';
				break;

			case 'G':
				dna_complement[dna_len-i-1] = 'C';
				break;

			case 'T':
				dna_complement[dna_len-i-1] = 'A';
				break;

			default:
				dna_complement[dna_len-i-1] = dna[i];
				break;
		}
	}

error:
    return;
}

void complement_destroy(char *complement)
{
	if(complement != NULL) free(complement);
}

// int main(void)
// {
// 	char *dna = "AAAACCCGGT";
// 	int dna_len = sizeof(char) * strlen(dna);
// 	char *dna_complement = complement_create(dna, dna_len);
//
// 	printf("DNA complement: %s\n", dna_complement);
// 	printf("DNA Original  : %s\n", dna);
//
// 	complement_destroy(dna_complement);
// }
