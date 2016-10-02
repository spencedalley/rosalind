#include "minunit.h"
#include <dlfcn.h>
#include "rosalind_c.h"

char *test_rosalind_c()
{
    return NULL;
}


char *all_tests()
{
    mu_suite_start();

    mu_run_test(test_rosalind_c);

    return NULL;
}

RUN_TESTS(all_tests);
