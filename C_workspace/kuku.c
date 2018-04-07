/*for文を使用して、掛け算九九の表を表示するプログラムを作成せよ。
ヒント：%2d指定子を使うと表を揃えられる。
ヒント：for文の中でfor文を使っても良い。*/

#include <stdio.h>

int main(void) {
  int i, d, product;
  for (i=1; i <= 9; i++) {
    for (d=1; d <= 9; d++) {
      product = i * d;
      printf("%02d\t", product);
    }
    printf("\n");
  }
}