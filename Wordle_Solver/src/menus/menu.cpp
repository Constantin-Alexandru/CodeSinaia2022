#include "menu.h"

#include "utils.h"
#include <conio.h>

#define KEY_ENTER 13
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
  v2 pos = config.calculate_position(position);

  for (int i = 0; i < menus[current_menu].size(); i++)
  {
    MOVE_CURSOR_TO_POS(pos.height + i, pos.width);
    if (i == this->current_option)
    {
      SET_8_VALUE_COLOUR(TXT_MAGENTA);
      std::cout << "> ";
    }
    std::cout << menus[current_menu][i] << '\n';
    if (i == this->current_option)
    {
      SET_8_VALUE_COLOUR(TXT_WHITE);
    }
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
  case KEY_S:
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