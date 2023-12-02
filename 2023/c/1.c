#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>


int sum_numbers_in_string(char *s);

void test_func(char* s[], int len) {
	int total = 0;
	for (int i = 0; i < len; i++){
		int sum = sum_numbers_in_string(s[i]);
		total += sum;
		printf("number for row %d is %d\n", i, sum);
	}
	printf("test total is %d\n", total);
}

int sum_numbers_in_string(char* s){
	int left = 0;
	int right = strlen(s);
	char strnum[2];
	int filled = 0;
	while (filled < 2){
		if (isdigit(s[left])){
			strnum[0] = s[left];
			filled++;
		}
		if (isdigit(s[right])){
			strnum[1] = s[right];
			filled++;
		}
		left++;
		right--;
	}
	return atoi(strnum);
}

int main(){
	char* t1[] = {
		"1abc2",
		"pqr3stu8vwx",
		"a1b2c3d4e5f",
		"treb7uchet",
	};
	int size1 = sizeof(t1)/sizeof(t1[0]);
	char* t2[] = {
		"6mxgxnjb",
		"threeseven4",
		"treb7uchet",
	};
	int size2 = sizeof(t2)/sizeof(t2[0]);
	test_func(t1, size1);
	test_func(t2, size2);
	char stringBuf[128];
	FILE* ptr;
	ptr = fopen("1.txt", "r");
	if (ptr == NULL){
		printf("file can't be opened\n");
	}

	int total = 0;
	while (fgets(stringBuf, 128, ptr)){
		int sum = sum_numbers_in_string(stringBuf);
		total += sum;
		printf("answer for %s is %d\n", stringBuf, sum);
	}

	fclose(ptr);
	printf("total sum is %d\n", total);
	return 0; 
}
