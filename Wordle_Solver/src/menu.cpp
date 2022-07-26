#include "menu.h"

#include "utils.h"
#include <conio.h>

#define KEY_ARR -32
#define KEY_UP 72
#define KEY_DOWN 80
#define KEY_LEFT 75
#define KEY_RIGHT 77
#define KEY_W 119
#define KEY_A 97
#define KEY_S 115
#define KEY_D 100

void Menu::show(Position position)
{
  v2 pos = v2();

  switch (current_menu)
  {
  case 0:
    pos = config.calculate_position(Position::CENTER, -3, -3);
    break;
  case 1:
    pos = config.calculate_position(Position::CENTER, -4, -1);
    break;
  case 2:
  case 3:
  case 4:
    pos = config.calculate_position(Position::BOTTOM_CENTER, -2);
    break;
  }

  for (int i = 0; i < menus[current_menu].size(); i++)
  {
    MOVE_CURSOR_TO_POS(pos.height + i, pos.width);
    std::cout << menus[current_menu][i] << '\n';
  }
}

void Menu::process_input(char key)
{
  if (key == KEY_ARR)
  {
    key = getch();
  }

  switch (key)
  {
  case KEY_W:
  case KEY_UP:
    this->current_option = wrap<int>(this->current_option - 1, 0, menus[current_menu].size());
    break;
  case KEY_D:
  case KEY_DOWN:
    this->current_option = wrap<int>(this->current_option + 1, 0, menus[current_menu].size());
    break;

  default:
    break;
  }

  return;
}

void Menu::help()
{
  return;
}

void Menu::about()
{
  return;
}