layout = {
    1: (70, 415),
    2: (245, 415),
    3: (415, 415),
    4: (70, 250),
    5: (245, 250),
    6: (415, 250),
    7: (70, 75),
    8: (245, 75),
    9: (415, 75)
}

x_winning_conditions = [
    [
        "1", "1", "1",
        "0", "0", "0",
        "0", "0", "0"
    ],
    [
        "0", "0", "0",
        "1", "1", "1",
        "0", "0", "0"
    ],
    [
        "0", "0", "0",
        "0", "0", "0",
        "1", "1", "1"
    ],
    [
        "1", "0", "0",
        "1", "0", "0",
        "1", "0", "0"
    ],
    [
        "0", "1", "0",
        "0", "1", "0",
        "0", "1", "0"
    ],
    [
        "0", "0", "1",
        "0", "0", "1",
        "0", "0", "1"
    ],
    [
        "1", "0", "0",
        "0", "1", "0",
        "0", "0", "1"
    ],
    [
        "0", "0", "1",
        "0", "1", "0",
        "1", "0", "0"
    ]
]

y_winning_conditions = [
    [
        "2", "2", "2",
        "0", "0", "0",
        "0", "0", "0"
    ],
    [
        "0", "0", "0",
        "2", "2", "2",
        "0", "0", "0"
    ],
    [
        "0", "0", "0",
        "0", "0", "0",
        "2", "2", "2"
    ],
    [
        "2", "0", "0",
        "2", "0", "0",
        "2", "0", "0"
    ],
    [
        "0", "2", "0",
        "0", "2", "0",
        "0", "2", "0"
    ],
    [
        "0", "0", "2",
        "0", "0", "2",
        "0", "0", "2"
    ],
    [
        "2", "0", "0",
        "0", "2", "0",
        "0", "0", "2"
    ],
    [
        "0", "0", "2",
        "0", "2", "0",
        "2", "0", "0"
    ]
]

def CheckXWin(board):
    refinedBoard = []
    for num in board:
        if num != "1":
            refinedBoard.append("0")
        else:
            refinedBoard.append(num)
    for condition in x_winning_conditions:
        for num in condition:
            if condition[0] == refinedBoard[0] and condition[1] == refinedBoard[1] and condition[2] == refinedBoard[2] and condition[3] == refinedBoard[3] and condition[4] == refinedBoard[4] and condition[5] == refinedBoard[5] and condition[6] == refinedBoard[6] and condition[7] == refinedBoard[7] and condition[8] == refinedBoard[8]:
                return True
    return False

def CheckYWin(board):
    refinedBoard = []
    for num in board:
        if num != "2":
            refinedBoard.append("0")
        else:
            refinedBoard.append(num)
    for condition in y_winning_conditions:
        for num in condition:
            if condition[0] == refinedBoard[0] and condition[1] == refinedBoard[1] and condition[2] == refinedBoard[2] and condition[3] == refinedBoard[3] and condition[4] == refinedBoard[4] and condition[5] == refinedBoard[5] and condition[6] == refinedBoard[6] and condition[7] == refinedBoard[7] and condition[8] == refinedBoard[8]:
                return True
    return False

def CheckBoardFull(board):
    xWon = CheckXWin(board)
    yWon = CheckYWin(board)
    for num in board:
        if num == "0":
            return False
    if xWon or yWon:
        return False
    else:
        return True
    

def GetNumberFromPosition(pos):
    if pos[0] > 0 and pos[0] < 140 and pos[1] < 480 and pos[1] > 350:
        return 1
    if pos[0] > 160 and pos[0] < 330 and pos[1] < 480 and pos[1] > 350:
        return 2
    if pos[0] > 350 and pos[0] < 480 and pos[1] < 480 and pos[1] > 350:
        return 3
    if pos[0] > 0 and pos[0] < 140 and pos[1] < 335 and pos[1] > 160:
        return 4
    if pos[0] > 160 and pos[0] < 330 and pos[1] > 160 and pos[1] < 330:
        return 5
    if pos[0] > 350 and pos[0] < 480 and pos[1] > 160 and pos[1] < 330:
        return 6
    if pos[0] > 0 and pos[0] < 140 and pos[1] > 0 and pos[1] < 350:
        return 7
    if pos[0] > 160 and pos[0] < 330 and pos[1] > 0 and pos[1] < 350:
        return 8
    if pos[0] > 350 and pos[0] < 480 and pos[1] > 0 and pos[1] < 350:
        return 9
    return None


def GetPositionFromNumber(number):
    return layout[number]

