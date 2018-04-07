#include <stdio.h>

int main(void){
  int no;
  printf("なんか数字打ってください\n");
  scanf("%d", &no);
  switch (no){
    case 1:
    printf("お前は一位だよ");
    break;
    default:
    printf("はい神");
    break;
  }
}