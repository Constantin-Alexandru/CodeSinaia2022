#include <iostream>
#include <fstream>
#include "../ANSI-Library/ansi_lib.h"
#include "menu.h"
#include <Windows.h>
#include <conio.h>

int main(int argc, char *argv[])
{
  setupConsole();

  Menu menu = Menu(v2(50, 50));

  char c;

  while (true)
  {
    ERASE_SCREEN;
    menu.show(Position::CENTER);
    c = getch();
    menu.process_input(c);

    if (c == 27)
      exit(0);
  }

  resetConsole();
}