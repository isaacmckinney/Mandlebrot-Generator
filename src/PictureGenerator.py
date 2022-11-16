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

    def generateCnums(self):
        newCnums = pp.PixelPlot(self.gconfig).createPointsList()
        self.cnums = newCnums

        return self.cnums
    
    def generateStabilityScores(self):
        newScores = StabilityChecker.checkStability(self.cnums, 2, self.gradientSize)
        self.stability = newScores

        return self.stability
    
    def generateStylizedArray(self):
        stylizedArray = np.zeros((len(self.stability), 4), dtype=np.uint8)
        for score in range(len(self.stability)):
            #if self.styleProfile.style[ self.stability[ score ] ][0] < 253:
                #print(self.styleProfile.style[ self.stability[ score ] ][0])
            stylizedArray[score, 0] = (np.uint8) (self.styleProfile.style[ self.stability[ score ] ][0])
            stylizedArray[score, 1] = (np.uint8) (self.styleProfile.style[ self.stability[ score ] ][1])
            stylizedArray[score, 2] = (np.uint8) (self.styleProfile.style[ self.stability[ score ] ][2])
            stylizedArray[score, 3] = (np.uint8) (self.styleProfile.style[ self.stability[ score ] ][3])

        stylizedArray = np.reshape( stylizedArray, (self.gconfig.x, self.gconfig.y, 4) )
        #stylizedArray = np.transpose(stylizedArray)
        self.stylizedArray = stylizedArray
        return stylizedArray
    
    def generatePictureFromStylizedArray(self, nameOfFile, saveStatus):
        im = Image.fromarray(self.stylizedArray, mode="RGBA")
        self.image = im
        #self.image.transpose(method=Image.FLIP_TOP_BOTTOM)
        self.image.show(title=nameOfFile)
        if saveStatus:
            self.image.save(nameOfFile + '.png')

        return self.image