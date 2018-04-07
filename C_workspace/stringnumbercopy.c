#include <stdio.h>
#include <string.h>

int main(void){
  char tennis[] = "tennis", soccer[10];
  strncpy(soccer, tennis, 4);
  printf("%s", soccer);
}