#ifndef _stronghold_dna_complement_h
#define _stronghold_dna_complement_h

char *complement_create(char *dna, int dna_len);
void complement_create_alt(char *dna, char *dna_complement, int dna_len);
void complement_destroy(char *complement);

#endif
