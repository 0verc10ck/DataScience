import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style='whitegrid')
from pandas.plotting import scatter_matrix
import tkinter

red_input = pd.read_csv('winequality-red.csv', sep=';')#open red
red_input['WineType'] = 'Red'#add column wineType
white_input = pd.read_csv('winequality-white.csv',sep=';')#openWhite
white_input['WineType'] = 'White'#add column wineType
result = pd.concat([red_input, white_input], ignore_index=True, sort = False)#concat red and white
result.to_csv('result.csv',) #save as csv file
#print(result.describe()) # 5 * 13이 되어야 하는데 5 * 12로 나옴

print("평균\n")
print(result.mean(axis = 0))
print("\n분산\n")
print(result.var(axis= 0))
print("\n\n")

#원형차트 (white vs. red)
result['WineType'].value_counts().plot.pie(autopct='%.1f')
#plt.show()

print('히스토그램')
result['alcohol'].plot.hist()
plt.show()

print('상자 그림')
result['pH'].plot.box(by ='class')
plt.show()

print('바이올림 플롯') #(전체 속성 또는 속성 자유 선택, 단 white vs. red 확률밀도함수 구분하여 출력)
sns.violinplot(data = result, x = 'WineType', y = 'sulphates')
plt.show()

print('산점도')
result.plot.scatter(y = 'pH', x = 'quality')
plt.title('pH vs quality')
plt.show()


print('산점도행렬')
scatter_matrix(result)
plt.show()