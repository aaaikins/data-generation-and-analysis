'''Aikins Acheampong
09/13/23
CS 152 A
Lab 01
This is a practice program for the first CS 152 Lab01!'''


def ballistc2(pi, vi, a, t):
    '''calculates the final position of a projectile when the user inputs initial position, 
    initial velocity, acceleration and time.'''
    pf = pi + vi * t + 0.5 * a * t ** 2

    return pf

#test1 = ballistc2(1, 11, -10, 0.5)
#print(test1)

#test2 = ballistc2(2, 11, -10, 0.5)
#print(test2)

def clearfile(filename):
    '''Clears the content of any given file when the user inputs its name (filename)'''
    fp = open( filename, 'w' )
    fp.close()

def computeAndOutput(pi, vi, a, t, filename):
    '''calculates the final position of an object in a ballistic trajectory when the user inputs initial position, 
    initial velocity, acceleration and time, and appends the results to a CSV file you name, and print the results'''
    pf = ballistc2(pi, vi, a, t)

    with open(filename, 'a') as fp:
        fp.write(f'{t}, {pf}\n')
        fp.close()
    print(f"{t}, {pf}")  

def trajectory10(pi, vi, a, ti, dt, filename):
    '''Computes and outputs the final positions of an object in a ballistic trajectory at 10 different time intervals, 
    starting from a given initial time'''
    for N in range(10):
        computeAndOutput(pi, vi, a, ti + N * dt, filename)

def trajectory100(pi, vi, a, ti, dt, filename):
    '''Computes and outputs the final positions of an object in a ballistic trajectory at 100 different time intervals, 
    starting from a given initial time'''
    for i in range(10):
        trajectory10(pi, vi, a, ti, dt, filename)
        ti += 1

def trajectory1000(pi, vi, a, ti, dt, filename):
    '''Computes and outputs the final positions of an object in a ballistic trajectory at 1000 different time intervals, 
    starting from a given initial time'''
    for i in range(100):
        trajectory10(pi, vi, a, ti, dt, filename)
        ti += 1



clearfile('mydata_extension.csv')
trajectory1000(1, 50, -10, 0, 0.1, 'mydata_extension.csv')