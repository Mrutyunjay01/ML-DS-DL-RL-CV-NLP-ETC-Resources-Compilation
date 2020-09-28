# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 00:43:08 2020

@author: MRUTYUNJAY BISWAL
"""
import numpy as np
import torch

def describe(x):
    """
    

    Parameters
    ----------
    x : tensor 

    Returns
    -------
    None.
    prints various methods of a tensor object in pytorch.
    """
    print(f"Size: {x.shape}")
    print(f'Type: {type(x)}')
    print(f'Value: {x}')
    pass

describe(torch.tensor([2, 3]))

# tensor from uniform distribution
describe(torch.rand(2, 3))

# tensor from normal distribution
describe(torch.randn(2, 3))

x = torch.zeros(2, 3)
describe(x)
x = torch.ones(2, 3)
describe(x)
x.fill_(5)
describe(x)

# creating a tensor object from a numpy array
npy = np.random.randn(3, 3)
x = torch.from_numpy(npy)
describe(x)