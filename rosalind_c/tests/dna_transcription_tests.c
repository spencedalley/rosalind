#include <stronghold/dna_transcription.h>
#include <string.h>
#include "minunit.h"

char *test_rna_create()
{
    char *dna = "GATGGAACTTGACTACGTAAATT";
    int dna_len = sizeof(char) * strlen(dna);
    char *rna;
    rna  = rna_create(dna, dna_len);

    debug("RNA is '%s'", rna);
    //mu_assert(rna == "GAUGGAACUUGACUACGUAAAUU", "Got wrong value on transcription");

    rna_destroy(rna);

    return NULL;
}

char *test_rna_create2()
{
    char *dna = "GATGGAACTTGACTACGTAAATT";
    int dna_len = sizeof(char) * strlen(dna);
    char *rna;

    rna_create2(dna, rna, dna_len);

    debug("RNA is '%s'", rna);
    debug("RNA is '%s'", "GAUGGAACUUGACUACGUAAAUU");
    mu_assert(rna == "GAUGGAACUUGACUACGUAAAUU", "Got wrong value on transcription");

    return NULL;
}


char *all_tests()
{
    mu_suite_start();

    mu_run_test(test_rna_create);

    return NULL;
}

RUN_TESTS(all_tests);
