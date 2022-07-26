#pragma once

#include "typedefs.h"

template <typename T>
inline T wrap(T number, T lwr_bnd, T upp_bnd)
{
  T range = upp_bnd - lwr_bnd;

  if (number < lwr_bnd)
    number += range * ((lwr_bnd - number) / range + 1);

  return lwr_bnd + (number - lwr_bnd) % range;
}

template <typename T>
inline T limitToRange(T number, T lwr_bnd, T upp_bnd)
{
  return number < lwr_bnd ? lwr_bnd : number > upp_bnd ? upp_bnd
                                                       : number;
}