PIECE_INFO = {
  "I": {
    "color": "#00FFFF",
    "rotations": [
      [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
      ],
      [
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0]
      ],
      [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0]
      ],
      [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]
      ]
    ],
    "kick_index": 1
  },
  "O": {
    "color": "#FFFF00",
    "rotations": [
      [
        [1, 1],
        [1, 1]
      ],
      [
        [1, 1],
        [1, 1]
      ],
      [
        [1, 1],
        [1, 1]
      ],
      [
        [1, 1],
        [1, 1]
      ]
    ],
    "kick_index": 2
  },
  "T": {
    "color": "#800080",
    "rotations": [
      [
        [0, 1, 0],
        [1, 1, 1],
        [0, 0, 0]
      ],
      [
        [0, 1, 0],
        [0, 1, 1],
        [0, 1, 0]
      ],
      [
        [0, 0, 0],
        [1, 1, 1],
        [0, 1, 0]
      ],
      [
        [0, 1, 0],
        [1, 1, 0],
        [0, 1, 0]
      ]
    ],
    "kick_index": 0
  },
  "S": {
    "color": "#00FF00",
    "rotations": [
      [
        [0, 1, 1],
        [1, 1, 0],
        [0, 0, 0]
      ],
      [
        [0, 1, 0],
        [0, 1, 1],
        [0, 0, 1]
      ],
      [
        [0, 0, 0],
        [0, 1, 1],
        [1, 1, 0]
      ],
      [
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0]
      ]
    ],
    "kick_index": 0
  },
  "Z": {
    "color": "#FF0000",
    "rotations": [
      [
        [1, 1, 0],
        [0, 1, 1],
        [0, 0, 0]
      ],
      [
        [0, 0, 1],
        [0, 1, 1],
        [0, 1, 0]
      ],
      [
        [0, 0, 0],
        [1, 1, 0],
        [0, 1, 1]
      ],
      [
        [0, 1, 0],
        [1, 1, 0],
        [1, 0, 0]
      ]
    ],
    "kick_index": 0
  },
  "J": {
    "color": "#0000FF",
    "rotations": [
      [
        [1, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
      ],
      [
        [0, 1, 1],
        [0, 1, 0],
        [0, 1, 0]
      ],
      [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 1]
      ],
      [
        [0, 1, 0],
        [0, 1, 0],
        [1, 1, 0]
      ]
    ],
    "kick_index": 0
  },
  "L": {
    "color": "#FF7F00",
    "rotations": [
      [
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
      ],
      [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
      ],
      [
        [0, 0, 0],
        [1, 1, 1],
        [1, 0, 0]
      ],
      [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
      ]
    ],
    "kick_index": 0
  }
}

KICK_TABLE = [
  [
    [
      [[0, 0]],
      [[0, 0], [-1, 0], [-1, 1], [0, -2], [-1, -2]],
      [[0, 0], [0, 1], [1, 1], [-1, 1], [1, 0], [-1, 0]],
      [[0, 0], [1, 0], [1, 1], [0, -2], [1, -2]]
    ],
    [
      [[0, 0], [1, 0], [1, -1], [0, 2], [1, 2]],
      [[0, 0]],
      [[0, 0], [1, 0], [1, -1], [0, 2], [1, 2]],
      [[0, 0], [1, 0], [1, 2], [1, 1], [0, 2], [0, 1]]
    ],
    [
      [[0, 0], [0, -1], [-1, -1], [1, -1], [-1, 0], [1, 0]],
      [[0, 0], [-1, 0], [-1, 1], [0, -2], [-1, -2]],
      [[0, 0]],
      [[0, 0], [1, 0], [1, 1], [0, -2], [1, -2]]
    ],
    [
      [[0, 0], [-1, 0], [-1, -1], [0, 2], [-1, 2]],
      [[0, 0], [-1, 0], [-1, 2], [-1, 1], [0, 2], [0, 1]],
      [[0, 0], [-1, 0], [-1, -1], [0, 2], [-1, 2]],
      [[0, 0]]
    ]
  ],
  [
    [
      [[0, 0]],
      [[0, 0], [1, 0], [-2, 0], [-2, -1], [1, 2]],
      [[0, 0], [0, 1], [1, 1], [-1, 1], [1, 0], [-1, 0]],
      [[0, 0], [-1, 0], [2, 0], [2, -1], [-1, 2]]
    ],
    [
      [[0, 0], [-1, 0], [2, 0], [-1, -2], [2, 1]],
      [[0, 0]],
      [[0, 0], [-1, 0], [2, 0], [-1, 2], [2, -1]],
      [[0, 0], [1, 0], [1, 2], [1, 1], [0, 2], [0, 1]]
    ],
    [
      [[0, 0], [0, -1], [-1, -1], [1, -1], [-1, 0], [1, 0]],
      [[0, 0], [-2, 0], [1, 0], [-2, 1], [1, -2]],
      [[0, 0]],
      [[0, 0], [2, 0], [-1, 0], [2, 1], [-1, -2]]
    ],
    [
      [[0, 0], [1, 0], [-2, 0], [1, -2], [-2, 1]],
      [[0, 0], [-1, 0], [-1, 2], [-1, 1], [0, 2], [0, 1]],
      [[0, 0], [1, 0], [-2, 0], [1, 2], [-2, -1]],
      [[0, 0]]
    ]
  ],
  [
    [
      [[0, 0]],
      [[0, 0]],
      [[0, 0]],
      [[0, 0]]
    ],
    [
      [[0, 0]],
      [[0, 0]],
      [[0, 0]],
      [[0, 0]]
    ],
    [
      [[0, 0]],
      [[0, 0]],
      [[0, 0]],
      [[0, 0]]
    ],
    [
      [[0, 0]],
      [[0, 0]],
      [[0, 0]],
      [[0, 0]]
    ]
  ]
]

