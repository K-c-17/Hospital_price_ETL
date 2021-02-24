#!/usr/bin/env python
# coding: utf-8

# In[471]:


import pandas as pd
import numpy as np


# In[472]:


df=pd.read_excel('Copy of Copy of 550526150_CAMC_standardcharges 011521.xlsx')


# In[473]:


df.head()


# In[474]:


df.columns


# In[475]:


df_backup=df


# In[476]:


def get_code(x):
    for j in list(x.columns):
        if type(j)==str and any(y in j.lower() for y in ['cpt']):
            x.rename(columns={j:'Code'},inplace=True)
            x['Type_of_code']='CPT/HCPCS'
            return print('Done.CPT column was replaced')
    for j in list(x.columns):
        if type(j)==str and any(y in j.lower() for y in ['cpt','drg']):
            x.rename(columns={j:'Code'},inplace=True)
            x['Type_of_code']='CPT/HCPCS'
            return print('Done.CPT-DRG column was replaced')
    for j in list(x.columns):
        if type(j)==str and any(y in j.lower() for y in ['drg']):
            x.rename(columns={j:'Code'},inplace=True)
            x['Type_of_code']='MS-DRG'
            return print('Done.DRG column was replaced')
    for j in list(x.columns):
        if type(j)==str and any(y in j.lower() for y in ['revenue','rev']):
            x.rename(columns={j:'Code'},inplace=True)
            x['Type_of_code']='Revenue_code'
            return print('Done.Revenue column was replaced')
    return print('Not found. It is unusual')


# In[477]:


def get_desc(x):
    for j in list(x.columns):
        if type(j)==str and any(y in j.lower() for y in ['description']) :
            x.rename(columns={j:'Description'},inplace=True)
            return print('Done')
    x['Description']=''
    return print('Not found. It is unusual')


# In[478]:


def get_gross(x):
    for j in list(x.columns):
        if type(j)==str and any(y in j.lower() for y in ['gross']):
            x.rename(columns={j:'Gross_Charges'},inplace=True)
            return print('Done')
    x['Gross_Charges']=''
    return print('Not found')


# In[479]:


def get_dis_CP(x):
    for j in list(x.columns):
        if type(j)==str and any(y in j.lower() for y in ['discounted']) :
            x.rename(columns={j:'Discounted_Cash_Price'},inplace=True)
            return print('Done')
    x['Discounted_Cash_Price']=''
    return print('Not found')


# In[480]:


def get_patient_class(x):
    for j in list(x.columns):
        if type(j)==str and any(y in j.lower() for y in ['inpatient','outpatient','patient_type']) :
            x.rename(columns={j:'Patient_class'},inplace=True)
            return print('Done')
    x['Patient_class']=''
    return print('Not found')


# In[481]:


def get_volume(x):
    for j in list(x.columns):
        if type(j)==str and any(y in j.lower() for y in ['volume']) :
            x.rename(columns={j:'Volume'},inplace=True)
            return print('Done')
    x['Volume']=''
    return print('Not found')


# In[482]:


def get_max_charge(x):
    for j in list(x.columns):
        if type(j)==str and any(y in j.lower() for y in ['maximum negotiated charge','max charge','max negotiated charge','max negotiated rate']) :
            x.rename(columns={j:'Max_charge'},inplace=True)
            return print('Done')
    x['Max_charge']=''
    return print('Not found')


# In[483]:


def get_min_charge(x):
    for j in list(x.columns):
        if type(j)==str and any(y in j.lower() for y in ['minimum negotiated charge','min charge','min negotiated charge','min negotiated rate']) :
            x.rename(columns={j:'Min_charge'},inplace=True)
            return print('Done')
    x['Min_charge']=''
    return print('Not found')


# In[484]:


def get_ndc_code(x):
    for j in list(x.columns):
        if type(j)==str and any(y in j.lower() for y in ['ndc']) :
            x.rename(columns={j:'NDC_code'},inplace=True)
            return print('Done')
    x['NDC_code']=''
    return print('Not found')


# In[485]:


def get_avg_charge(x):
    for j in list(x.columns):
        if type(j)==str and any(y in j.lower() for y in ['average charge']) :
            x.rename(columns={j:'Average_Charge'},inplace=True)
            return print('Done')
    x['Average_Charge']=''
    return print('Not found')


# In[486]:


def get_self_pay(x):
    for j in list(x.columns):
        if type(j)==str and any(y in j.lower() for y in ['self','undiscounted','self pay price']) :
            x.rename(columns={j:'Self_Pay_Price'},inplace=True)
            return print('Done')
    x['Self_Pay_Price']=''
    return print('Not found')


