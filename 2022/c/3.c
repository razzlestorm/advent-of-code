#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int get_shared_char_priority(char* s);
int get_priority(char c);

void test_func(){
	char* s1[] = {
		"vJrwpWtwJgWrhcsFMMfFFhFp",
		"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
		"PmmdzqPrVvPwwTWBwg",
		"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
		"ttgJtRGJQctTZtZT",
		"CrZsJsPPZsGzwwsLwLmpwMDw"
	};
	int total = 0;
	for(int i = 0; i < 6; i++){
		int p = get_shared_char_priority(s1[i]);
		total += p;
		printf("total for %d is %d\n", i, p);
	}
	printf("test total is %d\n", total);
	
}

int get_shared_char_priority(char* s){
	int len = strlen(s);
	int i;
	int seen[64] = {0};
	for(i = 0; i < len; i++){
		int p = get_priority(s[i]);
		if (i < len/2){
			seen[p] = 1; 
		}
		else {
			if (seen[p]){
				return p;
			}
		}	
	}
	printf("NO CHARACTER FOUND");
	return '\0';
}

int get_priority(char c){

	if(c>= 'a' && c <= 'z'){
		return (c - 'a') + 1;
	}

	else if(c >= 'A' && c <= 'Z'){
		return 27 + (c - 'A');
	}
	else {
		return 0;
	}
}

int main(){

	char line[64];
	FILE* ptr;
	ptr = fopen("3.txt", "r");
	if (ptr == NULL){
		printf("file can't be opened\n");
	}

	int total = 0;
	char c;
	while (fgets(line, 64, ptr)){
		int p = get_shared_char_priority(line);
		total += p;
	}

	fclose(ptr);
	printf("The total for part 1 is %d\n", total);

	test_func();
	return 0;
}
