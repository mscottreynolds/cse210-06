import time
import random


def main():
    rows = 20
    cols = 50
    max = rows * cols
    c=220
    d=700
    m = [0] * max
    n = [0] * max

    print("\033[2J")      # Clear screen

    # Initialize arrays.
    # for j in range(0, i):
    #     m[j] = 0
    #     n[j] = 0

    # drop cells at random locations.
    for j in range(0, d):
        m[random.randint(0, max-1)] = 1
        
    # While c generations...
    while c > 0:
        c -= 1

        for i in range(51, 949):
            # Count neighbors.
            d = m[i-1] + m[i+1] + m[i-51] + m[i-50] + m[i-49] + m[i+49] + m[i+50] + m[i+51]

            # Compute new state.
            n[i] = m[i]
            if m[i] == 0 and d == 3:
                n[i] = 1
            elif m[i] == 1 and d < 2:
                n[i] = 0
            elif m[i] == 1 and d > 3:
                n[i] = 0
        
        # Display results.
        print("\033[1;1H")   # Home cursor
        print(c)     # Countdown
        for i in range(0, max): # Gridsize 50x20
            if n[i] > 0:
                print("O", end='')
            else:
                print(".", end='')
            
            if (i+1) % 50 == 0:
                print('')       # Print new line.

            # And new state to main array.
            m[i] = n[i]

        time.sleep(0.5)

main()
