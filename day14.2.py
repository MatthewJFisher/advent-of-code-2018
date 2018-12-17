import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter

recipe_board = '37'

e1n = 0
e2n = 1

# input = '59414'
input = '920831'

done = False

recipes = 2

while recipe_board[-len(input):] != input and recipe_board[-len(input)-1:-1] != input:
    # if len(recipe_board)%100000==0:
    #     print(len(recipe_board))
    new_recipe = int(recipe_board[e1n])+int(recipe_board[e2n])
    recipe_board = recipe_board + str(new_recipe)
    # if new_recipe < 10:
    #     recipe_board = recipe_board*10 + new_recipe
    # else:
    #     recipe_board = recipe_board*100 + new_recipe

    e1n += 1 + int(recipe_board[e1n])
    e2n += 1 + int(recipe_board[e2n])
    board_length = len(recipe_board)
    while e1n >= board_length:
        e1n -= board_length
    while e2n >= board_length:
        e2n -= board_length

if recipe_board[-len(input):] == input:
    print(len(recipe_board)-len(input))
else:
    print(len(recipe_board)-len(input)-1)
