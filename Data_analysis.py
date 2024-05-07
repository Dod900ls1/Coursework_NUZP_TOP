"""
Here I would do stats
"""
from scipy.stats import f_oneway
from scipy.stats import tukey_hsd


"""
What means do we compare with ANOVA?

We want to create a mean execution time for what? 

For different optimization methods. But I wonder if there is a problem with just doing anova on average execution time
in general. What I might do instead, is to separate dataset into polynomials, exponential and logarithmic functions.
And test the average execution time of those 3.

After a while, I realized that it is noncense, and I would just compare their means.

6 optimization methods - do anova. Then do turkish HDS.

But first we need to check assumptions what needed
"""


print(f_oneway([1,2,3,4,5], [1,2,3,4,5]))














