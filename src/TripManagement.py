import os
import numpy as np

from PictureGenerator import PictureGenerator
from GraphConfig import GraphConfig

class User:

    def __init__(self):
        self.shot_titles = np.empty(0, dtype=str)
        self.shots = np.empty(0, dtype=Shot)
    
    def loadShotManifest(self):
        shotmani = np.load('./projects/pmani.npy', allow_pickle=True)
        self.shot_titles = np.empty(len(shotmani), dtype=str)
        self.shots = np.empty(len(shotmani), dtype=Shot)
        for i in range(len(shotmani)):
            self.shot_titles[i] = shotmani[i]
            print('importing project titled \'' + str(shotmani[i]) + '\'')
            self.shots[i] = Shot(shotmani[i])
            self.shots[i].loadShotData()

    def createNewShot(self, name):
        self.shot_titles = np.append(self.shot_titles, name)
        self.shots = np.append(self.shots, Shot(name))

        np.save('./projects/pmani.npy', self.shot_titles, allow_pickle=True)
    
    def getShot(self, index):
        return self.shots[index]

    def checkForProjectManifest(self):
        if not os.path.isfile('./projects/pmani.npy'):
            print('No project manifest detected. ')
            self.shot_titles = np.empty(0, dtype=str)
            np.save('./projects/pmani.npy', self.shot_titles, allow_pickle=True)
            print("created new project manifest. ")
        else:
            self.shot_titles = np.load('./projects/pmani.npy', allow_pickle=True)

    def makePictureFromShot(self, index):
        self.shots[index].generatePicture()



class Shot:

    def __init__(self, name):
        self.name = name
        self.p = None
        self.createShotDirectory()
        #self.picgen = PictureGenerator(GraphConfig([-8, 8, -4.5, 4.5], [1920, 1080]))
    
    def setBounds(self, newBounds):
        self.shotbounds = newBounds
        np.save('./projects/' + str(self.name) + '/' + str(self.name) + '-bounds.npy', self.shotbounds, allow_pickle=True)
        #self.p.gconfig.bounds.setBorder(self.shotbounds)
        return self.shotbounds

    def setReso(self, newReso):
        self.shotreso = newReso
        np.save('./projects/' + str(self.name) + '/' + str(self.name) + '-reso.npy', self.shotreso, allow_pickle=True)
        return self.shotreso
    
    def setDepth(self, newDepth):
        self.shotdepth = newDepth
        np.save('./projects/' + str(self.name) + '/' + str(self.name) + '-depth.npy', self.shotdepth, allow_pickle=True)
        return self.shotdepth
    
    def setFactor(self, newFactor):
        self.shotfactor = newFactor
        np.save('./projects/' + str(self.name) + '/' + str(self.name) + '-factor.npy', self.shotfactor, allow_pickle=True)
        return self.shotfactor
    
    def setMat(self, newMat):
        self.shotmat = newMat
        np.save('./projects/' + str(self.name) + '/' + str(self.name) + '-mat.npy', self.shotmat, allow_pickle=True)
        return self.shotmat

    def setColors(self, newColors):
        self.colors = newColors
        np.save('./projects/' + str(self.name) + '/' + str(self.name) + '-colors.npy', self.colors, allow_pickle=True)
        return self.colors
    
    def setGradientSteps(self, newGradientSteps):
        self.gradientSteps = newGradientSteps
        np.save('./projects/' + str(self.name) + '/' + str(self.name) + '-gradientSteps.npy', self.gradientSteps, allow_pickle=True)
        return self.gradientSteps

    def loadShotData(self):
        self.loadBoundsData()
        self.loadResoData()
        self.loadDepthData()
        self.loadFactorData()
        self.loadMatData()
        if os.path.isfile('./projects/' + str(self.name) + '/' + str(self.name) + '-colors.npy'):
            print("importing color scheme for " + str(self.name))
            self.loadColorsData()
            self.loadGradientStepsData()
            self.configColorScheme()

    def loadBoundsData(self):
        self.shotbounds = np.load('./projects/' + str(self.name) + '/' + str(self.name) + '-bounds.npy', allow_pickle=True)
        return self.shotbounds

    def loadResoData(self):
        self.shotreso = np.load('./projects/' + str(self.name) + '/' + str(self.name) + '-reso.npy', allow_pickle=True)
        return self.shotreso

    def loadDepthData(self):
        self.shotdepth = np.load('./projects/' + str(self.name) + '/' + str(self.name) + '-depth.npy', allow_pickle=True)
        return self.shotdepth

    def loadFactorData(self):
        self.shotfactor = np.load('./projects/' + str(self.name) + '/' + str(self.name) + '-factor.npy', allow_pickle=True)
        return self.shotfactor

    def loadMatData(self):
        self.setMat( np.load('./projects/' + str(self.name) + '/' + str(self.name) + '-mat.npy', allow_pickle=True) )
        if self.p != None:
            self.p.setScores(self.shotmat)
        else:
            self.p = PictureGenerator(GraphConfig(self.shotbounds, self.shotreso), self.shotdepth)
            self.p.setScores(self.shotmat)
        return self.shotmat

    def loadColorsData(self):
        self.setColors( np.load('./projects/' + str(self.name) + '/' + str(self.name) + '-colors.npy', allow_pickle=True) )
        return self.colors

    def loadGradientStepsData(self):
        self.setGradientSteps( np.load('./projects/' + str(self.name) + '/' + str(self.name) + '-gradientSteps.npy', allow_pickle=True) )
        return self.gradientSteps

    def generateStabMat(self):
        self.p = PictureGenerator(GraphConfig(self.shotbounds, self.shotreso), self.shotdepth)
        self.p.generateCnums()

        self.setMat(self.p.generateStabilityScores(self.shotfactor))

    def configColorScheme(self):
        if self.p != None:
            self.p.configInterpSequence(self.colors, self.gradientSteps)
        else:
            self.p = PictureGenerator(GraphConfig(self.shotbounds, self.shotreso), self.shotdepth)
            self.p.configInterpSequence(self.colors, self.gradientSteps)
            
    def generatePicture(self):
        self.p.generateStylizedArray()
        self.p.generatePictureFromStylizedArray('./projects/' + str(self.name) + '/' + str(self.name), True, False)

    def createShotDirectory(self):
        if not os.path.exists('./projects/' + str(self.name) + '/'):
            os.makedirs('./projects/' + str(self.name) + '/')
