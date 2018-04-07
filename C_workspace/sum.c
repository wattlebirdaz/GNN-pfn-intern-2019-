#include <stdio.h>

int sum(void);
int ask(void);
int main(void){
  ask();
  sum();
  return 0;
}

int x,y;
int ask(void){
  printf("total sum of x to y.\nInput x,y\n");
  scanf("%d,%d",&x,&y);
}

int sum(void){
  printf("total sum between %d and %d is %d", x, y, (x+y) * (y-x+1) /2);
}