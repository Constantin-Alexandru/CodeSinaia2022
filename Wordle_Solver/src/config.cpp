#include "config.h"

v2 Config::calculate_position(Position position, int x_off, int y_off)
{
  switch (position)
  {
  case Position::TOP_LEFT:
    return v2(x_off, y_off);
  case Position::TOP_CENTER:
    return v2(size.width / 2 + x_off, y_off);
  case Position::TOP_RIGHT:
    return v2(size.width + x_off, y_off);
  case Position::CENTER_LEFT:
    return v2(x_off, size.height / 2 + y_off);
  case Position::CENTER:
    return v2(size.width / 2 + x_off, size.height / 2 + y_off);
  case Position::CENTER_RIGHT:
    return v2(size.width / 2 + x_off, size.height / 2 + y_off);
  case Position::BOTTOM_LEFT:
    return v2(x_off, size.height / 2 + y_off);
  case Position::BOTTOM_CENTER:
    return v2(size.width / 2 + x_off, size.height / 2 + y_off);
  case Position::BOTTOM_RIGHT:
    return v2(size.width + x_off, size.height + y_off);
  default:
    return v2(0, 0);
  }
}