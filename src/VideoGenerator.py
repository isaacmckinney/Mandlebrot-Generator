from GraphConfig import GraphConfig
from PictureGenerator import PictureGenerator
from GeometricSeries import GeometricSequence

import cv2
import numpy
import glob

class VideoGenerator:

    def __init__(self, bounds, resolution):
        self.bounds = bounds
        self.resolution = resolution
        self.g = GraphConfig(bounds, resolution)
    
    def generateConstantBoundsAnimation(self, colors, StabilityFactor, interpSteps):
        colorsToUse = colors.copy()
        p = PictureGenerator( self.g, 504 )
        p.generateCnums()
        p.generateStabilityScores(StabilityFactor)
        p.configInterpSequence( colorsToUse, interpSteps )
        print("Generating" + str(len(p.styleProfile.style)) + " Images")
        for i in range(len(p.styleProfile.style)):
            p.styleProfile.style = [p.styleProfile.style[-2]] + p.styleProfile.style[0:-2] + [p.styleProfile.style[-1]]

            p.generateStylizedArray()
            
            p.generatePictureFromStylizedArray("test" + str(i), True, False)
    
    def generateZoomAnimation(self, startingBounds, boundsToZoom, zoomSteps, colors, interpSteps):
        colorsToUse = colors.copy()
        ogBounds = startingBounds.copy()
        zoomBounds = boundsToZoom.copy()

        


        x1diff = ogBounds[0] - zoomBounds[0] 
        x2diff = ogBounds[1] - zoomBounds[1] 
        y1diff = ogBounds[2] - zoomBounds[2] 
        y2diff = ogBounds[3] - zoomBounds[3] 

        print("X1Diff: " + str(x1diff))
        print("X2Diff: " + str(x2diff))
        print("Y1Diff: " + str(y1diff))
        print("Y2Diff: " + str(y2diff))

        p = PictureGenerator( self.g, 504 )

        ## currently cuts length difference into a linear pattern
        ## need to change it to be non-linear, to get rid of the big jump at the end
        #for i in range(zoomSteps + 1):
        #    zb = [ogBounds[0] - ( x1diff * i ), ogBounds[1] - ( x2diff * i ), ogBounds[2] - ( y1diff * i ), ogBounds[3] - ( y2diff * i )]
        #    p.gconfig.setBounds(zb)
        #    p.generateCnums()
        #    p.generateStabilityScores(2)
        #    p.configInterpSequence(colors, interpSteps)
        #    print("Img " + str( i ) + ": " + str(zb))
        #    p.generateStylizedArray()
        #    p.generatePictureFromStylizedArray("test" + str( i ), True, False)
        
        
        x1Seq = GeometricSequence(x1diff, zoomSteps)
        x2Seq = GeometricSequence(x2diff, zoomSteps)
        y1Seq = GeometricSequence(y1diff, zoomSteps)
        y2Seq = GeometricSequence(y2diff, zoomSteps)
        print("x1: " + str(x1Seq.testSum()))
        print("x2: " + str(x2Seq.testSum()))
        print("y1: " + str(y1Seq.testSum()))
        print("y2: " + str(y2Seq.testSum()))
        for i in range(zoomSteps + 1):
            p.gconfig.setBounds( [ ogBounds[0] - x1Seq.getSumToN(i), ogBounds[1] - x2Seq.getSumToN(i), ogBounds[2] - y1Seq.getSumToN(i), ogBounds[3] - y2Seq.getSumToN(i) ] )
            p.generateCnums()
            p.generateStabilityScores(2)
            p.configInterpSequence(colors, interpSteps)
            print("Img " + str( i ))
            p.generateStylizedArray()
            p.generatePictureFromStylizedArray("test" + str( i ), True, False)


    def generateVideo(self, fps):
        imgs = []

        for j in range(100 + 1):
            img = cv2.imread('test' + str(j) + '.png')
            height, width, layers = img.shape
            size = (width,height)
            imgs.append(img)
        
        out = cv2.VideoWriter('mandle.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

        for i in range(len(imgs)):
            out.write(imgs[i])
        out.release()
