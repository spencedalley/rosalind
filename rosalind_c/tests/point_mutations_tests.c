#include <stronghold/point_mutations.h>
#include <string.h>
#include <stdlib.h>
#include "minunit.h"

char *test_hamming_distance()
{
	char *s = "GAGCCTACTAACGGGAT";
	char *t = "CATCGTAATGACGGCCT";
	int expected_value = 7;

	mu_assert(hamming_distance(s, t) == expected_value, "Wrong value on hamming");
	mu_assert(hamming_distance(NULL, NULL) == -1, "Wrong value on NULL input");
	mu_assert(hamming_distance(NULL, t) == -1, "Wrong value on NULL input");
	mu_assert(hamming_distance(s, NULL) == -1, "Wrong value on NULL input");

	return NULL;
}

char *all_tests()
{
	mu_suite_start();

	mu_run_test(test_hamming_distance);

	return NULL;
}

RUN_TESTS(all_tests);
