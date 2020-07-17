# boards_n = ([list_of_boards], [list_of_available_nums], subgrid_height, subgrid_width)

boards_3 = ([
    [
        [0, 0, 3],
        [2, 0, 0],
        [0, 0, 0]
    ],
    [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 3]
    ],
    [
        [0, 2, 0],
        [0, 0, 0],
        [1, 0, 0]
    ],
    [
        [0, 0, 0],
        [0, 0, 2],
        [1, 0, 0]
    ],
    [
        [3, 0, 0],
        [0, 0, 0],
        [0, 2, 0]
    ],
    [
        [2, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ],
    [
        [1, 0, 0],
        [0, 0, 0],
        [0, 3, 0]
    ],
    [
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 0]
    ],
    [
        [0, 0, 1],
        [0, 0, 0],
        [2, 0, 0]
    ],
    [
        [2, 0, 0],
        [0, 0, 1],
        [0, 0, 0]
    ]
], [0, 1, 2, 3], 0, 0)

boards_4 = ([
    [
        [2, 1, 0, 0],
        [0, 3, 2, 0],
        [0, 0, 0, 4],
        [1, 0, 0, 0]
    ],
    [
        [1, 0, 3, 4],
        [0, 3, 0, 0],
        [2, 0, 0, 0],
        [0, 0, 0, 1]
    ],
    [
        [0, 0, 1, 2],
        [0, 1, 0, 3],
        [0, 0, 0, 0],
        [4, 0, 2, 0]
    ],
    [
        [0, 2, 3, 0],
        [0, 3, 0, 0],
        [0, 0, 0, 1],
        [2, 0, 4, 0]
    ],
    [
        [4, 2, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 2, 0],
        [0, 0, 0, 3]
    ],
    [
        [0, 0, 0, 3],
        [4, 0, 0, 0],
        [0, 1, 3, 0],
        [3, 0, 2, 0]
    ],
    [
        [4, 0, 0, 0],
        [0, 0, 4, 0],
        [0, 1, 2, 0],
        [2, 0, 0, 3]
    ],
    [
        [3, 0, 0, 0],
        [0, 0, 0, 2],
        [0, 1, 0, 3],
        [0, 0, 2, 1]
    ],
    [
        [0, 0, 1, 0],
        [0, 2, 0, 0],
        [4, 0, 2, 0],
        [2, 0, 0, 4]
    ],
    [
        [0, 3, 0, 0],
        [4, 1, 0, 0],
        [1, 2, 3, 0],
        [3, 0, 0, 0]
    ],
    [
        [0, 0, 4, 0],
        [1, 0, 0, 0],
        [0, 2, 0, 0],
        [0, 0, 0, 3]
    ],
    [
        [2, 0, 0, 0],
        [0, 0, 0, 3],
        [0, 0, 0, 0],
        [0, 4, 1, 0]
    ],
    [
        [0, 4, 0, 0],
        [0, 0, 0, 2],
        [0, 0, 0, 0],
        [0, 0, 2, 3]
    ],
    [
        [0, 4, 0, 0],
        [3, 0, 0, 0],
        [0, 0, 1, 4],
        [0, 0, 2, 0]
    ],
    [
        [0, 0, 0, 3],
        [0, 0, 0, 4],
        [3, 0, 0, 0],
        [2, 0, 0, 0]
    ],
    [
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 4, 0, 0],
        [0, 0, 2, 0]
    ],
    [
        [0, 0, 0, 0],
        [4, 3, 0, 2],
        [2, 0, 0, 4],
        [0, 0, 0, 0]
    ],
    [
        [0, 1, 0, 0],
        [0, 0, 2, 0],
        [0, 0, 0, 3],
        [4, 0, 0, 0]
    ],
    [
        [0, 0, 0, 4],
        [4, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 2, 0, 0]
    ],
    [
        [0, 0, 1, 0],
        [3, 0, 0, 0],
        [0, 3, 0, 0],
        [0, 0, 0, 2]
    ]
], [0, 1, 2, 3, 4], 2, 2)

