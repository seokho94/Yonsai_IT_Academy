import os, re
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

os.chdir(r'C:\\Users\\YONSAI\\Documents\\GitHub\\Yonsai_IT_Academy\\vscode\\python\\py_doit')
df2 = pd.read_csv('survey.csv')

print(df2.head())

print(df2.mean())

print(df2.income.sum())

print(df2.income.mean())

print(df2.income.median())

print(df2.describe())

print(df2.income.describe())

print(df2.sex.value_counts())

print(df2.groupby(df2.sex).mean())

male = df2.income[df2.sex == 'm']

female = df2.income[df2.sex == 'f']

print(stats.ttest_ind(male, female))

ttest_result = stats.ttest_ind(male, female)

print(ttest_result[0])
print(ttest_result[1])

if ttest_result[1] > .05:
    print('p-value는 {}로 95% 수준에서 유의하지 않음'.format(ttest_result[1]))
else :
    print('p-value는 {}로 95% 수준에서 유의함'.format(ttest_result[1]))
    
if ttest_result[1] > .05:
    print('p-value는 %f로 95%% 수준에서 유의하지 않음'%ttest_result[1])
else :
    print('p-value는 %f로 95%% 수준에서 유의함'%ttest_result[1]) 
    
corr = df2.corr()
print(corr)

print(df2.corr(method = 'spearman'))

print(df2.income.corr(df2.stress))

corr.to_csv('corr.csv')

model = smf.ols(formula = 'jobSatisfaction~English', data = df2)
result = model.fit()
print(result.summary())

model2 = smf.ols(formula = 'jobSatisfaction~English + income', data = df2)
result = model2.fit()

X = [1, 4, 9, 16, 25, 36, 49, 64]

Y = [i for i in range(1, 9)]
plt.plot(X,Y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('maplotlib sample')
plt.show()