import numpy as np


class StabilityStyle:

    def __init__(self):
        self.style = None
    
    def generateRepeatedPattern(self, pattern, steps):
        newStyle = {}

        i = 0

        while i < 500:

            for c in range(len(pattern)):
                newStyle[i] = pattern[c]
                #newStyle[i][3] = (np.uint8)( 255 - (i * ( 255 / steps ) ) )
                i = i + 1
        
        self.style = newStyle
        return newStyle




    def generateInterpolatedStyle(self, color1, color2, steps):

        r1 = color1[0]
        g1 = color1[1]
        b1 = color1[2]
        a1 = color1[3]
        
        r2 = color2[0]
        g2 = color2[1]
        b2 = color2[2]
        a2 = color2[3]
    
        rDelta = r1 - r2
        gDelta = g1 - g2
        bDelta = b1 - b2
        aDelta = a1 - a2

        rDeriv = rDelta / steps
        gDeriv = gDelta / steps
        bDeriv = bDelta / steps
        aDeriv = aDelta / steps

        newStyle = {}

        for i in range(steps):
            newStyle[i + 1] = [round( r1 - (i * rDeriv) ), round( g1 - (i * gDeriv) ), round( b1 - (i * bDeriv) ), round( a1 - (i * aDeriv) )]
        
        self.style = newStyle
        return newStyle