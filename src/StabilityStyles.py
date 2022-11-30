import numpy as np


class StabilityStyle:

    def __init__(self, depth):
        self.style = None
        self.depth = depth
    
    ## input: [c0, c1, c2, ...]
    ## output: [c0, c1, c2, c0, c1, c2]
    def generateRepeatedPattern(self, pattern, steps):
        newStyle = []

        i = 0

        while i < self.depth:

            for c in range(len(pattern)):
                newStyle[i] = pattern[c]
                #newStyle[i][3] = (np.uint8)( 255 - (i * ( 255 / steps ) ) )
                i = i + 1
        
        self.style = newStyle
        return newStyle

    ## input: c0, c1, c2, c3, ....
    ## output: {c0 -interp-> c1, c1 -interp-> c2, ...}
    def generateInterpolationSequence(self, colors, steps):

        newStyle = [None]*(self.depth + 1)
        styleScoreTracker = 0

        fullColorList = []

        for c in range(len(colors)):

            r1 = colors[c][0]
            g1 = colors[c][1]
            b1 = colors[c][2]
            a1 = colors[c][3]
            
            r2 = 0
            g2 = 0
            b2 = 0
            a2 = 0

            if c == len(colors) - 1:
                r2 = colors[0][0]
                g2 = colors[0][1]
                b2 = colors[0][2]
                a2 = colors[0][3]
                
            else:
                r2 = colors[c + 1][0]
                g2 = colors[c + 1][1]
                b2 = colors[c + 1][2]
                a2 = colors[c + 1][3]
        
            rDelta = r1 - r2
            gDelta = g1 - g2
            bDelta = b1 - b2
            aDelta = a1 - a2

            rDeriv = rDelta / steps
            gDeriv = gDelta / steps
            bDeriv = bDelta / steps
            aDeriv = aDelta / steps


            for step in range(steps):
                fullColorList.append([round( r1 - (step * rDeriv) ), round( g1 - (step * gDeriv) ), round( b1 - (step * bDeriv) ), round( a1 - (step * aDeriv) )])
            
        i = 0
        while i <= self.depth :
            for c in range(len(fullColorList)):
                if i <= self.depth:
                    #print("Setting index: " + str(i))
                    newStyle[i] = fullColorList[c]
                    i = i + 1
                
        
        #newStyle[0] = [0, 0, 0, 0]
        #newStyle[1] = [0, 0, 0, 0]
        
        newStyle[self.depth] = [0, 0, 0, 0]

        self.style = newStyle
        return newStyle




    ## input: c0, c1
    ## output: { c0 -interp-> c1, c0 -interp-> c1, c0 -interp-> c1, ... }
    def generateRepeatedInterpolation(self, color1, color2, steps):

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

        newStyle = []

        cs = []

        i = 0

        for step in range(steps):
            cs.append([round( r1 - (step * rDeriv) ), round( g1 - (step * gDeriv) ), round( b1 - (step * bDeriv) ), round( a1 - (step * aDeriv) )])

        while i < 500:
            for c in range(len(cs)):
                newStyle[i] = cs[c]
                i = i + 1
            for v in range(len(cs) - 2):
                newStyle[i] = cs[ ( len(cs) - 2 ) - v ]
                i = i + 1
        newStyle[0] = [0, 0, 0, 0]
        newStyle[1] = [0, 0, 0, 0]
        newStyle[self.depth] = [0, 0, 0, 0]
        self.style = newStyle
        return newStyle

        


    ## input: c0, c1
    ## output: full object interp from c0 to c1
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

        newStyle = []

        for i in range(steps):
            newStyle[i + 1] = [round( r1 - (i * rDeriv) ), round( g1 - (i * gDeriv) ), round( b1 - (i * bDeriv) ), round( a1 - (i * aDeriv) )]
        
        self.style = newStyle
        return newStyle