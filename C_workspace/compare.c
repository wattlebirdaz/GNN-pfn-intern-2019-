#include <stdio.h>
#include <string.h>

int main(void) {
  char set1[] = "DRAGONQUEST";
  char set2[256];
  printf("set1と同じ文字列を入力してください");
  scanf("%s", set2);
  if (strcmp(set1, set2) == 0){
    printf("right!");
  } else {
    printf("wrong!");
  }
  return 0;
}