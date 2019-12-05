from __future__ import print_function
import numpy as np
import DiscreteRubiksCube2x2

hO = np.ones(729, dtype=np.int) * 12
hP = np.ones(117649, dtype=np.int) * 12

moveStrs = {0: "U", 1: "U'", 2: "U2", 3: "R", 4: "R'", 5: "R2", 6: "F", 7: "F'", 8: "F2"}

# generate pruning table for the piece orientation states
def genOTable(s, d, lm=-3):
  index = DiscreteRubiksCube2x2.indexO(DiscreteRubiksCube2x2.getOP(s))
  if d < hO[index]:
    hO[index] = d
    for m in range(9):
      if int(m / 3) == int(lm / 3):
        continue
      genOTable(DiscreteRubiksCube2x2.Move(s, m), d + 1, m)

# generate pruning table for the piece permutation states
def genPTable(s, d, lm=-3):
  index = DiscreteRubiksCube2x2.indexP(DiscreteRubiksCube2x2.getOP(s))
  if d < hP[index]:
    hP[index] = d
    for m in range(9):
      if int(m / 3) == int(lm / 3):
        continue
      genPTable(DiscreteRubiksCube2x2.Move(s, m), d + 1, m)

# IDA* which prints all optimal solutions
def IDAStar(s, d, moves, lm=-3):
  if DiscreteRubiksCube2x2.CorrectState(s):
    printMoves(moves)
    return True
  else:
    sOP = DiscreteRubiksCube2x2.getOP(s)
    if d > 0 and d >= hO[DiscreteRubiksCube2x2.indexO(sOP)] and d >= hP[DiscreteRubiksCube2x2.indexP(sOP)]:
      dOptimal = False
      for m in range(9):
        if int(m / 3) == int(lm / 3):
          continue
        newMoves = moves[:]; newMoves.append(m)
        solved = IDAStar(DiscreteRubiksCube2x2.Move(s, m), d - 1, newMoves, m)
        if solved and not dOptimal:
          dOptimal = True
      if dOptimal:
        return True
  return False

# print a move sequence from an array of move indices
def printMoves(moves):
  moveStr = ""
  for m in moves:
    moveStr += moveStrs[m] + " "
  print(moveStr)

# solve a cube state
def solveCube(s):
  # print cube state
  DiscreteRubiksCube2x2.printCube(s)

  # FC-normalize stickers
  print("normalizing stickers...")
  s = DiscreteRubiksCube2x2.updatedFC(s)

  # generate pruning tables
  print("generating pruning tables...")
  genOTable(DiscreteRubiksCube2x2.initState(), 0)
  genPTable(DiscreteRubiksCube2x2.initState(), 0)

  # run IDA*
  print("searching...")
  solved = False
  depth = 1
  while depth <= 10 and not solved:
    print("depth {}".format(depth))
    solved = IDAStar(s, depth, [])
    print(solved)
    depth += 1

if __name__ == "__main__":
  # input some scrambled state
  s = DiscreteRubiksCube2x2.newAlgStr(DiscreteRubiksCube2x2.initState(), "R U2 R2 F2 R' F2 R F R")
  # solve cube
  solveCube(s)

  # s = DiscreteRubiksCube2x2.newAlgStr(DiscreteRubiksCube2x2.initState(), "x y R U' R' U' F2 U' R U R' U F2")
  # solveCube(s)
  #
  # s = DiscreteRubiksCube2x2.newAlgStr(DiscreteRubiksCube2x2.initState(), "F R2 F' R U2 R2 F' R")
  # solveCube(s)
  printMoves(s)
