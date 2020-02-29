sub = ['io','tu','lui','lei','noi','voi','loro']
essere = {'io':'sono','tu':'sei','lui':'e','lei':'e','noi':'siamo','voi':'siete','loro':'sono'}
from random import randint

while True:
    subj = sub[randint(0, 6)]
    answer = input('Conjugate essere to {}'.format(subj))
    if answer == 'q':
        break
    elif answer == essere[subj]:
        print('Correct!')
    else :
        print('Oups! The answer is {}'.format(essere[subj]))
