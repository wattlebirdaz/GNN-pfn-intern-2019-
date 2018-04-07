#include <stdio.h>


int main(void)
{
	int i;
	
	char str[256];
	scanf("%s",str);
	
	for (i = 0;str[i] != '\0';i++) {
    printf("%d", i);
  }
	
	return 0;
}
//appと入れると結果は012である

int main(void)
{
	int i;
	
	char str[256];
	scanf("%s",str);
	
	for (i = 0;str[i] != '\0';i++);
  printf("%d", i);

	
	return 0;
}
//appと入れると結果は2である