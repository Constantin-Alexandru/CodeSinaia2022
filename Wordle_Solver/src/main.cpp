#include <iostream>
#include <fstream>
#include "../ANSI-Library/ansi_lib.h"
#include "menu.h"
#include <Windows.h>

int main(int argc, char *argv[])
{
  setupConsole();

  Menu menu = Menu(v2(50, 50));

  ERASE_SCREEN;
  menu.show(Position::CENTER);

  Sleep(5000);
  Sleep(5000);
  Sleep(5000);
  Sleep(5000);

  resetConsole();
}