

class GeometricSequence:

    def __init__(self, seqSum, num):
        self.seqSum = seqSum
        self.r = 11/12
        self.first = ( seqSum * ( 1 - (self.r) ) ) / ( 1 - ((self.r)**(num)) )
        self.num = num
        
        self.sequence = self.generateSequence()
        print(self.sequence)
    
    def generateSequence(self):

        seqToReturn = []
        seqToReturn.append(self.first)

    

        for i in range(1, self.num):
            
            newTerm = self.r * seqToReturn[i - 1]
            seqToReturn.append(newTerm)



        #self.sequence = seqToReturn
        return seqToReturn

    def testSum(self):
        if self.seqSum == self.getSumToN(self.num):
            return True
        else:
            print("Given Sum: " + str(self.seqSum))
            print("Calculated Sum: " + str(self.getSumToN(self.num)))
            return False


    def getSumToN(self, n):
        newSum = 0
        for i in range(n):
            newSum = newSum + self.sequence[i]
        return newSum