# board = [["N"] * 10 for _ in range(40)]


def boardToString(board):
  boardStr = ""

  for row in board:
    boardStr += "".join(row)
    boardStr += "\n"

  return boardStr

# print(boardToString())


def isValid(board, piece, px, py, r):
  rMatrix = PIECE_INFO[piece]["rotations"][r]

  for dy in range(len(rMatrix)):
    for dx in range(len(rMatrix[dy])):
      x = px + dx
      y = py + dy

      if rMatrix[dy][dx] == 1 and (x < 0 or x >= 10 or y < 0 or y >= 40 or board[y][x] != "N"):
        return False
  
  return True

def getRotationResult(board, piece, px, py, r, rot):
  newR = r + rot
  while newR < 0: newR += 4
  while newR >= 4: newR -= 4
  kicks = KICK_TABLE[PIECE_INFO[piece]["kick_index"]][r][newR]

  for dx, dy in kicks:
    if isValid(board, piece, px+dx, py-dy, newR): # dy in kick table is pos for up, but needs to be reversed cus top board row is index 0
      return (px+dx, py-dy, newR, True)
  
  return (px, py, r, False)

def isTerminal(board, piece, px, py, r):
  return not isValid(board, piece, px, py+1, r)

def getAllBoardStates(board, piece):
  stack = [(3 if piece != "O" else 4, 0, 0)]
  terminal_states = set()
  seen = set()
  moves = [(1, 0), (-1, 0), (0, 1)] # (0, 1) is move down, since top row is index 0
  rotations = [1, -1, 2]

  while stack:
    curr = stack.pop()

    if curr in seen:
      continue

    seen.add(curr)
    px, py, r = curr

    if isTerminal(board, piece, px, py, r):
      terminal_states.add(curr)
    
    for dx, dy in moves:
      if isValid(board, piece, px + dx, py + dy, r):
        stack += [(px + dx, py + dy, r)]
    
    for rot in rotations:
      newX, newY, newR, valid = getRotationResult(board, piece, px, py, r, rot)

      if valid:
        stack += [(newX, newY, newR)]
  
  return terminal_states


def getBoardString(board, piece, px, py, r):
  board_copy = [row[:] for row in board]
  
  rMatrix = PIECE_INFO[piece]["rotations"][r]

  for dy in range(len(rMatrix)):
    for dx in range(len(rMatrix[dy])):
      if rMatrix[dy][dx] == 1:
        x = px + dx
        y = py + dy
        board_copy[y][x] = piece
  
  boardStr = ""

  for row in board_copy:
    boardStr = "".join(row) + boardStr
  
  return boardStr



def getBoardMatrix(boardStr):
  boardArr = []

  for r in range(40):
    row = []

    for c in range(10):
      i = 10 * r + c
      row += [boardStr[i]]
    
    boardArr.insert(0, row)
  
  return boardArr

init_board = getBoardMatrix("GGGGGNGGGGGGGGGGGGGNGGGGGGGGGNGGGGGGGGGNGGGGGGGGGNGGGGGGGGGNGGGGGGNGGGGGGGGNGGGGGGGGGNGGGGGGGGGNGGGGSSTTTLNJJJNSSTNNNLZJNNNNNNNLZZNNNNNNNLLZNNNNIIIIOONNNNNNNNOONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
init_piece = "J"
# print(isValid(init_board, init_piece, 7, 37, 1))
# print(boardToString(init_board))
states = getAllBoardStates(init_board, init_piece)
boardStrings = []

for px, py, r in states:
  boardStrings += [getBoardString(init_board, init_piece, px, py, r)]

boardStrings = sorted(list(set(boardStrings)))
# print(sorted(boardStrings))

import json

with open("states.json", "w") as f:
    json.dump(list(states), f)

with open("boardStrings.json", "w") as f:
    json.dump(boardStrings, f)


