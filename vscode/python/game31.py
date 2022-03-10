from random import *

class Game31 :
    
    def result_Game(result) :
        if result :
            print('You Win!')
        else :
            print('You Lose!')

    def play_game(currentNumber) :
        print('{}!'.format(currentNumber))

    def check_number(your_number) :
        while True :
            try :
                number = int(input(your_number))
                if number >= 1 and number <= 3 :
                    break
                else :
                    print('1에서 3사이의 숫자만 입력하세요')
            except :
                print('잘못 입력했습니다. 숫자만 입력하세요')

        return number

    # def userTurn(currentNumber) :
    #     your_number = '[참가자1] 숫자 몇 개를 부를 건가요? (1~3) : '
    #     userNumber = check_number(your_number)
    #     for count in range (userNumber) :
    #         currentNumber+=1
    #         if(currentNumber==31) :
    #             break
    #         # else :
    #         #     # play_game(currentNumber) 

        return currentNumber
    
    def aiTurn(currentNumber) :
        aiNumber = int(input('[컴퓨터]] 숫자 몇 개를 부를 건가요? (1~3) : {}'.format(randint(1,3))))
        for count in range (aiNumber) :
            currentNumber+=1
            if(currentNumber==31) :
                break
            # else :
            #     # play_game(currentNumber) 

        return currentNumber
