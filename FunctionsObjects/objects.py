import time

# CAR MANUFACTURER
class Car:
    numberOfWindows = 4
    color = 'red'
    manufactured = True

def calculate_result(parm1, parm2):
    result = parm1 + parm2 * 2
    print('-------------------------')
    print('-------------------------')
    print('Result: ' + str(result))
    print('-------------------------')
    print('-------------------------')

# FOR EVERY CAR IN THE LINE
for i in range(10):

    sportsCar = Car
    print('Windows: ' + str(sportsCar.numberOfWindows))
    print('Color: ' + str(sportsCar.color))

    print('Iteration number ' + str(i + 1))
    time.sleep(.5)

    # WHILE CAR IS BEING MADE
    j = 1
    while j != 10: # CAR PARTS ITERATOR
        if j == 5 or j == 4 or j == 3 or j == 2 or j == 1:
            try:
                print('NESTED: Iteration number ' + str(k))
            except Exception as e:
                print('Error: ' + str(e))
                calculate_result(i, j)
        elif j == 6 and i == 6: # SPECIAL PART FOR SPECIAL CAR
            print('TEST: Iteration number ' + str(j) + ' == ' + str(i))
        else:
            print('Not checked!')
        j += 1
        time.sleep(.1)