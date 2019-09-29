from Engine import Engine


game = Engine()
select = ""
print("\n\n###### Python Chess ######\n(1) Start game\n(2) Debug mode")
while not select:
    try:
        select = int(input(": "))
        if not 1 <= select <= 2:
            raise ValueError
    except ValueError:
        print("Invalid input.")
        select = ""
if select == 1:
    while not game.isGameOver:
        game.assignTurn()
    game.winningScreen()
elif select == 2:
    game.debugMode()
