import random
import os
def _cls():
    os.system('cls' if os.name=='nt' else 'clear')
def fortune():
    keepgoing = 0
    print('Welcome to Fortune-telling')
    while keepgoing != 2:
        positive = ['Yes, go ahead!', 'You should do it now', 'Just go', 'NOW!', 'You are the best to do it', 'YEAH!', 'Sure']
        negative = ['No', 'Nope','Are you crazy? NO!','Just no']
        answertype = random.randint(1,2)
        answer = ''
        sizepositive = len(positive)
        sizenegative = len(negative)
        question = input('Ask:\n> ')
        if answertype == 1:
            positiveanswer = random.randint(0, sizepositive)
            answer = positive[positiveanswer]
            print(f'{answer}')
            keepgoing = int(input('\nDo you want to play again? [1] Yes [2] No\n> '))
            _cls()
        elif answertype == 2:
            negativeanswer = random.randint(0, sizenegative)
            answer = negative[negativeanswer]
            print(f'{answer}')
            keepgoing = int(input('\nDo you want to play again? [1] Yes [2] No\n> '))
fortune()