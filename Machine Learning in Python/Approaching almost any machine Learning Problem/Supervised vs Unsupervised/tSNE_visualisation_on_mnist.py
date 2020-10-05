# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 19:21:35 2020

@author: MRUTYUNJAY BISWAL
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import manifold

pixel_values, targets = datasets.fetch_openml('mnist_784',
                                              version=1,
                                              return_X_y=True)

# targets are of type 'object'
# convert into int type
targets = targets.astype('int')

single_image = pixel_values[1, :].reshape(28, 28)
plt.imshow(single_image, cmap='gray')

tsne = manifold.TSNE(n_components=2,
                     random_state=42)

transformed_data = tsne.fit_transform(pixel_values[:3000])

# for visualisation purposes, convert this type of data into a dataframe
tsne_df = pd.DataFrame(
        np.column_stack((transformed_data, targets[:3000])),
        columns=['component1', 'component2', 'targets']
    )

tsne_df.loc[:, 'targets'] = tsne_df.targets.astype('int')

grid = sns.FacetGrid(tsne_df,
                     hue='targets',
                     size=8)

grid.map(plt.scatter, 'component1', 'component2').add_legend()