'''Aikins Acheampong
09/13/23
CS 152 A
Lab 01
This is a practice program for the first CS 152 Lab01!'''

# pf = 'final position'
# pi = 'initial position'
# vi = 'initial velocity'
# t = 'time'
# a = 'acceleration'

pi = 1
vi = 11
a = -10
t =0.5

pf = pi + vi * t + 0.5 * a * t ** 2

#print(pf)


def ballistc1(t):
    '''calculates the final position of a projectile when its initial position, 
    initial velocity and acceleration is constant.'''
    pi = 1
    vi = 11
    a = -10
    pf = pi + vi * t + 0.5 * a * t ** 2

    #print(pf)
    return pf


#ballistc1(0.5)
#ballistc1(1.0)

#y = ballistc1(0.5)
#print("f(0.5) is ", y)


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

    

def computeAndOutput(pi, vi, a, t):
    '''calculates the final position of an object in a ballistic trajectory when the user inputs initial position, 
    initial velocity, acceleration and time, and appends the results to a CSV file (mydata.csv), and print the results'''
    pf = ballistc2(pi, vi, a, t)

    fp = open( 'mydata.csv', 'a' )
    fp.write( str(t) + "," + str(pf) + "\n" )
    fp.close()
    print(t, ",", pf)


def trajectory10(pi, vi, a, ti):
    '''Computes and outputs the final positions of an object in a ballistic trajectory at ten different time intervals, 
    starting from a given initial time.'''
    for N in range(10):
        computeAndOutput(pi, vi, a, ti + N * 0.1)

#trajectory10(1, 11, -10, 0)
#trajectory10(1, 11, -10, 1)

def trajectory100(pi, vi, a, ti):
    '''Computes and outputs the final positions of an object in a ballistic trajectory at 100 different time intervals, 
    starting from a given initial time'''
    for i in range(10):
        trajectory10(pi, vi, a, ti)
        ti += 1

clearfile('mydata.csv')
#trajectory100(1, 50, -10, 0)


# Generates trajectories for Earth
#trajectory100(1, 50, -10, 0)

# Generates trajectories for Mars
#trajectory100(1, 50, -3.77, 0)

# Generates trajectories for Jupiter
trajectory100(1, 100, -23.6, 0)
