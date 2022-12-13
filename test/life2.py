import time

X_MAX = 20
Y_MAX = 20

class Point:
    def __init__(self):
        self._text = '#'
    
    def get_text(self):
        return self._text


def main():
    # Create two X_MAX * Y_MAX arrays, plus two more for borders.
    world =      [ [None] * (Y_MAX+2) for i in range(X_MAX+2) ]
    next_world = [ [None] * (Y_MAX+2) for i in range(X_MAX+2) ]

    # Glider test
    world[1][1] = Point()
    world[1][2] = None
    world[1][3] = None
    world[2][1] = None
    world[2][2] = Point()
    world[2][3] = Point()
    world[3][1] = Point()
    world[3][2] = Point()
    world[3][3] = None

    print("\033[2J")      # Clear screen

    while True:
        # Wrap endless world by using borders to mirror the opposite side.
        for y in range(1, Y_MAX+1):
            world[0][y] = world[X_MAX][y]
            world[X_MAX+1][y] = world[1][y]
        
        for x in range(1, X_MAX+1):
            world[x][0] = world[x][Y_MAX]
            world[x][Y_MAX+1] = world[x][1]
        
        world[0][0]             = world[X_MAX][Y_MAX]
        world[X_MAX+1][Y_MAX+1] = world[1][1]
        world[X_MAX+1][0]       = world[1][Y_MAX]
        world[0][Y_MAX+1]       = world[X_MAX][1]
        # End wrap endless world.

        # Compute next state.
        for y in range(1, Y_MAX+1):
            for x in range(1, X_MAX+1):                
                # Count neighbors
                d = count_neighbors(world, x, y)

                # Rules
                if d == 3 or world[x][y] and d == 2:
                    next_world[x][y] = Point()
                else:
                    next_world[x][y] = None


        # Print next state and update world.
        print("\033[1;1H")   # Home cursor
        print('+' + '-' * (X_MAX) + '+')

        for y in range(1, Y_MAX+1):
            print('|', end='')
            for x in range(1, X_MAX+1):
                if next_world[x][y]:
                    print(next_world[x][y].get_text(), end='')
                else:
                    print(' ', end='')
                world[x][y] = next_world[x][y]
            print('|')
        print('+' + '-' * (X_MAX) + '+')

        time.sleep(0.058)


def count_neighbors(world, x, y):
    n = 0
    n += 1 if world[x-1][y-1] else 0
    n += 1 if world[x-1][y] else 0
    n += 1 if world[x-1][y+1] else 0
    n += 1 if world[x][y-1] else 0
    n += 1 if world[x][y+1] else 0
    n += 1 if world[x+1][y-1] else 0
    n += 1 if world[x+1][y] else 0
    n += 1 if world[x+1][y+1] else 0
    return n


    #     d =  world[x-1][y-1] + world[x-1][y] + world[x-1][y+1] 
    # d += world[x][y-1]                   + world[x][y+1]  
    # d += world[x+1][y-1] + world[x+1][y] + world[x+1][y+1]


if __name__ == "__main__":
    main()
