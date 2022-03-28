import pandas as pd
import re, os
import usecsv
os.chdir(r'C:\\Users\\YONSAI\Documents\\GitHub\\Yonsai_IT_Academy\\vscode\\python\\py_doit')

df = pd.read_csv('apt_201912.csv', encoding='cp949')
print(df.head())
print(df.tail())
print(df.시군구)
print(df.전용면적 > 130)

print(df[df.전용면적 > 130])

print(df.거래금액[df.전용면적 > 130])

print(df.거래금액[(df.전용면적 > 130) & (df.거래금액 < 15000)])

print(df.거래금액[(df.전용면적 > 130) | (df.거래금액 < 15000)])

print(df.loc[:10, ['단지명', '거래금액']])

print(df.loc[:, ['단지명', '거래금액']][df.거래금액 > 40000])

df['단가'] = df.거래금액 / df.전용면적
print(df.loc[:10, ('거래금액','전용면적','단가')])

print(df.sort_values(by = '거래금액').loc[:, ('거래금액', '시군구')])

print(df.sort_values(by = '거래금액', ascending=False).loc[:, ('거래금액', '시군구')])

print(df[df.거래금액 > 40000].sort_values(by = '전용면적').loc[:,('거래금액','전용면적', '시군구')])

print(df.시군구.str.find('강릉'))

print(df[df.시군구.str.find('강릉')>-1])

dfF = df[df.시군구.str.find('강릉') > -1]

print(dfF.mean())