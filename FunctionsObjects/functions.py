import time

def calculate_result(parm1, parm2):
    result = parm1 + parm2 * 2
    print('-------------------------')
    print('-------------------------')
    print('Result: ' + str(result))
    print('-------------------------')
    print('-------------------------')

for i in range(10):
    print('Iteration number ' + str(i + 1))
    time.sleep(.5)

    j = 1
    while j != 10:
        if j == 5 or j == 4 or j == 3 or j == 2 or j == 1:
            try:
                print('NESTED: Iteration number ' + str(k))
            except Exception as e:
                print('Error: ' + str(e))
                calculate_result(i, j)
        elif j == 6 and i == 6:
            print('TEST: Iteration number ' + str(j) + ' == ' + str(i))
        else:
            print('Not checked!')
        j += 1
        time.sleep(.1)