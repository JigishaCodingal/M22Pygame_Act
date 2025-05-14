import pandas as pd
s=pd.Series([5,9,3,2])
print(s)
s=pd.Series({'a':15,'b':10,'c':15,'d':20})
print(s)
s=pd.Series([5,9,3,2],[1,0,4,8])
print(s)
s=pd.DataFrame([[5,9,3,2],[15,19,13,12],[50,90,30,20]])
print(s)
print(s[1])
print(s.loc[:,1])#column
print(s.loc[1])#row
df=pd.DataFrame({'a':[2,7,9],'b':[20,70,90],'c':[23,27,19]})
print(df)