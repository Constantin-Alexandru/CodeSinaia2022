#pragma once
#include "../ANSI-Library/ansi_lib.h"
#include "config.h"
#include <vector>
#include <string>
#include <iostream>

class Menu
{
public:
  Menu(Config config) : config(config) {}

  void show(Position position);
  void process_input(char key);

private:
  void help();
  void about();

private:
  int current_option = 0;
  int current_menu = 0;

  Config config;

  std::vector<std::vector<std::string>> menus = {
      {"Start Game", "Configure", "Statistics", "About", "Credits", "Exit"},
      {"Add Word", "Remove Word", "Back"},
      {"Back"},
      {"Back"},
      {"Back"}};
};