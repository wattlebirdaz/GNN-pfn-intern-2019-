#include <stdio.h>

int main(void)
{
  int value;
  value = 10;
  printf("最初は%dだよ\n", value);
  value++;
  printf("一増やしてみたら%dになった\n", value);
  value--;
  printf("一減らしてみたら%dで,元に戻った\n", value);
  return 0;
}