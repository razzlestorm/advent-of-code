#include <stdlib.h>
#include <stdio.h>

int main(){

	char stringBuf[64];
	long max[3] = {0, 0, 0};
	long sum = 0;
	FILE* ptr;
	ptr = fopen("1.txt", "r");
	if (ptr == NULL){
		printf("file can't be opened\n");
	}

	while (fgets(stringBuf, 64, ptr)){
		if (stringBuf[0] == '\n'){
			for (int i = 2; i >=0; i--){
				if (sum >= max[i]){
					long tmp = max[i];
					max[i] = sum;
					sum = tmp;
				}
			}
			sum = 0;
		}
		sum += strtol(stringBuf, NULL, 10);
	}

	fclose(ptr);
	printf("Top three are: %d, %d, %d\n", max[2], max[1], max[0]);
	printf("Their sum is: %d\n", max[0]+max[1]+max[2]);
	return 0; 
}
