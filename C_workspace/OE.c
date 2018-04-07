/*偶奇を判断するプログラム*/

#include <stdio.h>

int main(void)
{
  int number, score;
  printf("数値を入力してください\n");
  scanf("%d", &number);
  score = number % 2;
  if (score == 0) printf("%dは偶数です", number);
  if (score == 1) printf("%dは奇数です", number);
  return 0;
}