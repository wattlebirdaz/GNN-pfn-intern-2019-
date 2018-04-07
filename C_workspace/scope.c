#include <stdio.h>

int main(void){
  int num1 = 30, num2 = 40;
  printf("%d, %d\n", num1, num2);
  {
    // 初期化したら新たな変数
    int num1;
    num1 = 10;
    num2 = 20;
    printf("%d, %d\n", num1, num2);
  }
  printf("%d, %d\n", num1, num2);
  return 0;
}