def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    list_plane = []
    c = 0
    for i in matrix:
        for k in i:
            list_plane.append(k)
    for j in list_plane:
        c += 1
        if c == 3:
            c = 0
            print("{:d}".format(j))
        elif c < 3:
            print("{:d}".format(j), end=" ")
        else:
            pass
