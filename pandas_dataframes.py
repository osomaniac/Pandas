import pandas as pd 

grades_dict = {'Wally':[87,96,70],'Ava':[100,87,90],'Sam':[94,77,90],'Katie':[100,81,82],'Bob':[83,65,85]}

grades = pd.DataFrame(grades_dict)
# print(grades)

grades.index = ['Test1','Test2', 'Test3']
# print(grades)

# print(grades.Sam)
'''
print(grades.loc['Test1']) ## loc give names
print(grades.iloc[0]) ## iloc give index

print(grades.loc['Test1':'Test3']) ## range
print(grades.iloc[0:2]) ## iloc give index, does not include upper range

print(grades.loc[['Test1','Test3']]) ## only test 1 & 3
print(grades.iloc[[0,2]]) 

print(grades.loc[['Test1','Test3'], ['Ava', 'Katie']]) # only test 1 & 3 for only Ava and Katie
print(grades.iloc[[0,2],[1,3]])


print(grades[grades>90])
print(grades[(grades<90) & (grades>79)]) ## use & NOT 'and'

print(grades.at['Test2','Ava'])
grades.at['Test2','Ava'] = 100 # permanant change
print(grades.at['Test2','Ava'])

print(grades)
print(grades.iat[1,2])
grades.iat[1,2] = 87
print(grades)
'''

pd.set_option('precision',2)

'''
print(grades.describe())
print(grades.mean())
print((grades.T).mean()) ## transpose first to get the test averages

print(grades.sort_index(ascending=False))
print(grades.sort_index(axis=1)) ## 0 by rows, 1 by col
'''
print(grades.sort_values(by='Test1', axis=1, ascending=False))
print((grades.sort_values(by='Test1', axis=1, ascending=False)).T)
print(grades.T.sort_values(by='Test1', ascending=False)) ## same as above
print(grades.loc['Test1'].sort_values(ascending=False)) ## if you use inplace=True, sort change is permanent, else not