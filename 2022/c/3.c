#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char find_shared_char(char* s);
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
		char c = find_shared_char(s1[i]);
		int plus = get_priority(c);
		total += plus;
		printf("total for %d is %d\n", i, plus);
	}
	printf("test total is %d\n", total);
	
}

char find_shared_char(char* s){
	int len = strlen(s);
	int left, right;
	for(left = 0; left < len / 2; left++){
		for (right = len / 2; right < len; right++){
			if (s[left] == s[right]){
				return s[left];
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
		c = find_shared_char(line);
		total += get_priority(c);
	}

	fclose(ptr);
	printf("The total for part 1 is %d\n", total);

	test_func();
	return 0;
}
