#include <stdio.h>

int sum(int,int);

int main(void) {
  sum(50, 100);
  return 0;
}

int sum(int x, int y) {
  printf("%dから%dまでの和は、%dです", x, y, (x+y) * (y-x) /2);
  return 0;
}