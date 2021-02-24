#!/usr/bin/env python
# coding: utf-8

# In[153]:


import pandas as pd
import numpy as np


# In[154]:


tab1=pd.read_excel('grant_hospital.xlsx',header=3)


# In[155]:


tab1['Type_of_Code']=tab1['Code'].str.extract('(MS-DRG|HCPCS|CPT)')


# In[156]:


tab1['Code_mod']=''


# In[157]:


tab1['Code_mod'][tab1['Type_of_Code']=='MS-DRG']=tab1['Code'].str[-3:]
tab1['Code_mod'][tab1['Type_of_Code']=='HCPCS']=tab1['Code'].str[-5:]
tab1['Code_mod'][tab1['Type_of_Code']=='CPT']=tab1['Code'].str[-5:]


# In[158]:


tab1['Code']=tab1['Code_mod']


# In[159]:


tab1['Hospital_name']='Grant Medical Centre'
tab1['Hospital_pin']='124234'
tab1['NDC_code']=''
tab1['Market']='Columbus'
tab1.rename(columns={'Patient Class (Inpatient/Outpatient)':'Patient_class','Procedure Description':'Description','Discounted Cash Price (Uninsured Discount 35%)':'Discounted_cash_price','De-identified Minimum negotiated charge':'Min_charge','De-identified maximum negotiated charge':'Max_charge'},inplace=True)
tab1['Average_charge']=''
tab1['Volume']=''
tab1['payment_method']=''


# In[160]:


tab2=tab1[['Hospital_pin','Hospital_name','Market','Description', 'NDC_code','Average_charge','Patient_class', 'Code','Type_of_Code','Gross Charge', 'Discounted_cash_price','Min_charge', 'Max_charge','Volume','payment_method']]


# In[161]:


tab3=pd.read_excel('grant_hospital.xlsx',header=2)


# In[203]:


columns=['Hospital_pin', 'Hospital_name', 'Market', 'Description', 'NDC_code', 'Average_charge', 'Patient_class', 'Code', 'Type_of_Code', 'Gross Charge', 'Discounted_cash_price', 'Min_charge', 'Max_charge', 'Volume', 'payment_method','Payer_reimbursemet','Payer','Plan_Type']
tab_final=pd.DataFrame(columns=['Hospital_pin', 'Hospital_name', 'Market', 'Description', 'NDC_code', 'Average_charge', 'Patient_class', 'Code', 'Type_of_Code', 'Gross Charge', 'Discounted_cash_price', 'Min_charge', 'Max_charge', 'Volume', 'payment_method','Payer_reimbursemet','Payer','Plan_Type'])


# In[204]:


jim=list(tab3.columns)[7:-2]
for j in jim:
    print(j+' Payer ingestion started')
    tab4=tab3[[j]]
    tab4['Payer']=j
    tab4.rename(columns={j:'Payer_reimbursemet'},inplace=True)
    #print(tab4.columns)
    for i in list(list(tab4['Payer_reimbursemet'][0:1])[0].split(',')):
        print(i+' Plan Type ingestion started')
        tab4['Plan_Type']=i
        tab4_temp=tab4[1:]
        #print(str(len(tab2)),'is the length of tab2')
        #print(str(len(tab4_temp)),'is the length of tab4_temp')
        tab_piece=pd.concat([tab2,tab4_temp],axis=1,ignore_index=True)
        tab_piece.columns=['Hospital_pin', 'Hospital_name', 'Market', 'Description', 'NDC_code', 'Average_charge', 'Patient_class', 'Code', 'Type_of_Code', 'Gross Charge', 'Discounted_cash_price', 'Min_charge', 'Max_charge', 'Volume', 'payment_method','Payer_reimbursemet','Payer','Plan_Type']
        #print(list(tab_piece.columns))
        #print(str(len(tab_piece)),'is the length of tab_piece')
        tab_final=tab_final.append(tab_piece,ignore_index=True,sort=False)
        print(str(len(tab_final)),'is the length of tab_final')
        #print(len(tab_final))
        print(i+' Plan Type ingestion over')
    print(j+' Payer ingestion is done')
    
    


# In[ ]:




