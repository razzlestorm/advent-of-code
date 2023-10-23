#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int score_line(char opp, char player);

void test_func(){
	int total = 0;
	total = score_line('A', 'Y');
	total += score_line('B', 'X');
	total += score_line('C', 'Z');
	printf("%d should equal 15", total);
}

int score_line(char opp, char player){
	int total = 0;
	switch (player) {
		case 'X':
			total += 1;
			break;
		case 'Y':
			total += 2;
			break;
		case 'Z':
			total += 3;
			break;
	}


	return total;

}

int main(){

	char line[8];
	FILE* ptr;
	ptr = fopen("2.txt", "r");
	if (ptr == NULL){
		printf("file can't be opened\n");
	}

	int total = 0;
	while (fgets(line, 8, ptr)){
		total += score_line(line[0], line[2]);
		
	}

	fclose(ptr);
}