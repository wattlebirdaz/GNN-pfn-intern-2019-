#include <stdio.h>
#include <string.h>

int main(void) {
  char set1[] = "today is";
  char set2[] = {" sunny"};
  strcat(set1, set2);
  printf("%s", set1);
}