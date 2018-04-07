#include <stdio.h>

int countf();
int main(void){
  countf();
  countf();
  int i;
  for (i=1; i<=100; i++){
    countf();
  }
}

int countf(void){
  static int count = 0;
  count++;
  printf("%d\n", count);
  return 0;
}
