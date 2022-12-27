########################################################################################################################
#
#                    This is a file for storing each the available blocks common to all board
#

#       Structure :
#           BLOCKS = [
#     [
#         [0, 0, 0, 0], block n° 0
#         [0, 0, 0, 0],
#         [2, 0, 0, 0],
#         [2, 2, 0, 0],
#     ],
#
#     [
#       [...] block n° n-2
#     ],
#
#     [...], block n° n-1
#
#     ]

#       Note :
#           -each element of the BLOCKS list is an integer 2D-matrix where :
#                   - a 0 represents the absence of a block
#                   - a 2 represents the presence of a block
#

########################################################################################################################

BLOCKS = [
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [2, 0, 0, 0],
        [2, 2, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 2, 0, 0],
        [2, 2, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [2, 0, 0, 0],
        [2, 2, 2, 0],
    ],
    [
        [0, 0, 0, 0],
        [2, 2, 0, 0],
        [0, 2, 0, 0],
        [0, 2, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [2, 0, 0, 0],
        [2, 2, 0, 0],
        [2, 0, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 2, 0, 0],
        [2, 2, 2, 0],
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [2, 2, 0, 0],
        [0, 2, 2, 0],
    ],
    [
        [0, 0, 0, 0],
        [2, 0, 0, 0],
        [2, 2, 0, 0],
        [0, 2, 0, 0],
    ],
    [
        [2, 0, 0, 0],
        [2, 0, 0, 0],
        [2, 0, 0, 0],
        [2, 0, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [2, 2, 0, 0],
        [2, 2, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [2, 2, 0, 0],
        [0, 2, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [2, 2, 0, 0],
        [2, 0, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, 0],
        [2, 2, 2, 0],
    ],
    [
        [0, 0, 0, 0],
        [2, 0, 0, 0],
        [2, 0, 0, 0],
        [2, 2, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [0, 2, 0, 0],
        [2, 2, 0, 0],
        [0, 2, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [2, 2, 2, 0],
        [0, 2, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 2, 2, 0],
        [2, 2, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [0, 2, 0, 0],
        [2, 2, 0, 0],
        [2, 0, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [2, 0, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [2, 2, 2, 2],
    ],
]

if __name__ == "__main__":
    def display_block(blocks: list,):
        """
        used for displaying a block "as it would appear"
        :param blocks: 2D matrix representing a block
        :return: nothing
        """
        for i, block in enumerate(blocks):
            print(f"block n°{i}")
            for line in block:
                for column in line:
                    if column == 2:
                        print("■", end="░")
                    elif column == 0:
                        print("░", end="░")
                    else:
                        print("!", end="!") # if the value inst expected
                print("")

    def display_block_v2(blocks: list, blocks_per_line: int):
        """
        used for displaying a block "as it would appear"
        :param blocks: 2D matrix representing a block
        :return: nothing
        """
        for i in range(0, len(blocks), blocks_per_line):
            for j in range(len(blocks[i])):
                for k in range(blocks_per_line):

                    print("|", end="")
                    for column in blocks[i+k][j]:
                        if column == 2:
                            print("■", end="░")
                        elif column == 0:
                            print("░", end="░")
                        else:
                            print("!", end="!") # if the value inst expected

                print("|")
            print(f"Blocks {i+1} to {i+blocks_per_line}")

    print("common set")
    display_block_v2(BLOCKS, 10)