# In[487]:


def code_rev_merge(x):
    for j in list(x.columns):
        if type(j)==str and any(y in j.lower() for y in ['ms-drg']):
            x['Type_of_code'][(x['Code']=='') & (x[j].notnull())]='MS-DRG'
            x['Code']=x['Code'].combine_first(x[j])
        if type(j)==str and any(y in j.lower() for y in ['rev_code','revenue_code']):
            x['Type_of_code'][(x['Code']=='') & (x[j].notnull())]='Revenue_code'
            x['Code']=x['Code'].combine_first(x[j])


# In[488]:


def code_rev_merge_V1(x):
    x['Code'].replace(np.NaN,'$',inplace=True)
    for j in list(x.columns):
        if type(j)==str and any(y in j.lower() for y in ['ms-drg']):
            x['Type_of_code'][((x['Code']=='$') | (~x['Code'].str.contains('[0-9]'))) & (x[j].notnull())]='MS-DRG'
            #x['Code'].combine_first(x[j])
            x['Code'][((x['Code']=='$') | (~x['Code'].str.contains('[0-9]'))) & (x[j].notnull())]=x[j]
            print('1')
        if type(j)==str and any(y in j.lower() for y in ['charge code']):
            x['Type_of_code'][((x['Code']=='$') | (~x['Code'].str.contains('[0-9]'))) & (x[j].notnull())]='Hospital Internal Code'
            #x['Code'].combine_first(x[j])
            x['Code'][((x['Code']=='$') | (~x['Code'].str.contains('[0-9]'))) & (x[j].notnull())]=x[j]
            print('2')
        if type(j)==str and any(y in j.lower() for y in ['rev_code','revenue_code']):
            x['Type_of_code'][((x['Code']=='$') | (~x['Code'].str.contains('[0-9]'))) & (x[j].notnull())]='Revenue_code'
            #x['Code'].combine_first(x[j])
            x['Code'][((x['Code']=='$') | (~x['Code'].str.contains('[0-9]'))) & (x[j].notnull())]=x[j]
            print('3')


# In[489]:


get_ndc_code(df)


# In[490]:


get_avg_charge(df)


# In[491]:


get_self_pay(df)


# In[492]:


get_patient_class(df)


# In[493]:


get_dis_CP(df)


# In[494]:


get_gross(df)


# In[495]:


get_desc(df)


# In[496]:


get_code(df)


# In[497]:


df.columns


# In[498]:


code_rev_merge_V1(df)


# In[499]:


df.head()


# In[500]:


get_max_charge(df)


# In[501]:


get_min_charge(df)


# In[502]:


get_volume(df)


# In[503]:


df.insert(0,'Hospital_pin',1233423)


# In[504]:


df.insert(1,'Hospital_name','Charleston Area Medical Centre')


# In[505]:


df.columns


# In[515]:


def id_vars_collector(x):
    jim=[]
    for j in list(x.columns):
        #print(j)
        if type(j)==str and any(y in ['hospital_pin','hospital_name','description','code','type_of_code','ndc_code','discounted_cash_price','max_charge','min_charge','average_charge','self_pay_price','gross_charges','patient_class','volume'] for y in [j.lower()]):
            jim.append(j)
    return jim


# In[516]:


id_var=id_vars_collector(df)


# In[517]:


id_var


# In[519]:


list(df.columns)


# In[523]:


payer_cols=list(df.columns)[14:-5]


# In[524]:


payer_cols


# In[525]:


final_lis=id_var+payer_cols


# In[526]:


final_lis


# In[527]:


df1=df[final_lis]


# In[535]:


df_unpivoted = df1.melt(id_vars=id_var, var_name='Payer', value_name='Payer_Reimbursement')
df_unpivoted


# In[536]:


print(df1.shape)
print(df_unpivoted.shape)


# In[537]:


def split_payer(x):
    tim=x['Payer'].str.split(n=2,expand=True)
    x['Payer']=tim[0]
    x['Plan_Type']=tim[1]
    x['Patient_class']=tim[2]


# In[538]:


split_payer(df_unpivoted)


# In[539]:


df_unpivoted.columns


# In[541]:


df_final=df_unpivoted[['Hospital_pin','Hospital_name','Description','Code','Type_of_code','NDC_code','Discounted_Cash_Price','Max_charge','Min_charge','Average_Charge','Self_Pay_Price','Gross_Charges','Patient_class','Payer','Plan_Type','Payer_Reimbursement','Volume']]

