#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Stock_Market = {'Year': [2017,2017,2017,2017],
                'Month': [12, 11,10,9],
                'Interest_Rate': [2.75,2.5,2.5,2.5],
                'Unemployment_Rate': [5.3,5.3,5.3,5.3],
                'Stock_Index_Price': [1464,1394,1357,1293]        
                }

df = pd.DataFrame(Stock_Market,columns=['Year','Month','Interest_Rate','Unemployment_Rate','Stock_Index_Price']) 

print (df)


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
  
Stock_Market = {'Year': [2017,2017,2017,2017],
                'Month': [12, 11,10,9],
                'Interest_Rate': [2.75,2.5,2.5,2.5],
                'Unemployment_Rate': [5.3,5.3,5.3,5.3],
                'Stock_Index_Price': [1464,1394,1357,1293]        
                }
 
df = pd.DataFrame(Stock_Market,columns=['Year','Month','Interest_Rate','Unemployment_Rate','Stock_Index_Price'])
 
plt.scatter(df['Interest_Rate'], df['Stock_Index_Price'], color='red')
plt.title('Stock Index Price Vs Interest Rate', fontsize=14)
plt.xlabel('Interest Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.grid(True)
plt.show()


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
  
Stock_Market = {'Year': [2017,2017,2017,2017],
                'Month': [12, 11,10,9],
                'Interest_Rate': [2.75,2.5,2.5,2.5],
                'Unemployment_Rate': [5.3,5.3,5.3,5.3],
                'Stock_Index_Price': [1464,1394,1357,1293]        
                }
 
 
df = pd.DataFrame(Stock_Market,columns=['Year','Month','Interest_Rate','Unemployment_Rate','Stock_Index_Price'])
 
plt.scatter(df['Unemployment_Rate'], df['Stock_Index_Price'], color='green')
plt.title('Stock Index Price Vs Unemployment Rate', fontsize=14)
plt.xlabel('Unemployment Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.grid(True)
plt.show()


# In[ ]:




