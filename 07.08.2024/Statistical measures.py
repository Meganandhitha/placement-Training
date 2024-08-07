import numpy as np
a=np.array([[0,1,2],
            [3,4,5]])
print("Original array:",a)            
print("Mean:",np.mean(a,axis=1))
print("Standard deviation:",np.std(a,axis=1))
print("Variance:",np.var(a,axis=1))
