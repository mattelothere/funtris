def circle(size):
    """
    generates a size*size matrix representing the playable space
    """
    # mat = [[5] * size] * size # is an error : copies the memory address
    mat = [[0] * size for _ in range(size)]
    corner_size = 3

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (i+j) <= corner_size or (size-1-j+i) <= corner_size or (size-1-i+j) <= corner_size or (size-1-i+size-1-j) <= corner_size:
                mat[i][j] = 0
            else:
                mat[i][j] = 1
    return mat


def gen_circle(size: str, path: str):
    """
    generates a map of shape circle with the requested size and saves it as a txt file at the wanted path
    size : either "small", "medium" or "large"
    path : the path to the directory you want to save the matrix in
    """
    with open(path+"circle_"+size+".txt", "w") as f:
        if size == "small":
            size = 21
        elif size == "medium":
            size = 23
        elif size == "large":
            size = 25
        else:  # set size to medium by default
            size = 23
        circle_mat = circle(size)
        for line in circle_mat:
            for character in line:
                f.write(str(character))
            f.write("\n")


if __name__ == "__main__":
    gen_circle("small", "../assets/gamegrids/circle/")
    gen_circle("medium", "../assets/gamegrids/circle/")
    gen_circle("large", "../assets/gamegrids/circle/")
