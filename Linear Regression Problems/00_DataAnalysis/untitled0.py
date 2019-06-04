# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:24:19 2019

@author: egwil
"""

# Import Data
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', parse_dates=['date'], index_col='date')
df.reset_index(inplace=True)

# Prepare data
df['year'] = [d.year for d in df.date]
df['month'] = [d.strftime('%b') for d in df.date]
years = df['year'].unique()

print(df.head())

# Prep Colors
#np.random.seed(100)
#mycolors = np.random.choice(list(mpl.colors.XKCD_COLORS.keys()), len(years), replace=False)
#
## Draw Plot
#plt.figure(figsize=(16,12), dpi= 80)
#for i, y in enumerate(years):
#    if i > 0:        
#        plt.plot('month', 'value', data=df.loc[df.year==y, :], color=mycolors[i], label=y)
#        plt.text(df.loc[df.year==y, :].shape[0]-.9, df.loc[df.year==y, 'value'][-1:].values[0], y, fontsize=12, color=mycolors[i])
#
## Decoration
#plt.gca().set(xlim=(-0.3, 11), ylim=(2, 30), ylabel='$Drug Sales$', xlabel='$Month$')
#plt.yticks(fontsize=12, alpha=.7)
#plt.title("Seasonal Plot of Drug Sales Time Series", fontsize=20)
#plt.show()