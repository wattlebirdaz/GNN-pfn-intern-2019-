#include <stdio.h>

int sum(int, int);
int main(void){
  int total;
  total = sum(50, 100);
  printf("50〜100の和は%d", total);
  return 0;
  
}
int sum(int x, int y){
  int num;
  num = (x + y) * (y - x + 1) /2;
  return num;
}