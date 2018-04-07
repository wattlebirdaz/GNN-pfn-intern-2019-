#include <stdio.h>

int score(int);
int tensai(void);

int main(void){
  int num = score(tensai());
  if (num == 1 || num == 3){
    printf("no olympics\n");
  } else if (num == 0) {
    printf("summer olymipc");
  } else {
    printf("winter olympic");
  }
}

int tensai(void){
  int x;
  printf("西暦を入力してください\n");
  scanf("%d",&x);
  return x;
}

int score(int y){
  return (y % 4);
}