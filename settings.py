from numba import njit
from pyglm import glm
import numpy as np
import math

#Window resolution
WIN_RES = glm.vec2(1600, 900)

#Chunk size
CHUNK_SIZE = 32
H_CHUNK_SIZE = CHUNK_SIZE // 2
CHUNK_AREA = CHUNK_SIZE * CHUNK_SIZE
CHUNK_VOL = CHUNK_AREA * CHUNK_SIZE

#World size
WORLD_W , WORLD_H = 10, 3
WORLD_D = WORLD_W
WORLD_AREA = WORLD_W * WORLD_D
WORLD_VOL = WORLD_AREA * WORLD_H

#World center
CENTER_XZ = WORLD_W * H_CHUNK_SIZE
CENTER_Y = WORLD_H * H_CHUNK_SIZE

#Camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG) # verical POV
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO) # horizontal POV
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89)

#Player
PLAYER_SPEED = 0.005
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(CENTER_XZ, WORLD_H * CHUNK_SIZE , CENTER_XZ)
MOUSE_SENSITIVITY = 0.002

#Background colors
BG_COLOR = glm.vec3(0.1, 0.16, 0.25)