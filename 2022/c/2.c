#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int score_line(char opp, char player);

int score_line_two(char opp, char player);

void test_func(){
	int total = 0;
	total = score_line('A', 'Y');
	total += score_line('B', 'X');
	total += score_line('C', 'Z');
	printf("%d should equal 15\n", total);
}

void test_func_two(){
	int total = 0;
	total = score_line_two('A', 'Y');
	total += score_line_two('B', 'X');
	total += score_line_two('C', 'Z');
	printf("%d should equal 12\n", total);
}
int score_line(char opp, char player){
	int total = 0;
	switch (player) {
		case 'X':
			total += 1;
			switch (opp){
				case 'A':
				total += 3;
				break;
			}
			switch (opp){
				case 'B':
				total += 0;
				break;
			}
			switch (opp){
				case 'C':
				total += 6;
				break;
			}
			break;
		case 'Y':
			total += 2;
			switch (opp){
				case 'A':
				total += 6;
				break;
			}
			switch (opp){
				case 'B':
				total += 3;
				break;
			}
			switch (opp){
				case 'C':
				total += 0;
				break;
			}
			break;
		case 'Z':
			total += 3;
			switch (opp){
				case 'A':
				total += 0;
				break;
			}
			switch (opp){
				case 'B':
				total += 6;
				break;
			}
			switch (opp){
				case 'C':
				total += 3;
				break;
			}
			break;
	}
	return total;
}


int score_line_two(char opp, char player){
	int total = 0;
	switch (player) {
		case 'X':
			switch (opp){
				case 'A':
				total += 3;
				break;
			}
			switch (opp){
				case 'B':
				total += 1;
				break;
			}
			switch (opp){
				case 'C':
				total += 2;
				break;
			}
			break;
		case 'Y':
			total += 3;
			switch (opp){
				case 'A':
				total += 1;
				break;
			}
			switch (opp){
				case 'B':
				total += 2;
				break;
			}
			switch (opp){
				case 'C':
				total += 3;
				break;
			}
			break;
		case 'Z':
			total += 6;
			switch (opp){
				case 'A':
				total += 2;
				break;
			}
			switch (opp){
				case 'B':
				total += 3;
				break;
			}
			switch (opp){
				case 'C':
				total += 1;
				break;
			}
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
		total += score_line_two(line[0], line[2]);
	}

	fclose(ptr);
	test_func_two();

	printf("%d", total);
	return 0;
}


#include <stdio.h>

#define AOCYEAR 2022
#define AOCDAY  2

enum round {
	WIN = 6,
	TIE = 3,
	LOSS = 0,
};

enum round outcome(int const a, int const b);
int choose_move(int const a, enum round const outcome);

// Move this here because it will be used by multiple functions
static const enum round outcomes[3][3] = {
	{TIE, LOSS, WIN},
	{WIN, TIE, LOSS},
	{LOSS, WIN, TIE},
};

int main(void)
{
	char a, b;
	int score1 = 0;
	int score2 = 0;

	while (2 == scanf(" %c %c", &a, &b)) {
		a = a - 'A';
		b = b - 'X';

		score1 += outcome(b, a) + (b + 1);
		score2 += (b * 3) + choose_move(a, b * 3);
	}

	printf("%4d-%02d/%d: %d\n", AOCYEAR, AOCDAY, 1, score1);
	printf("%4d-%02d/%d: %d\n", AOCYEAR, AOCDAY, 2, score2);
}

enum round outcome(int const a, int const b)
{
	return outcomes[a][b];
}

int choose_move(int const a, enum round const outcome)
{
	int i;
	for (i = 0; i < 3; ++i) {
		// 6 - outcome "inverts" the outcome
		if (outcomes[a][i] == (6 - outcome)) {
			break;
		}
	}
	return i + 1;
}
