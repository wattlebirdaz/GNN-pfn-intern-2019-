#include <stdio.h>
#include <memory.h>

int array1[] = {1,2,3,4,5};
int array2[] = {6,7,8,9,10};
int array3[] = {11,22,33,44,55};

int main(void) {
  int i;
  printf("now array1 is\n");
  for (i=0; i < sizeof(array1)/sizeof(array1[0]); i++){
    printf("%d,",array1[i]);
  }
  printf("\nhowever, array1 is now\n");
  for (i=0; i< sizeof(array2)/sizeof(array2[0]); i++){
    array1[i] = array2[i];
    printf("%d,",array1[i]);
  }
  memcpy(array1, array3, sizeof(array3));
  printf("\narray1 has changed again and it is now...\n");
  for (i=0; i < sizeof(array1)/sizeof(array1[0]); i++){
    printf("%d,",array1[i]);
  }

}