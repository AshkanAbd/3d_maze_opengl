import random


class Map:
    __groundArray = []
    __player = []
    __blocks = []
    __blocks2D = []
    __random = random.Random
    __goal = []

    def __init__(self):
        self.__player = [(7 * 2) + 1, 1, 2.1]
        self.__random = random.Random()

    def generateMap(self):
        for x in range(8):
            arr = []
            for y in range(8):
                c_x = (x * 2) + 1
                c_y = (y * 2) + 1
                arr1 = [c_x, c_y, 0]
                arr.append(arr1)
            self.__groundArray.append(arr)

    def generateBlocks(self):
        for i in range(10):
            while True:
                x = self.__random.randint(0, 7)
                y = self.__random.randint(0, 7)
                if ([x, y] not in self.__blocks2D) and (not (x == 7 and y == 0)):
                    break
            self.__blocks2D.append([x, y])
            self.__blocks.append([(x * 2) + 1, (y * 2) + 1, 2.1])

    def generateGoal(self):
        while True:
            x = self.__random.randint(0, 7)
            y = self.__random.randint(0, 7)
            if ([x, y] not in self.__blocks2D) and (not (x == 7 and y == 0)):
                break
        self.__goal.append([(x * 2) + 1, (y * 2) + 1, 0])

    def getGround(self):
        return self.__groundArray

    def getBlocks(self):
        return self.__blocks

    def getPlayer(self):
        return self.__player

    def getGoal(self):
        return self.__goal[0]
