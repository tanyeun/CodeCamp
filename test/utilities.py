def pair_equal_non_order(pair1, pair2):
    if pair1[0] == pair2[0] and pair1[1] == pair2[1]:
        return True
    elif pair1[0] == pair2[1] and pair1[1] == pair2[0]:
        return True
    else:
        return False
