#Öznur Güngör - 2076396

import pandas as pd
import os

def group_by_mean(df,gb,m):
    df_res = df.groupby([gb])[m].mean().reset_index()
    return df_res

#reading files       
filename = os.getcwd() + "/sudeste.csv"
filename2 = os.getcwd() + "/weather_madrid_LEMD_1997_2015.csv"

df_brazil = pd.read_csv(filename,usecols=["temp","date"])
df_madrid = pd.read_csv(filename2,usecols=["Mean TemperatureC","CET"])
print(df_brazil.columns)
print(df_madrid.columns)
print(df_madrid['CET'])
print(df_brazil['date'])

df_madrid['date'] = df_madrid['CET']
del df_madrid['CET']

df_brazil_new = group_by_mean(df_brazil,'date','temp')
df_merge = pd.merge(df_brazil_new, df_madrid, how='inner', on=['date'])

print(df_merge)

#just checking
'''
print(min(df_brazil['date']))
print(max(df_brazil['date']))
print(min(df_madrid['date']))
print(max(df_madrid['date']))
print(min(df_merge['date']))
print(max(df_merge['date']))
print(df_brazil[df_brazil['date']=='2000-05-24'])
print(df_madrid[df_madrid['date']=='2000-05-24'])
'''

df_final = pd.DataFrame(columns=['temp_brazil','temp_madrid','date'])
df_final['temp_brazil'] = df_merge['temp']
df_final['temp_madrid'] = df_merge['Mean TemperatureC']
df_final['date'] = df_merge['date']

print(df_final)

#Heat maps (Figure 1) display numeric tabular data where the cells are colored depending upon the contained value. But here, this may be somehow unnecessary.
import seaborn as sns
print(df_final.corr())
sns.heatmap(df_final.corr())

import matplotlib.pyplot as plt
df_final.plot(kind='scatter',x='temp_brazil',y='temp_madrid',color='red')
plt.show()

#A correlation between variables indicates that as one variable changes in value, the other variable tends to change in a specific direction.
#Understanding that relationship is useful because we can use the value of one variable to predict the value of the other variable.
#If correlation coefficient was +1 (/-1), we would interpret this as perfect pozitive relationship (/perfect negative relationship). If it was 0, that means no relationship i.e as one value increases, there is no tendency for the other value to change in a specific direction.
#Here we see that the correlation coefficient is -0.030652. This means that there is a weak negative tendency between variables (temp_brazil and temp_madrid), since the value is really close to 0, the variables are not affected with each other prominently and the correlation does not mean much.
#Plot attached with this exam (Figure 2) shows the relationship between temp_brazil and temp_madrid. 