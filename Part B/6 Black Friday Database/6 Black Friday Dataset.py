"""a)Load the â€˜Black Fridayâ€™ dataset into one of the data structures (NumPy or Pandas).\n",
    "b)Display header rows and description of the loaded dataset.\n",
"""
import pandas as pd
import numpy as np

df = pd.read_csv("blackfri.csv")
print("\<-----Data Information----->\")
print("Head of Dataset")
print(df.head(5))
print("Head of Dataset")
print(df.describe())
print(df.info())

"""c) Remove unnecessary features (E.g. drop unwanted columns) from the dataset such as â€˜User_IDâ€™, â€˜Product_ID â€˜ â€˜Stay_In_Current_City_Yearsâ€™"""
df.drop(['User_ID','Product_ID','Stay_In_Current_City_Years'], axis=1, inplace=True)
print(df.head(5))
   
"""d) Manipulate data by replacing empty column values in â€˜City_Categoryâ€™ with a default value for the city. """
print("Filling empty values")
df['City_Category'] = df['City_Category'].fillna(\"A\")
print(df.head(5))

"""e) Convert the attribute â€˜City_Categoryâ€™ to have â€˜Aâ€™ to be â€˜Metro Citiesâ€™, â€˜Bâ€™ to be â€˜Small Townsâ€™ ,  â€˜Câ€™ to be â€˜Villagesâ€™."""
print("Mapping values/attributes in City_Category to types")
df['City_Category'] = df['City_Category'].map({'A':'Metro cities','B':'Small Towns','C':'Villages'})
print(df.head(5))

"""f) Rename the attribute â€˜Product_Category_1â€™ to have â€˜Baseball Capsâ€™, \n",
    "â€˜Product_Category_2â€™ to have â€˜Wine Tumblersâ€™ and â€˜Product_Category_3â€™ to \n",
    "have â€˜Pet Raincoatsâ€™\n",
    """
print("Renaming the column names")
df.rename(columns={'Product_Category_1':'Baseball_Caps','Product_Category_2':'Wine_Tumblers','Product_Category_3':'Pet_Raincoats'},inplace=True)
print(df.head(5))

"""g) Convert the attribute â€˜Marital_Statusâ€™ to have â€˜1:Marriedâ€™ and â€˜0:Un-Marriedâ€™\n","""
print("Mapping values/attributes in Marital Status to types")
df['Marital_Status'] = df['Marital_Status'].map({1:'Married',0:'Un-Married'})
print(df.head(5))

"""h) Perform the following visualizations on the loaded dataset:\n",
    "i)   Tally of the Number of Male & Female who bought â€˜Product_Category_3(Pet_Raincoats)â€™. \n",
    """
import matplotlib.pyplot as plt
import seaborn as sns
print("<-------Data Visualisation------->")
print(pd.crosstab(df.Gender,df.Baseball_Caps))
print(pd.crosstab(df.Gender,df.Pet_Raincoats))

ax = sns.countplot(data=df,x='Gender',hue='Pet_Raincoats',palette='Set2')
ax.set(title='Male and Female who bought Pet_Raincoats',xlabel='Gender',ylabel='Count')
plt.show()


"""h) Perform the following visualizations on the loaded dataset:\n",
    "ii)  Total Number of Male & Female persons belonging to each city category\n",
    """
ax = sns.countplot(data=df,x='Gender',hue='City_Category',palette='Set1')
ax.set(title='Male and Female belonging to each city',xlabel='Gender',ylabel='Count')
plt.show()
