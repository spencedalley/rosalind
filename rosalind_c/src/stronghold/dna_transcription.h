#ifndef _stronghold_dna_transcription_h
#define _stronghold_dna_transcription_h

char *rna_create(char *dna, int dna_len);
void rna_destroy(char *rna);

void rna_create2(char *dna, char *rna, int dna_len);

#endif
