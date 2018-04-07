//簡易シグマ計算
#include <stdio.h>

int main(void)
{
  int min, max, sum;
  printf("最小値と最大値をスペースで区切って入力してください\n");
  scanf("%d%d", &min, &max);
  sum = (min + max) * (max - min + 1) / 2;
  printf("%dから%dまでの合計は%dである", min, max, sum);
  return 0;
}