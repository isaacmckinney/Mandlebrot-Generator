import unittest
import sys
sys.path.append('./src/')
from PixelPlot import PixelPlot
from GraphConfig import GraphConfig



class TestPixelPlot(unittest.TestCase):

    def testCreatePointsList(self):
        g = GraphConfig( [-1, 1, -1, 1], [2, 2] )
        p = PixelPlot( g )
        self.assertEqual( p.createPointsList(), [[-1, 1], [-1, 0], [0, 1], [0, 0]], "simple 4 point object" )

if __name__ == '__main__':
    unittest.main()