import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter

recipe_board = [3,7]

e1n = 0
e2n = 1

# input = 2018
input = 920831

done = False

recipes = 2

while len(recipe_board) < 11 + input:
    new_recipe = recipe_board[e1n]+recipe_board[e2n]
    if new_recipe < 10:
        recipe_board.append(new_recipe)
    else:
        recipe_board.append(1)
        recipe_board.append(new_recipe-10)
    e1n += 1 + recipe_board[e1n]
    e2n += 1 + recipe_board[e2n]
    board_length = len(recipe_board)
    while e1n >= board_length:
        e1n -= board_length
    while e2n >= board_length:
        e2n -= board_length

result = ''
for i in range(input,input+10):
    result += str(recipe_board[i])

print(result)
