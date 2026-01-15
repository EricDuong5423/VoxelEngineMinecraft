from numba import njit
from pyglm import glm
import numpy as np
import math

#Window resolution
WIN_RES = glm.vec2(1600, 900)

#Background colors
BG_COLOR = glm.vec3(0.1, 0.16, 0.25)