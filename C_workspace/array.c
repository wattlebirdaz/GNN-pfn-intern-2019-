#include <stdio.h>

int array[100];

int main(void){
  int i;
  array[0] = 1;
  array[1] = 2;
  printf("%d\n%d\n", array[0], array[1]);
  for (i=2; i<=20; i++){
    array[i] = array[i-1] + array[i-2];
    printf("array[%d] is %d\n", i, array[i]);
  }
}