#include <math.h>
#include <stronghold/gc_content.h>
#include <string.h>
#include <stdlib.h>
#include "minunit.h"

char *test_gc_content()
{
    char *dna = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT";
    int dna_len = strlen(dna);

    double gc_levels_fail = compute_gc_content(dna, 0);
    double gc_levels = compute_gc_content(dna, dna_len);
    // (count of GC / total) * 100
    double expected_value = ((double)53 / (double)87) * 100;

    mu_assert(gc_levels_fail == -1.0, "Wrong value on fail")
    mu_assert(gc_levels == expected_value, "Wrong GC content");

    return NULL;
}

char *all_tests()
{
    mu_suite_start();

    mu_run_test(test_gc_content);

    return NULL;
}

RUN_TESTS(all_tests);
