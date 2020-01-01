from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import cube as cube_file
import map as map_file

ESCAPE = b'\x1b'
ARROW_LEFT = 100
ARROW_UP = 101
ARROW_RIGHT = 102
ARROW_DOWN = 103

window = 0

# rotation
X_AXIS = -45.0
Y_AXIS = 0.0
Z_AXIS = -45

DIRECTION = 1

gameMap = map_file.Map()
groundMapCenters = []
groundMapCubes = []
player = []
playerCube = cube_file.Cube
goal = []
goalCube = cube_file.Cube
blocksCenter = []
blocksCubes = []


def keyPressed(*args):
    global player
    if winGame():
        return
    if args[0] == ESCAPE:
        sys.exit()
    if args[0] == ARROW_LEFT:
        if checkMove([player[0], player[1] - 2, player[2]]):
            player[1] -= 2
    if args[0] == ARROW_UP:
        if checkMove([player[0] - 2, player[1], player[2]]):
            player[0] -= 2
    if args[0] == ARROW_RIGHT:
        if checkMove([player[0], player[1] + 2, player[2]]):
            player[1] += 2
    if args[0] == ARROW_DOWN:
        if checkMove([player[0] + 2, player[1], player[2]]):
            player[0] += 2
    if winGame():
        print("YOU WIN!!!")


def checkMove(newPose):
    if newPose[0] < 0 or newPose[0] > 15 or newPose[1] < 0 or newPose[1] > 15:
        return False
    if newPose in blocksCenter:
        return False
    return True


def winGame():
    if player[0] == goal[0] and player[1] == goal[1]:
        return True
    return False


def DrawGLScene():
    global X_AXIS, Y_AXIS, Z_AXIS
    global DIRECTION

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslatef(-11, -0.0, -30.0)

    glRotatef(X_AXIS, 1.0, 0.0, 0.0)
    glRotatef(Y_AXIS, 0.0, 1.0, 0.0)
    glRotatef(Z_AXIS, 0.0, 0.0, 1.0)

    generateCubes()
    drawGoal()
    drawGround()
    drawPlayer()
    drawBlocks()

    glutSwapBuffers()


def drawGround():
    global groundMapCubes
    for i in range(len(groundMapCubes)):
        cubes = groundMapCubes[i]
        i_offset = i * 0.01
        for j in range(len(cubes)):
            j_offset = j * 0.01
            cube = cubes[j]
            cube.draw(i_offset, j_offset)


def drawPlayer():
    global playerCube, player
    playerCube.draw((player[0] - 1) / 2 * 0.01, (player[1] - 1) / 2 * 0.01)


def drawGoal():
    global goal, goalCube
    goalCube.draw((goal[0] - 1) / 2 * 0.01, (goal[1] - 1) / 2 * 0.01)


def drawBlocks():
    global blocksCenter, blocksCubes
    for i in range(len(blocksCubes)):
        cube = blocksCubes[i]
        center = blocksCenter[i]
        cube.draw((center[0] - 1) / 2 * 0.01, (center[1] - 1) / 2 * 0.01)


def generateCubes():
    global groundMapCenters, gameMap, groundMapCubes, goal, goalCube
    global player, playerCube, blocksCenter, blocksCubes
    blocksCubes = []
    groundMapCubes = []
    for i in groundMapCenters:
        cubes = []
        for j in i:
            cube = cube_file.getCube(j, [0.9, 0.9, 0.9])
            cubes.append(cube)
        groundMapCubes.append(cubes)
    for i in blocksCenter:
        blocksCubes.append(cube_file.getCube(i, [0.5, 0.5, 0.5]))
    playerCube = cube_file.getCube(player, [0.8, 0.8, 0])
    goalCube = cube_file.getCube(goal, [0.8, 0, 0])


def prepareMap():
    global groundMapCenters, gameMap, player, blocksCenter, blocksCubes
    global goal, goalCube
    gameMap.generateMap()
    groundMapCenters = gameMap.getGround()
    player = gameMap.getPlayer()
    gameMap.generateBlocks()
    blocksCenter = gameMap.getBlocks()
    gameMap.generateGoal()
    goal = gameMap.getGoal()


def InitGL(Width, Height):
    glClearColor(0.0, 0.3, 0.3, 0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def main():
    global window

    prepareMap()

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(960, 540)
    glutInitWindowPosition(400, 100)
    window = glutCreateWindow('Graphic Project')

    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutKeyboardFunc(keyPressed)
    glutSpecialFunc(keyPressed)
    InitGL(960, 540)
    glutMainLoop()


if __name__ == "__main__":
    main()
