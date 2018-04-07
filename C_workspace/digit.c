#include <stdio.h>
#include <ctype.h>

int main(void){
  printf("判定したい文字数値を入力してください\n");
  char a;
  scanf("%c", &a);
  int suuti;
  if (isdigit(a)) {
    suuti = a - '0';
    printf("it is a digit %d\n", suuti);
  } else {
    printf("sorry it is not a digit\n");
  }
  
}