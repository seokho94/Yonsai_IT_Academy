from game31 import*

class Main :
    game = Game31()
    currentNumber = 0
    turn = True
    while True :
        if turn :
            currentNumber = game.userTurn(currentNumber)
            turn = False
            
        else :
            currentNumber = game.aiTurn(currentNumber)
            turn = True

        if currentNumber==31 :
            if turn :
                game.result_Game(turn)
                break
            else : 
                game.result_Game(turn)
                break