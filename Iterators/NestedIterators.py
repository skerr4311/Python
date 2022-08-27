import time


for i in range(10):
    print('Iteration number ' + str(i + 1))
    time.sleep(1)

    j = 1
    while j != 10:
        print('NESTED: Iteration number ' + str(j))
        j += 1