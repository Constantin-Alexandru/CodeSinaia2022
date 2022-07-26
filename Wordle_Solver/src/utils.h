#pragma once

#include "typedefs.h"

template <typename T>
inline T wrap(T number, T lwr_bnd, T upp_bnd);
template <typename T>
inline T limitToRange(T number, T lwr_bnd, T upp_bnd);