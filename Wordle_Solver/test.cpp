#include <stdio.h>
#include <conio.h>

int main(int argc, char const *argv[])
{
  char c = getch();

  while (c != 13)
  {
    c = getch();

    printf("%d\n", c);
  }

  return 0;
}
