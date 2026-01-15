from unittest import skip

import numpy as np

class BaseMesh:
    def __init__(self):
        #OpenGL context
        self.ctx = None
        #shader_program
        self.program = None
        #vertex buffer data type format: "3f 3f"
        self.vbo_format = None
        #attribute names according to the format: ("in_position", "in_color")
        self.attrs: tuple[str, ...] = None
        #vertex array object

    def get_vertex_data(self): np.array: ...

    def get_vao(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        vao = self.ctx.vertex_arrays(
            self.program, [(vbo, self.vbo_format, *self.attrs)] , skip_erros=True
        )
        return vao