#%matplotlib inline

import pandas
import random

import matplotlib
import numpy
import matplotlib.pyplot as plt

ntries = 50
#throws = 25

experiments = [387.7,
387.7,
388.4,
387,
388.2,
388.1,
389,
388.6,
387.5,
387.8,
387.6,
387.8,
386.9,
387.7,
388.5,
387.9,
387.4,
388,
388.3,
389.9,
387.4,
389.1,
388.5,
387.1,
387.8,
389,
388.4,
387.5,
388.9,
388,
388.6,
386.6,
387.5,
389,
386.9,
387.1,
388.9,
389.9,
389,
387.8,
387.7,
387.3,
388.5,
388.7,
387.8,
387.3,
387.7,
386.9,
388.1,
388.8
] # Из лабораторной "измерение случайной величины".

plt.plot(list(range(ntries)), experiments)
plt.bar(list(range(ntries)), experiments)
plt.title('Experimental data')
plt.show()

import pandas

df = pandas.DataFrame(data={
    'experiments': experiments
})

df.to_csv("experiments.csv")

df.loc[df.experiments % 4 == 0, 'experiments'] = 0
df.to_hdf("experiments.h5", "experiments")

try:
    del df
except:
    pass

df1 = pandas.read_csv("experiments.csv")
df2 = pandas.read_hdf("experiments.h5")

df1['experiments'].plot(kind='bar')

print(df1.experiments.describe())
print(df2.experiments.describe())

df12 = pandas.DataFrame(data={
    'df1': df1['experiments'],
    'df2': df2['experiments'],
})

df12.plot.kde()

from scipy import stats

d1 = df12['df1']
d2 = df12['df2']

print(stats.kstest('norm', 'norm', N=3))
print(stats.kstest('norm', 'norm', N=500))
print(stats.kstest(d1, d2))
print()

print(stats.kstest(d1, 'norm', (d1.mean(), d1.std()), N=500)) #С изначальным значением слишком долго считалось.
print(stats.kstest(d2, 'norm', (d2.mean(), d2.std()), N=500))
