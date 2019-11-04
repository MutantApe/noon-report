#from Shipping.models import YangMIng_Daily_Noon
from django.db.backends.mysql import schema

import pandas as pd
data = pd.read_excel('C:/Users/Abhi/Downloads/04oct2018to16apr2019.xlsx',header=None,index=False)
d   =   pd.read_csv('C:/Users/Abhi/Documents/myDB.csv')
#print(data.head())
#d2=data.head()
#all_fields=YangMIng_Daily_Noon._meta.get_fields()
ls=data.iloc[5:data.shape[0]-2][0]
print(type(ls))

'''for i in data.iloc[0][7:]:
    print(i)'''

'''for i in data.iloc[1]:
    print(i)'''
#st=data.iloc[4:][0,]
#df=data.iloc[4
#for i in d2.iloc[0][10]:
    #print(i)
#st.to_excel("df.xlsx")

# Convert the dataframe to an XlsxWriter Excel object.
#data.to_excel('new.xlsx')