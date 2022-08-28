import time


for i in range(10):
    print('Iteration number ' + str(i + 1))
    time.sleep(.5)

    j = 1
    while j != 10:
        if j == 5 or j == 4 or j == 3 or j == 2 or j == 1:
            print('NESTED: Iteration number ' + str(j))
        elif j == 6 and i == 6:
            print('TEST: Iteration number ' + str(j) + ' == ' + str(i))
        else:
            print('Not checked!')
        j += 1
        time.sleep(.1)