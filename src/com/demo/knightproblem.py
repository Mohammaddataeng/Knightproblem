from src.com.util import utils as f


class cell:

    def __init__(self, x=0, y=0, dist=0, path=[]):
        self.x = x
        self.y = y
        self.dist = dist
        self.path = path








# Method returns the shortest path  to reach
# target position


def stepToReachTarget(knightpos,
                      targetpos, N):

    # all possible movements for the knight
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    queue = []

    # push starting position of knight
    # with 0 distance
    queue.append(cell(knightpos[0], knightpos[1], 0, [f.cordtopos((knightpos[0], knightpos[1]))]))

    # make all cell unvisited
    visited = {(knightpos[0], knightpos[1]): 1}

     # loop until we have one element in queue to check all possibliety of movement
    while (len(queue) > 0):

        t = queue[0]

        # if current cell is equal to target
        # cell, return its distance
        if (t.x == targetpos[0] and
                t.y == targetpos[1]):
            print("Total Moves : ", t.dist)
            print("Path : ", t.path)
            return t.path

        # iterate for all reachable states [Possible movement from current position]
        for i in range(8):

            x = t.x + dx[i]  # Next x-axis location
            y = t.y + dy[i]  # Next y-axis location
            cord = (x, y)

            if (f.isInside(x, y, N) and cord not in visited):
                visited[cord] = 1

                new_list = t.path + [f.cordtopos(cord)]
                queue.append(cell(x, y, t.dist + 1, new_list))
    print("Impossible")


# Main method (starting point of the program)
if __name__ == '__main__':
    N = 8
    inputVal = input("Please enter knight current position and target position [Exp D4 G7] :-  ")
    if inputVal:
        inputVals = inputVal.split(" ")
        if len(inputVals) == 2:
            knightpos = f.postocord(inputVals[0])
            targetpos = f.postocord(inputVals[1])
            stepToReachTarget(knightpos, targetpos, N)
        else:
            print("Incorrect input")
    # Function call