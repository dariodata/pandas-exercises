#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:18:08 2016

@author: arcosdid
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

#%% Read the file to a Dataframe
df = pd.read_excel('gruposinvestigacion.xlsx', sheetname=0, index_col=None)
df['count'] = pd.DataFrame(np.ones(3970,))

#%%
plt.figure(figsize=(10,10))

plt.subplot(2, 2, 1)
df.groupby('nombredpto').nombregrupo.nunique().sort_values().plot(kind='barh')

plt.subplot(2, 2, 2)
df.groupby('nombredpto').entidadesavalan.nunique().sort_values().plot(kind='barh')

plt.subplot(2, 2, 3)
df.loc[df['nombregranareaconocimiento'] == 'Ciencias Naturales'].groupby('nombreareaconocimiento').nombregrupo.nunique().sort_values().plot(kind='barh')

plt.subplot(2, 2, 4)
df.loc[df['nombregranareaconocimiento'] == 'Ciencias Naturales'].groupby('nombreareaconocimiento').nombregrupo.nunique().sort_values().plot(kind='barh')

plt.tight_layout()
plt.show()

#%% Pivot table
df.pivot_table(values='precio', index='departamento', columns=['ninosvacunados1','ninosvacunados2','ninosvacunados3','ninosvacunados4','ninosvacunados5','ninosvacunados6','ninosvacunados7','ninosvacunados8','ninosvacunados9','ninosvacunados10','ninosvacunados11','ninosvacunados12'])
df.pivot_table(values='precio', index='bandera', columns='producto').plot(kind='barh',cmap='gnuplot', figsize=(5,10))
plt.legend(loc='center left', fontsize=8, bbox_to_anchor=(1, 0.5))
plt.show()


#%%
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz','foo', 'foo', 'qux', 'qux'],['one', 'two', 'one', 'two','one', 'two', 'one', 'two']]))
 
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.rand(8, 2), index=index, columns=['A', 'B'])
df2 = df[:4]
df2

t=df2.unstack(level=0)
plt.plot(t[[0]], color='red')
plt.plot(t[[1]], color='blue')
plt.xticks(range(2), ['one','two'], size='small')

plt.show()