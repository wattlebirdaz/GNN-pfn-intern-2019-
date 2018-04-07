#include <stdio.h>
#include <string.h>

int main(void) {
  char set0[20];
  char set1[] = "this is a pen and it is ";
  char set2[] = " yen";
  int tennis = 15;
  sprintf(set0, "%s%d%s",set1, tennis, set2);
  printf("%s", set0);
  return 0;
}