from OpenGL.GL import *


class Cube:
    __colors = []
    __dimensionals = []
    __lines = []

    def setColors(self, c1, c2, c3, c4, c5, c6):
        self.__colors = [c1, c2, c3, c4, c5, c6]

    def setColor(self, c1):
        self.__colors = [c1, c1, c1, c1, c1, c1]

    def setDimensional(self, v1, v2, v3, v4, v5, v6):
        self.__dimensionals = [v1, v2, v3, v4, v5, v6]

    def setLines(self, v1, v2, v3, v4, v5, v6):
        self.__lines = [v1, v2, v3, v4, v5, v6]

    def draw(self, iOffset=0.0, jOffset=0.0):
        e1 = 0
        e2 = 0
        e3 = 0
        glBegin(GL_QUADS)
        for i in range(0, 6, 1):
            color = self.__colors[i]
            dimensional = self.__dimensionals[i]
            d1 = dimensional[0]
            d2 = dimensional[1]
            d3 = dimensional[2]
            d4 = dimensional[3]

            glColor3f(color[0], color[1], color[2])
            glVertex3f(d1[0] + iOffset - e1, d1[1] + jOffset - e2, d1[2] - e3)
            glVertex3f(d2[0] + iOffset - e1, d2[1] + jOffset - e2, d2[2] - e3)
            glVertex3f(d3[0] + iOffset - e1, d3[1] + jOffset - e2, d3[2] - e3)
            glVertex3f(d4[0] + iOffset - e1, d4[1] + jOffset - e2, d4[2] - e3)
        glEnd()

        glBegin(GL_LINES)
        for i in range(0, 6, 1):
            dimensional = self.__lines[i]
            d1 = dimensional[0]
            d2 = dimensional[1]
            d3 = dimensional[2]
            d4 = dimensional[3]

            glColor3f(0, 0, 0)
            glVertex3f(d1[0] + iOffset - e1, d1[1] + jOffset - e2, d1[2] - e3)
            glVertex3f(d2[0] + iOffset - e1, d2[1] + jOffset - e2, d2[2] - e3)
            glVertex3f(d2[0] + iOffset - e1, d2[1] + jOffset - e2, d2[2] - e3)
            glVertex3f(d3[0] + iOffset - e1, d3[1] + jOffset - e2, d3[2] - e3)
            glVertex3f(d3[0] + iOffset - e1, d3[1] + jOffset - e2, d3[2] - e3)
            glVertex3f(d4[0] + iOffset - e1, d4[1] + jOffset - e2, d4[2] - e3)
            glVertex3f(d4[0] + iOffset - e1, d4[1] + jOffset - e2, d4[2] - e3)
            glVertex3f(d1[0] + iOffset - e1, d1[1] + jOffset - e2, d1[2] - e3)
        glEnd()


def getCube(array, color):
    cube = Cube()
    x = array[0]
    y = array[1]
    z = array[2]
    d1 = [
        [x - 1, y + 1, z + 1],
        [x - 1, y + 1, z - 1],
        [x - 1, y - 1, z - 1],
        [x - 1, y - 1, z + 1],
    ]
    d2 = [
        [x + 1, y + 1, z + 1],
        [x + 1, y + 1, z - 1],
        [x + 1, y - 1, z - 1],
        [x + 1, y - 1, z + 1],
    ]
    d3 = [
        [x + 1, y - 1, z + 1],
        [x + 1, y - 1, z - 1],
        [x - 1, y - 1, z - 1],
        [x - 1, y - 1, z + 1],
    ]
    d4 = [
        [x + 1, y + 1, z + 1],
        [x + 1, y + 1, z - 1],
        [x - 1, y + 1, z - 1],
        [x - 1, y + 1, z + 1],
    ]
    d5 = [
        [x + 1, y + 1, z - 1],
        [x + 1, y - 1, z - 1],
        [x - 1, y - 1, z - 1],
        [x - 1, y + 1, z - 1],
    ]
    d6 = [
        [x + 1, y + 1, z + 1],
        [x + 1, y - 1, z + 1],
        [x - 1, y - 1, z + 1],
        [x - 1, y + 1, z + 1],
    ]
    cube.setColor(color)
    cube.setDimensional(d1, d2, d3, d4, d5, d6)
    d1 = [
        [x - 1.01, y + 1.01, z + 1.01],
        [x - 1.01, y + 1.01, z - 1.01],
        [x - 1.01, y - 1.01, z - 1.01],
        [x - 1.01, y - 1.01, z + 1.01],
    ]
    d2 = [
        [x + 1.01, y + 1.01, z + 1.01],
        [x + 1.01, y + 1.01, z - 1.01],
        [x + 1.01, y - 1.01, z - 1.01],
        [x + 1.01, y - 1.01, z + 1.01],
    ]
    d3 = [
        [x + 1.01, y - 1.01, z + 1.01],
        [x + 1.01, y - 1.01, z - 1.01],
        [x - 1.01, y - 1.01, z - 1.01],
        [x - 1.01, y - 1.01, z + 1.01],
    ]
    d4 = [
        [x + 1.01, y + 1.01, z + 1.01],
        [x + 1.01, y + 1.01, z - 1.01],
        [x - 1.01, y + 1.01, z - 1.01],
        [x - 1.01, y + 1.01, z + 1.01],
    ]
    d5 = [
        [x + 1.01, y + 1.01, z - 1.01],
        [x + 1.01, y - 1.01, z - 1.01],
        [x - 1.01, y - 1.01, z - 1.01],
        [x - 1.01, y + 1.01, z - 1.01],
    ]
    d6 = [
        [x + 1.01, y + 1.01, z + 1.01],
        [x + 1.01, y - 1.01, z + 1.01],
        [x - 1.01, y - 1.01, z + 1.01],
        [x - 1.01, y + 1.01, z + 1.01],
    ]
    cube.setLines(d1, d2, d3, d4, d5, d6)
    return cube
