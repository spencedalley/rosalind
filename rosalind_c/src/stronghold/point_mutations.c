#include <stdlib.h>
#include <string.h>
#include <stronghold/point_mutations.h>
#include <lcthw/dbg.h>

int hamming_distance(char *s, char *t)
{
	check(s != NULL, "'s' can't be NULL");
	check(t != NULL, "'t' can't be NULL");

	check(strlen(s) == strlen(t), "Lengths don't match");
	int i = 0;
	int diff = 0;

	for(i = 0; i < strlen(s); i++) {
		if(s[i] != t[i]) diff++;
	}

	return diff;

error:
	return -1;
}
