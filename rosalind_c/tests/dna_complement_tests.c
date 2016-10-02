#include <stronghold/dna_complement.h>
#include <string.h>
#include "minunit.h"

char *test_complement_create()
{
    char *dna = "AAAACCCGGT";
    int dna_len = strlen(dna);
    char *complement = complement_create(dna, dna_len);

    debug("Complement is '%s'", complement);

    //mu_assert(complement == "ACCGGGTTTT", "Wrong complement created");

    return NULL;
}

char *test_complement_create_alt()
{
    char *dna = "AAAACCCGGT";
    int dna_len = sizeof(char) * strlen(dna);
    char *complement;

    complement_create_alt(dna, complement, dna_len);

    debug("Complement is '%s'", complement);

    mu_assert(complement == "ACCGGGTTTT", "Wrong complement created");

    return NULL;
}

char *all_tests()
{
    mu_suite_start();

    mu_run_test(test_complement_create);

    return NULL;
}

RUN_TESTS(all_tests);
