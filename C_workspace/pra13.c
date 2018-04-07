#include <stdio.h>

int array[] = {1,2,3,4,5,6,7,8,9,10};

int main(void){
  int i;
  for (i=0; i < sizeof(array)/sizeof(array[0]); i++) {
    printf("array[%d] = %d\n", 9-i, array[9-i]);
  }
}