# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: 
#
# Date:
# 
##################################################
#
# Sample Script for Midterm Examination: 
# Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for another script that would
# execute the scripts (to run the doctests)
# and imports the modules to test the functions.
##################################################
##################################################
"""






##################################################
# Import Required Modules
##################################################

# import name_of_module
import math
import numpy as np
from typing import List



##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------
def logit(x: float, beta_0: float, beta_1: float) -> float:
    """Calculates the value of the logit link function
     for a variable x and coefficients beta_0 and beta_1.
    >>> logit(13.7, 0.0, 0.0)
    0.5
    >>> logit(0.0, math.log(2), 2.0)
    0.6666666666666666
    >>> logit(1.0, 0.0, math.log(5))
    0.8333333333333333
    """
    link = math.exp(beta_0 + x*beta_1)/(1 + math.exp(beta_0 + x*beta_1))

    return link

def logit_like(y: int, x: float, beta_0: float, beta_1: float) -> float:
    """Calculates the value of the likelihood function
    for one observation of x and y.

    >>> logit_like(1, 13.7, 0.0, 0.0)
    -0.6931471805599453
    >>> logit_like(0, 0.0, math.log(2), 2.0)
    -1.0986122886681096
    >>> logit_like(1, 1.0, 0.0, math.log(5))
    -0.1823215567939547
    """
    link = logit(x, beta_0, beta_1)
    if y == 0:
        like = math.log(1 - link)
    elif y == 1:
        like = math.log(link)
    else:
        print("Warning: y is not binary. y should be either 1 or 0.")
        like = None

    return like


def logit_like_sum(y: list, x: list, beta_0: float, beta_1: float) -> float:
    """Calculates the value of the likelihood function
    for the bivariate logistic regression model
    for multiple pairs of observations in the lists x and y
    and coefficients beta_0 and beta_1.
    
    >>> logit_like_sum([1, 1, 1], [13.7, 12, 437], 0.0, 0.0)
    -2.0794415416798357
    >>> logit_like_sum([1, 0], [1, 1], 0.0, math.log(2))
    -1.504077396776274
    >>> logit_like_sum([1, 0], [2, 3], math.log(5), math.log(2))
    -3.762362230873739
    """
    
    like_sum = 0
    for i in range(len(y)):
        if y[i] in [0,1]:
            like_sum_i = logit_like(y[i], x[i], beta_0, beta_1)
            like_sum = like_sum + like_sum_i
        else:
            print('Error: Observations in y must be either zero or one.')
            return None
        
    
    return like_sum




#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------


# Exercise 6


def max_logit(y: List[float], x: List[float], 
        beta_0_min: float, beta_0_max: float, 
        beta_1_min: float, beta_1_max: float, 
        step: float) -> float:
    """
    Calculates the estimated coefficients 
    by grid search on the value of the logit_like_sum function
    for the logistic regesssion model 
    given two lists of data y and x.
    
    The search is taken over a grid of candidate values
    of beta_0 and beta_1 defined over
    np.arange(beta_0_min, beta_0_max, step) and
    np.arange(beta_1_min, beta_1_max, step), respectively.
    
    
    >>> max_logit([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], \
                  -2.0, 2.0, -2.0, 2.0, 0.10)
    [0.0, 0.0]
    >>> max_logit([1, 0, 1], [15.0, 10.0, 5.0], \
                  -1.0, 1.0, -1.0, 1.0, 0.01)
    [0.69, 0.0]
    >>> max_logit([1, 0, 1, 0, 1], [0, 0, 1, 1, 1], \
                  -1.0, 1.0, -1.0, 1.0, 0.01)
    [0.0, 0.69]
    """
    
    # Code goes here.
    
    beta_0_list = np.arange(beta_0_min, beta_0_max, step)
    beta_1_list = np.arange(beta_1_min, beta_1_max, step)
    max_logit_sum = float("-inf")
    i_max = None
    j_max = None
    for i in range(len(beta_0_list)):
        for j in range(len(beta_1_list)):
            beta_0 = beta_0_list[i]
            beta_1 = beta_1_list[j]
            logit_sum_ij = logit_like_sum(y, x, beta_0, beta_1)
            if logit_sum_ij > max_logit_sum:
                max_logit_sum = logit_sum_ij
                i_max = i
                j_max = j                
    if (i_max is not None and j_max is not None):
        return [beta_0_list[i_max], beta_1_list[j_max]]
    else:
        print("No value of logit_like_sum was higher than the initial value.")
        print("Choose different values of the parameters for beta_0 and beta_1.")
    return None




# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

# Make sure to include examples in your docstrings
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# The tests are implemented below -- but only
# when the script is run, not when it is imported. 







##################################################
# End
##################################################
