#include <stdio.h>

int main(void){
  int money, month = 1;
  printf("初めの月のお小遣いを教えてください\n");
  scanf("%10d", &money);
  while (money<100000) {
    printf("%2d月目は%d円\n", month, money);
    money *= 2;
    month++;
  }
  printf("お小遣いは%2d月目に、%dとなり,10万円超えました。", month, money);
  return 0;
}