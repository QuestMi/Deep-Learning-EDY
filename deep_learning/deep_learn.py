# -*- coding: utf-8 -*- 
"""
Create on : 2024/9/13
@Author   : Xiao QingLin 
@File    : deep_learn  
"""

import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    return np.array(x > 0, dtype=int)
if __name__ == '__main__':
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()

def relu(x):
    return np.maximum(x, 0)

if __name__ == '__main__':
    pass
