#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <eu/p28.h> 

int diagonal(int n)
{
	if(n <= 9) n = 1001;

	int t = 0,
		r = 1,
		j = 2,
		i = 3;

	for(i = 3; i < n+1; i+=2) {
		t = i * i;
		t = pow(i, 2);
		r += (t + (t-j) + (t-j*2) + (t-j*3));
		j += 2;
	}

	return r;
}
