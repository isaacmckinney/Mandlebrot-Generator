import numpy as np
import PixelPlotter as pp
import StabilityChecker
from PIL import Image
from StabilityStyles import StabilityStyle

class PictureGenerator:

    def __init__(self, gconfig, gradientSize):
        # GraphConfig object, see GraphConfig.py { may be on branch, ' create-graph ' }
        self.gconfig = gconfig
        self.gradientSize = gradientSize
        self.styleProfile = None
        self.cnums = None
        self.stability = None
        self.stylizedArray = None
        self.image = None
    
    def configInterp(self, color1, color2):
        
        self.styleProfile = StabilityStyle()
        self.styleProfile.generateInterpolatedStyle(color1, color2, self.gradientSize)
        
        return self.styleProfile

    def configRepeatedPattern(self, pattern):
        self.styleProfile = StabilityStyle()
        self.styleProfile.generateRepeatedPattern(pattern, self.gradientSize)
        return self.styleProfile

    def configRepeatedInterp(self, color1, color2, steps):
        self.styleProfile = StabilityStyle(self.gradientSize)
        self.styleProfile.generateRepeatedInterpolation(color1, color2, steps)
        return self.styleProfile

    def configInterpSequence(self, colorsToUse, steps):
        self.styleProfile = StabilityStyle(self.gradientSize)
        
        self.styleProfile.generateInterpolationSequence(colorsToUse, steps)
        return self.styleProfile

    def generateCnums(self):
        newCnums = pp.PixelPlot(self.gconfig).createPointsList()
        self.cnums = newCnums

        return self.cnums
    
    def generateStabilityScores(self, factor):
        newScores = StabilityChecker.checkStability(self.cnums, factor, self.gradientSize)
        self.stability = newScores

        return self.stability
    
    def generateStylizedArray(self):
        stylizedArray = np.zeros((self.gconfig.y, self.gconfig.x, 4), dtype=np.uint8)

        stabCounter = 0

        for row in range(self.gconfig.x):

            for px in range(self.gconfig.y):
                #print(stabCounter)
                #print(self.stability[ stabCounter ])
                #print(self.styleProfile.style[ self.stability[ stabCounter ] ])
                stylizedArray[px, row, 0] = (np.uint8) (self.styleProfile.style[ self.stability[ stabCounter ] ][0])
                stylizedArray[px, row, 1] = (np.uint8) (self.styleProfile.style[ self.stability[ stabCounter ] ][1])
                stylizedArray[px, row, 2] = (np.uint8) (self.styleProfile.style[ self.stability[ stabCounter ] ][2])
                stylizedArray[px, row, 3] = (np.uint8) (self.styleProfile.style[ self.stability[ stabCounter ] ][3])

                stabCounter = stabCounter + 1


        self.stylizedArray = stylizedArray
        return stylizedArray
    
    def generatePictureFromStylizedArray(self, nameOfFile, saveStatus, showStatus):
        im = Image.fromarray(self.stylizedArray, mode="RGBA")
        self.image = im
        #self.image.transpose(method=Image.FLIP_TOP_BOTTOM)
        if showStatus:
            self.image.show(title=nameOfFile)
        if saveStatus:
            self.image.save(nameOfFile + '.png')

        return self.image
    
    def setScores(self, newScores):
        self.stability = newScores
        return self.stability