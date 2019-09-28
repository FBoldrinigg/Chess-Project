from Engine import Engine


game = Engine()
print("1) Start game\n2) Debug mode")
test = int(input(": "))
if test == 1:
    while not game.isGameOver:
        game.assignTurn()
    game.winningScreen()
elif test == 2:
    game.debugMode()
