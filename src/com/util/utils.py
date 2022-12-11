
# checks whether given position is
# inside the board

def isInside(x, y, N):
    if (x >= 1 and x <= N and
            y >= 1 and y <= N):
        return True
    return False

def postocord(pos) :

    cordis = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    prefix = pos[:1]

    ypos = suffix = pos[-1]

    xpos = cordis[prefix]

    return xpos, int(ypos)


def cordtopos(cord):

    possdis = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}

    prefix = possdis[cord[0]]
    suffix = cord[1]

    return "{}{}".format(prefix, suffix)

# if __name__ == '__main__':
#      value = input("Please enter start and target position : ")
#      print(value)
#
#      print(postocorrd('D5'))
#      print(postocorrd('G5'))
#      print(postocorrd('H5'))
#
#      print(corrdtopos((4, 5)))
#      print(corrdtopos((7, 5)))
#      print(corrdtopos((8, 5)))