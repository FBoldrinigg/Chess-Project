from Engine import Engine


game = Engine()
while not game.isGameOver:
    game.assignTurn()
