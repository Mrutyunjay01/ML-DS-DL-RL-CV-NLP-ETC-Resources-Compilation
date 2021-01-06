# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:56:39 2020

@author: MRUTYUNJAY BISWAL
"""

import numpy as np
import matplotlib.pyplot as plt
import torch

def get_toy_data(batch_size, left_center=(3, 3), right_center=(3, -2)):
    x_data = []
    y_targets = np.zeros(batch_size)
    
    for batch in range(batch_size):
        
        if np.random.random() > 0.5:
            x_data.append(np.random.normal(loc=left_center))
            
        else:
            x_data.append(np.random.normal(loc=right_center))
            y_targets[batch] = 1
            
    return torch.tensor(x_data, dtype=torch.float32), torch.tensor(y_targets, dtype=torch.float32)

    pass

def visualize_result(model, x, y,
                     n_samples=1000, ax=None, epoch=None,
                     title='', levels=[0.3, 0.4, 0.5], linestyles=['--', '-', '--']):
    
    y_pred = model(x)
    y_pred = (y_pred > 0.5).long().data.numpy().astype(np.int32)

    x_data = x.data.numpy()
    y_true = y.data.numpy().astype(np.int32)
    
    n_classes = 2
    
    all_x = [[] for _ in range(n_classes)]
    all_colors = [[] for _ in range(n_classes)]
    
    colors = ['red', 'lime']
    marker = '*'
    
    for x_i, y_pred_i, y_true_i in zip(x_data, y_pred, y_true):
        all_x[y_true_i].append(x_i)
        
        if y_pred_i == y_true_i:
            all_colors[y_true_i].append(colors[y_true_i])
        else:
            all_colors[y_true_i].append(colors[not y_true_i])
            
    all_x = [np.stack(x_list) for x_list in all_x]
    
    if ax is None:
        _, ax = plt.subplots(1, 1, figsize=(10, 10))
        
    for x_list, color_list in zip(all_x, all_colors):
        ax.scatter(x_list[:, 0], x_list[:, 1],
                   edgecolor='black',
                   marker=marker,
                   facecolor=color_list, s= 300)
        
    x_lim = (min([x_list[:, 0].min() for x_list in all_x]),
             max([x_list[:, 0].max() for x_list in all_x]))
    y_lim = (min([x_list[:, 1].min() for x_list in all_x]),
             max([x_list[:, 1].max() for x_list in all_x]))  
    
    
    xx = np.linspace(x_lim[0], x_lim[1], 30)
    yy = np.linspace(y_lim[0], y_lim[1], 30)
    
    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    
    Z = model(torch.tensor(xy, ))
    pass

if __name__=="__main__":
    
    seed = 1337
    
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    
    x_data, y_label = get_toy_data(batch_size=1000)
    
    x_data = x_data.data.numpy()
    y_label = y_label.data.numpy()
    
    left_x, right_x = [], []
    left_colors, right_colors = [], []
    
    for x_i, y_i in zip(x_data, y_label):
        
        if y_i == 0:
            left_x.append(x_i)
            left_colors.append('red')
            
        else:
            right_x.append(x_i)
            right_colors.append('lime')
            
    left_x = np.stack(left_x)
    right_x = np.stack(right_x)
    
    _, ax = plt.subplots(1, 1, figsize=(10, 4))
    
    ax.scatter(left_x[:, 0], left_x[:, 1], color=left_colors, marker='*', s=100)
    ax.scatter(right_x[:, 0], right_x[:, 1], color=right_colors, marker='*', s=100)
    plt.axis('off')
    pass