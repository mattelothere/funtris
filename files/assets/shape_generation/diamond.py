# function to form the diamond shape
# n must be odd,
def diamond(n):
    height = n//2
    mat = []
    for i in range(height):
        line = []
        for j in range(height-i):
            line.append(0)
        for k in range(2*i+1):
            line.append(1)
        for l in range(height-i):
            line.append(0)
        mat.append(line)
    mat.append([1 for i in range(n)])
    for i in range(height-1, -1, -1):
        line = []
        for j in range(height-i):
            line.append(0)
        for k in range(2 * i + 1):
            line.append(1)
        for l in range(height-i):
            line.append(0)
        mat.append(line)
    return mat


def gen_diamond(size: str, path: str):
    """
    generates a map of shape diamond with the requested size and saves it as a txt file at the wanted path
    size : either "small", "medium" or "large"
    path : the path to the directory you want to save the matrix in
    """
    with open(path+"diamond_"+size+".txt", "w") as f:
        if size == "small":
            size = 21
        elif size == "medium":
            size = 23
        elif size == "large":
            size = 25
        else:  # set size to medium by default
            size = 23
        diamond_mat = diamond(size)
        for line in diamond_mat:
            for character in line:
                f.write(str(character))
            f.write("\n")


if __name__ == "__main__":
    gen_diamond("small", "../assets/gamegrids/diamond/")
    gen_diamond("medium", "../assets/gamegrids/diamond/")
    gen_diamond("large", "../assets/gamegrids/diamond/")
