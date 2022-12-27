# function to form the triangle shape
# n must be odd,
def triangle(n):
    height = n // 2
    mat = []
    for i in range(height):
        line = []
        for j in range(height - i):
            line.append("0")
        for k in range(i):
            line.append('1')
        for k in range(i + 1):
            line.append("1")
        for l in range(height - i):
            line.append("0")

        mat.append(line)
    mat.append(["1" for i in range(n)])
    return mat


def gen_triangle(size: str, path: str):
    """
    generates a map of shape triangle with the requested size and saves it as a txt file at the wanted path
    size : either "small", "medium" or "large"
    path : the path to the directory you want to save the matrix in
    """
    with open(path+"triangle_"+size+".txt", "w") as f:
        if size == "small":
            size = 21
        elif size == "medium":
            size = 23
        elif size == "large":
            size = 25
        else:  # set size to medium by default
            size = 23
        triangle_mat = triangle(size)
        for line in triangle_mat:
            for character in line:
                f.write(str(character))
            f.write("\n")


if __name__ == "__main__":
    gen_triangle("small", "../assets/gamegrids/triangle/")
    gen_triangle("medium", "../assets/gamegrids/triangle/")
    gen_triangle("large", "../assets/gamegrids/triangle/")
