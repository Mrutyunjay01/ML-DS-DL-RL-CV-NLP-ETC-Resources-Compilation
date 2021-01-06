# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:18:55 2020

@author: MRUTYUNJAY BISWAL
"""
import numpy as np
import torch
import torch.optim as optimzers
import torch.nn as nn

from utils import get_toy_data
from simple_perceptron import Perceptron
# hyperlparameters
lr = 0.001
input_dim = 2

batch_size = 1000
n_epochs = 10
n_batches = 5

seed = 1337

# seed everything
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
np.random.seed(seed)

# instantiate the model
model = Perceptron(2)
# instantiate the optimizer
opt = optimzers.Adam(params=model.parameters(), lr=lr)
# instantitate the loss
loss = nn.BCELoss()