boards_6 = ([
    [
        [0, 5, 0, 0, 0, 1],
        [0, 0, 4, 6, 0, 0],
        [4, 0, 0, 0, 5, 0],
        [1, 0, 0, 0, 0, 4],
        [0, 4, 3, 0, 0, 0],
        [0, 6, 0, 2, 4, 0]
    ]
], [0, 1, 2, 3, 4, 5, 6], 2, 3)

boards_9 = ([
    [
        [0, 3, 0, 0, 0, 1, 0, 8, 9],
        [4, 8, 0, 0, 0, 3, 0, 5, 0],
        [6, 0, 0, 5, 9, 8, 2, 0, 4],
        [8, 0, 0, 6, 0, 0, 0, 2, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 7],
        [2, 7, 0, 0, 0, 9, 0, 0, 8],
        [7, 0, 3, 9, 5, 4, 0, 0, 2],
        [0, 4, 0, 1, 0, 0, 0, 7, 5],
        [1, 2, 0, 8, 0, 0, 0, 4, 0]
    ],
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ],
    [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0],
    ],
    [
        [9, 0, 0, 0, 8, 0, 0, 0, 1],
        [0, 0, 0, 4, 0, 6, 0, 0, 0],
        [0, 0, 5, 0, 7, 0, 3, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 4, 0],
        [4, 0, 1, 0, 6, 0, 5, 0, 8],
        [0, 9, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 7, 0, 3, 0, 2, 0, 0],
        [0, 0, 0, 7, 0, 5, 0, 0, 0],
        [1, 0, 0, 0, 4, 0, 0, 0, 7]
    ],
    [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ],
    [
        [1, 0, 0, 4, 8, 9, 0, 0, 6],
        [7, 3, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 1, 2, 9, 5],
        [0, 0, 7, 1, 2, 0, 6, 0, 0],
        [5, 0, 0, 7, 0, 3, 0, 0, 8],
        [0, 0, 6, 0, 9, 5, 7, 0, 0],
        [9, 1, 4, 6, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 3, 7],
        [8, 0, 0, 5, 1, 2, 0, 0, 4]
    ],
    [
        [0, 2, 0, 6, 0, 8, 0, 0, 0],
        [5, 8, 0, 0, 0, 9, 7, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [3, 7, 0, 0, 0, 0, 5, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 8, 0, 0, 0, 0, 1, 3],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 9, 8, 0, 0, 0, 3, 6],
        [0, 0, 0, 3, 0, 6, 0, 9, 0]
    ],
    [
        [0, 0, 0, 6, 0, 0, 4, 0, 0],
        [7, 0, 0, 0, 0, 3, 6, 0, 0],
        [0, 0, 0, 0, 9, 1, 0, 8, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 1, 8, 0, 0, 0, 3],
        [0, 0, 0, 3, 0, 6, 0, 4, 5],
        [0, 4, 0, 2, 0, 0, 0, 6, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 1, 0, 0]
    ],
    [
        [2, 0, 0, 3, 0, 0, 0, 0, 0],
        [8, 0, 4, 0, 6, 2, 0, 0, 3],
        [0, 1, 3, 8, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 2, 0, 3, 9, 0],
        [5, 0, 7, 0, 0, 0, 6, 2, 1],
        [0, 3, 2, 0, 0, 6, 0, 0, 0],
        [0, 2, 0, 0, 0, 9, 1, 4, 0],
        [6, 0, 1, 2, 5, 0, 8, 0, 9],
        [0, 0, 0, 0, 0, 1, 0, 0, 2]
    ],
    [
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 3],
        [0, 7, 4, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 2],
        [0, 8, 0, 0, 4, 0, 0, 1, 0],
        [6, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 7, 8, 0],
        [5, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0]
    ]
], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
