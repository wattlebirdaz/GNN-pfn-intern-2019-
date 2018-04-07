/*定価を入力すると、1割引、3割引、5割引、8割引の値段を、
一覧表示するプログラムを作成せよ。
なお、結果の金額は整数値での表示が望ましいが、実数でもかまわない。*/
#include <stdio.h>

int main(void)
{
  int price0, price1, price3, price5, price8;
  printf("定価を入力してください\n");
  scanf("%d", &price0);
  price1 = (int)(price0 * 0.9);
  price3 = (int)(price0 * 0.7);
  price5 = (int)(price0 * 0.5);
  price8 = (int)(price0 * 0.2);
  printf("一割引は%d\n三割引は%d\n五割引は%d\n八割引は%d\n", price1, price3, price5, price8);
  return 0;
}