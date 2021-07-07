# def make_bricks(small, big, goal):
#     total_bricks = small + big*5
#     if goal > total_bricks:
#         return False
#     if goal%5 > small:
#         return False
#     return True

def make_chocolate_possible(small, big, goal):
    if goal > big*5 + small:
        return False
    if goal%5 > small:
        return False
    return True
    
def make_chocolate(small, big, goal):
    if make_chocolate_possible(small, big, goal) == False:
        return -1
    if goal == big*5:
        return 0
    if big*5 < goal:
        return goal - (big*5)
    if goal % (big*5) > 0 and goal % (big*5) <= small:
        if goal % (big*5) == small:
            return small
        else:
            return goal % (big*5)
    if big*5 > goal:
        return goal%5