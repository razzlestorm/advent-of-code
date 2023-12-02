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
	int len = strlen(s);
	int first = 999;
	int last = 0;
	for (int i; i < len; i++){
		printf("%c", s[i]);
		if isdigit(s[i]){
			if (first == 999){
				first = ((int)(s[i]) - '0') * 10;
			}
			last = (int)(s[i] - '0');
		}
		printf("first is %d and last is %d\n", first, last);
	}
	int total = first + last;
	return total;
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
		return 1;
	}

	int total = 0;
	while (fgets(stringBuf, 128, ptr)){
		int sum = sum_numbers_in_string(stringBuf);
		total += sum;
	//	printf("answer for %s is %d\n", stringBuf, sum);
	}

	fclose(ptr);
	printf("total sum is %d\n", total);
	return 0; 
}
