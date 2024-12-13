# GEO1000 - Assignment 2
# Authors: Xinya Bi, Xu Wang
# Studentnumbers:6195350, 6235379


def wiggle(start, end, moves):
    # if it's already at end point and there's no move, gives 1
    if start == end and moves == 0:
        return 1
    # if it can't reach the end point, then it's impossible
    if moves == 0 and abs(start-end) > moves:
        return 0
    else:
        # either move 1 step left or 1 step right
        return wiggle(start-1, end, moves - 1) + wiggle(start, end-1, moves - 1)



if __name__ == "__main__":
    print("running cab.py directly")
    print(wiggle(1, 4, 5))
    print(wiggle(4, 1, 5))
    print(wiggle(1, 4, 2))


