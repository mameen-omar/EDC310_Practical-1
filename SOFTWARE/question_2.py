#Mohamed Ameen Omar
#16055323
####################################
###      EDC 310 Practical 1     ###
###             2018             ###
###         Question 2           ###
####################################

import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
from scipy.stats import norm
from question_1 import randomNumber


# Ensure that the source file question_1.py is in the current dorectory
# before running the script
# Refer to question_1.py for the parameters of the random number generator

def question2(sampleSize=10000000, binSize=200, save=True):
    # input parameter validation
    # all paramters must have a postive value
    if(sampleSize < 0):
        print("Sample size set to 10000000 entries")
        sampleSize = 10000000
    if(binSize < 0):
        print("Bin Size set to 200 bins")
        binSize = 200
    # create a randomGenerator object to get random numbers
    # For consistent results, pass seed paramters into the constructor
    randomGenerator = randomNumber()
    # list to store the values generated
    sampleSpace = [] 

    #Generate Sample Space
    print("Question 2")
    print("Generating Sample Space with Gaussian Random Number Generator")
    print("Sample space contains",sampleSize, "entries")
    print("The bin size is",binSize, "bins")
    for x in range(0, sampleSize):
        # adjust gaussian function paramters for differing outputs
        sampleSpace.append(randomGenerator.gaussian())
    print("Done")
    print()
    
    # Plot the PDF
    title = ("Probability Density Function of the Gaussian Random Number Generator")
    title = title + " with a sample size of " + str(sampleSize) + " and a bin size of " + str(binSize) + " bins"
    print("Plotting the Gaussian Random Number Generator PDF")  
    plt.hist(sampleSpace, color="Blue", edgecolor="black", bins=binSize, density=True)
    plt.ylabel("Probability")
    plt.xlabel("Random Number")
    x = np.linspace(norm.ppf(0.000000001), norm.ppf(0.999999999), binSize)
    plt.plot(x, norm.pdf(x), 'r-', lw=2, alpha=0.6, label='Actual Normally Distributed PDF with sd = 1, mean = 0')
    plt.legend(loc='best')
    plt.title(title)
    plt.show()
    print("Complete")
    print()

    # The mean, standard deviation and variance of the sample is computed
    # and displayed to the screen
    print("The Mean, Standard Deviation and Variance for the Gaussian Normally Distirbitued Random Number Generator")
    print("Mean =",np.mean(sampleSpace))
    print("Standard Deviation =", np.std(sampleSpace))
    print("Variance =",np.var(sampleSpace))

#adjust parameters at will
# Sample size = First Parameter
# Bin size = Second Parameter
# boolean to save the plots in the current directory= Third Paramter
# uncomment next line to run
#question2(10000000, 200, save = False)
