/*これ自体は、今までやってきたことで簡単に実現出来ますが、
今回は更に、100点より大きい点数を間違えて入力した場合、
自動的に100点に修正して記憶するという機能をつけてみます。*/

#include <stdio.h>

int main(void)
{
  int grade;
  printf("テストの得点を入力してください\n");
  scanf("%d", &grade);
  if (grade > 100)
  {
    printf("１００点を超えているので修正しました\n");
    grade = 100;
  }
  printf("得点は%dでした", grade);
  return 0;
}