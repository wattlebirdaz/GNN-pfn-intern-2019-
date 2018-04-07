/*テストの点数を入力するプログラムを作りたい。
ただし、テストの点数は0～100までしかないので、
それ以外が入力された場合には再入力させるようにすること。*/

#include <stdio.h>

int main(void){
  double score;
  do {
    printf("input test score\n");
    scanf("%lf", &score);
  } while (score < 0 || score > 100);
  printf("the score is %3.2f", score);
}