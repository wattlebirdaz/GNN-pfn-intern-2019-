/* 1本198円の清涼飲料水1本と、1本138円の牛乳2本を購入し、
千円札で払った場合のお釣りを求めよ。
ただし、5%の消費税を追加し、お釣りの額は整数とする。
なお、消費税を四捨五入するかどうかは自由とする。*/

#include <stdio.h>

int main(void)
{
  double price = (198 + 138 * 2)* 1.05;
  int change;
  change = 1000 - (int)price;
  printf("お釣りは%d円です", change);
  return 0;
}