#!/usr/bin/python3
import math

def getNextSmoothedGuess(oldGuess, newSample, alpha):
    return alpha * oldGuess + (1-alpha) * newSample

def sinDegrees(degrees):
    return math.sin(degrees * math.pi / 180)

def zeroSafePercentError(test, true):
    return 200 * abs((test - true) / (test + true))

alpha = 0.9
oldGuess = 0

for x in range(0, 720):
    newSample = sinDegrees(x)
    nextGuess = getNextSmoothedGuess(oldGuess, newSample, alpha)
    nextActual = sinDegrees(x+1)
    print('{} Error = {}%'.format(x, zeroSafePercentError(nextGuess, nextActual)))
    oldGuess = nextGuess
