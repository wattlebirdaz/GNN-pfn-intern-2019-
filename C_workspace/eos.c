#include <stdio.h>

int main(void){
  char set1[] = {'t', 'e', 'n', 's', 'a', 'i', '\0'};
  char set2[] = {'c', 'o', 'f', 'f', 'e', 'e'};
  char set3[6] = {'c', 'o', 'f', 'f', 'e', 'e'};
  printf("%s, %s, %s", set1, set2, set3);
}

