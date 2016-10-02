#include <lcthw/bstrlib.h>
#include <stronghold/count_nucleotides.h>
#include "minunit.h"

char *test_count_dna_nucleotides()
{
	char *dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC";
	int *count = count_dna_nucleotides(dna);

	mu_assert(count[0] == 20, "Incorrect number of A's counted.");
	mu_assert(count[1] == 12, "Incorrect number of C's counted.");
	mu_assert(count[2] == 17, "Incorrect number of G's counted");
	mu_assert(count[3] == 21, "Incorrect number of T's counted");

    count = count_dna_nucleotides(NULL);
    mu_assert(count == NULL, "Wrong value on NULL");

	return NULL;
}

char *all_tests()
{
	mu_suite_start();

	mu_run_test(test_count_dna_nucleotides);

	return NULL;
}

RUN_TESTS(all_tests);
