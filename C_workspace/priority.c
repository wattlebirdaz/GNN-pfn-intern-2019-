#include <stdio.h>

int count;
int countfunc();
int main(void) {
  countfunc();
  int count = 20;
  countfunc();
  countfunc();
  printf("count %d\n", count);
}

int countfunc(void) {
  count++;
  printf("count %d\n", count);
  return 0;
}