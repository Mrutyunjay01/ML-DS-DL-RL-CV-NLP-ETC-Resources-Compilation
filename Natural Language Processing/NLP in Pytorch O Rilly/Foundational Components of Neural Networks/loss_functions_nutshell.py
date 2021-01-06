# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 19:58:32 2020

@author: MRUTYUNJAY BISWAL
"""

import torch
import torch.nn as nn

# mean squarred loss
mse_loss = nn.MSELoss()
outputs = torch.randn(3, 5, requires_grad=True)
targets = torch.randn(3, 5)

mloss = mse_loss(outputs, targets)
print(mloss)

# categorical cross entropy loss
cce_loss = nn.CrossEntropyLoss()
outputs_cce = torch.randn(3, 5, requires_grad=True)
targets_cce = torch.tensor([1, 0, 3], dtype=torch.int64)

cceLoss = cce_loss(outputs_cce, targets_cce)
print(cceLoss)

# binary cross entropy loss
bce_loss = nn.BCELoss()
sigmoid = nn.Sigmoid()

proba = sigmoid(torch.randn(4, 1, requires_grad=True))
targets_bce = torch.tensor([1, 0, 1, 0], dtype=torch.float32)

loss = bce_loss(proba, targets_bce)
print(proba)
print(loss)