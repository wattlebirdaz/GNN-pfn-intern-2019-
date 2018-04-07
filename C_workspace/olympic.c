/*西暦年を入力すると、その年にオリンピックが開かれるか、
表示するプログラムを作成せよ。
可能なら、夏季と冬季の区別も表示できればなお良い。
ヒント:シドニー五輪(夏)は2000年開催であった。
※条件がややこしくなるので、
　以前夏季と冬季が同じ年だった時期のことは無視する。*/

#include <stdio.h>

int main(void)
{
  int year, score;
  printf("西暦を入力してください\n");
  scanf("%d", &year);
  if (year >= 2000) score = (year - 2000) % 4;
  if (year < 2000) score = (2000 - year) % 4;
  if (score == 1 || score == 3) printf("%d年にはオリンピックはありませんでした\n", year);
  if (score == 2) printf("%d年には冬季オリンピックがありました\n", year);
  if (score == 0) printf("%d年には夏季オリンピックがありました\n", year);
  return 0; 
}