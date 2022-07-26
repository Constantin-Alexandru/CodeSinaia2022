#pragma once

enum class Position
{
  ERR_POS = 0,
  TOP_LEFT = 1,
  TOP_CENTER = 2,
  TOP_RIGHT = 3,
  CENTER_LEFT = 4,
  CENTER = 5,
  CENTER_RIGHT = 6,
  BOTTOM_LEFT = 7,
  BOTTOM_CENTER = 8,
  BOTTOM_RIGHT = 9
};

struct v2
{
  v2(int w = 0, int h = 0) : width(w), height(h){};
  int width;
  int height;
};

struct Config
{
  Config(v2 size) : size(size){};

  v2 size;

  v2 calculate_position(Position position, int x_off = 0, int y_off = 0);
};
