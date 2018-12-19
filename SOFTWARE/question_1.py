#Mohamed Ameen Omar
#16055323
####################################
###      EDC 310 Practical 1     ###
###             2018             ###
###          Question 1          ###
####################################

import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
from scipy.stats import norm

############ Random Number Class #####################
# The random number class contains the two random number generators
class randomNumber:
    #Constructor
    def __init__(self, seed1 = time.time(), seed2 = time.time()-10, seed3 = time.time()+10):
        self.seed1 = seed1
        self.seed2 = seed2
        self.seed3 = seed3
        self.computed = None

    #Uniform Distribution Wichmann-Hill algorithm
    def WHill(self):
        # Seed values must be greater than zero 

        self.seed1 = 171 * (self.seed1 % 177) - (2*(self.seed1/177))
        if self.seed1 < 0:
            self.seed1 = self.seed1 + 30269

        self.seed2 = 172 * (self.seed2 % 176) - (35*(self.seed2/176))
        if self.seed2 < 0:
            self.seed2 = self.seed2 + 30307

        self.seed3 = 170 * (self.seed3 % 178) - (63*(self.seed2/178))
        if self.seed3 < 0:
            self.seed3 = self.seed3 + 30323

        temp = float(self.seed1/30269) + float(self.seed2/30307) + float(self.seed3/30323)
        # So that the output is between 0 and 1
        return (temp%1) 

    # Normal Distribituion random number generator.
    # Only used in Question 2 and Question 3. 
    def gaussian(self, mean = 0, stdDeviation = 1):
        if(self.computed is not None):
            returnVal = self.computed
            self.computed = None
            return returnVal
        else:            
            squaredSum = -1.0
            temp1 = 0.0
            temp2 = 0.0
            # find two numbers such that their squared sum falls within the 
            # boundaries of the square. 
            while( (squaredSum >= 1) or squaredSum == -1.0 ):
                temp1 = (2*self.WHill())-1
                temp2 = (2*self.WHill())-1
                squaredSum = (temp1**2) + (temp2 **2)

            mul = np.sqrt(-2.0*np.log(squaredSum)/squaredSum)

            #store the second point to avoid wasting computation time
            self.computed = mean + (stdDeviation * temp1 * mul)
            return (mean + (stdDeviation*temp2*mul))

################## End of class ###########################
    
# function to plot the PDF for the Uniformly distributed random number generator
def plotUniformPDF(sample = None, binSize = 200, save = True, iswHill = True):
    if(sample is None):
        print("Error, sample to plot not provided")
        return
    
    title = ("Probability Density Function of the ")
    # if the sample passed in was generated from the Wichmann-Hill algorithm
    if(iswHill is True):
        title = title + "Wichmann-Hill Random Number Generator"
    # if the sample passed in was generated from the python uniform random number generator
    else:
        title = title + "Python Uniform Random Number Generator"
    fileName = title
    title = title + " with a sample size of " + str(len(sample)) + " and a bin size of " + str(binSize) + " bins"
    fig = plt.figure()
    plt.hist(sample,color = "Blue", edgecolor = "black", bins = binSize, density = True)
    plt.xlabel("Random Number")
    plt.ylabel("Probability")
    plt.title(title)
    #Plot a real Uniform PDF for comparison
    plt.plot([0.0, 1.0], [1,1],'r-', lw=2, label='Actual Uniform PDF')
    plt.legend(loc='best')
    plt.show()

    #to save the plot 
    if(save is True):
        fileName = fileName + ".png"
        fig.savefig(fileName , dpi=fig.dpi)

# function to print the relevant statistics for the sample passed in
# The mean, standard deviation and variance of the sample is computed
# and displayed to the screen 
def printStats(sample = None, isWHill = True):
    if(sample is None):
        print("Error, sample not provided, no statistics to print")
        return
    message = ("The Mean, Standard Deviation and Variance for the ")
    if(isWHill is True):
        message = message + "Wichmann-Hill Uniformly Distributed Random Number Generator"
    else:
        message = message + "Built-in Python Uniformly Distributed Random Number Generator"
    print(message)
    print("Mean: " + str(np.mean(sample)))
    print("Standard Deviation: " + str(np.std(sample)))
    print("Variance: " + str(np.var(sample)))


def question1(sampleSize = 10000000, binSize = 200, save = True):
    #input parameter validation
    #all paramters must have a postive value
    if(sampleSize < 0):
        sampleSize = 10000000
    if(binSize < 0):
        binSize = 200
    #create a randomGenerator object to get Uniform distribution random numbers
    # For consistent results, pass seed paramters into the constructor
    randomGenerator = randomNumber() #create a random number object to generate uniform random number 
    sampleSpace = []
    
    print("Question 1:")

    #Generate Sample Space for Wichmann-Hill
    print("Generating Sample Space with Wichmann-Hill RNG")
    print("Sample space contains", sampleSize, "entries")
    print("The bin size is", binSize, "bins")
    for x in range(0, sampleSize):
        sampleSpace.append(randomGenerator.WHill())
    print("Task Complete")

    print("Plotting Wichmann-Hill PDF")
    plotUniformPDF(sampleSpace, binSize, save, True)
    print()
    printStats(sampleSpace, True)
    print()

    print("---------------------------------------")
    print("Generating Sample Space with Python RNG")
    print("Sample space contains", sampleSize, "entries")
    print("The bin size is", binSize, "bins")
    sampleSpace = np.random.uniform(size = sampleSize)
    print("Task Complete")

    print("Plotting Python RNG PDF")
    plotUniformPDF(sampleSpace, binSize, save, False)
    print()    
    printStats(sampleSpace, False)

# adjust parameters at will
# Sample size = First Parameter
# Bin size = Second Parameter
# boolean to save the plots = Third Paramter

# Uncomment next line to run
#question1(1000000,250,save = False)
