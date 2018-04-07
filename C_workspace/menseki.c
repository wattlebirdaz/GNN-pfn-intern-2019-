#include <stdio.h>

int main(void){
  double r, area;
  do {
    printf("半径を教えてください\n");
    scanf("%lf", &r);
  } while (r < 0);
  area = r * r * 3.14;
  printf("半径%fの円の面積はおよそ%4.3fです", r, area);
  return 0;
}