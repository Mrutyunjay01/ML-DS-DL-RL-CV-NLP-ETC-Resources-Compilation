# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 19:35:20 2020

@author: MRUTYUNJAY BISWAL
"""

import torch
import torch.nn as nn

class Perceptron(nn.Module):
    
    """ A perceptron is one linear layer! """
    def __init__(self, input_dim):
        """
        

        Parameters
        ----------
        input_dim : int
            Size of the input features.

        Returns
        -------
        None.

        """
        super(Perceptron, self).__init__()
        self.fc1 = nn.Linear(input_dim, 1)
        
    def forward(self, x_in):
        """
        The forward pass of the perceptron.

        Parameters
        ----------
        x_in : (torch.tensor): an input data tensor
            x_in.shape should be (batch, num_features)

        Returns
        -------
        the resulting tensor of shape (batch, )
        """
        return torch.sigmoid(self.fc1(x_in)).squeeze()
    pass
