#include "utils.h"

template <typename T>
inline T wrap(T number, T lwr_bnd, T upp_bnd)
{
  return lwr_bnd + number % upp_bnd;
}

template <typename T>
inline T limitToRange(T number, T lwr_bnd, T upp_bnd)
{
  return number < lwr_bnd ? lwr_bnd : number > upp_bnd ? upp_bnd
                                                       : number;
}