# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from scipy import stats
from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind


# data import
data = pd.read_csv('data_2.csv')
print(data.head())
mapping=pd.read_excel('test_mapping.xlsx')


#data discovery

print("Mapping")
mapping.dtypes
print('Number of variables: {}'.format(mapping.shape[1]))
print('Number of rows: {}'.format(mapping.shape[0]))

print("Data")
data.dtypes
print('Number of variables: {}'.format(data.shape[1]))
print('Number of rows: {}'.format(data.shape[0]))

#print(mapping.head())

# General Filters
# data = data[[data['sex']=='Male']]

# Relevent Columns 
col_list = mapping.act.values.tolist()
print(col_list)
streamlined =data.drop(columns = data.columns.difference(col_list))
race_map={0:2, 1:2,2:2,3:2,4:1,5:2,6:2}
streamlined["race"]=streamlined["race"].map(race_map)
#print(streamlined["race"].unique())


def mean_summarize(df):
    white1 = df[df["race"]==1] 
    white = white1.dropna()
    non_white1 = df[df["race"]==2] 
    non_white = non_white1.dropna()
    mean_white = white.iloc[:,1].mean()
    mean_non_white = non_white.iloc[:,1].mean()
    return [mean_white,mean_non_white,"NA"]

def count_summarize(df):
    white1 = df[df["race"]==1] 
    white = white1.dropna()
    non_white1 = df[df["race"]==2] 
    non_white = non_white1.dropna()
    number_white = len(white.index)
    number_nonwhite = len(non_white.index)
    return [number_white,number_nonwhite,"NA"]

def chi_handler(df,col_name):
    white1 = df[df["race"]==1] 
    white = white1.dropna()
    non_white1 = df[df["race"]==2] 
    non_white = non_white1.dropna()
    number_white = sum(white[col_name])
    number_nonwhite = sum(non_white[col_name])
    ind_1=len(white[white[col_name]==1])
    ind_2=len(white[white[col_name]==0])
    ind_3=len(non_white[non_white[col_name]==1])
    ind_4=len(non_white[non_white[col_name]==0])
    data=pd.DataFrame([['White',ind_1,ind_2],['Non White',ind_3,ind_4]],columns=['Race','Present','Not Present'])
    stat, p, dof, expected = chi2_contingency(data.iloc[:,1:].values,True)

    
    return [number_white,number_nonwhite,p]

def ttest_handler(df,col_name):
    white1 = df[df["race"]==1] 
    white = white1.dropna()
    non_white1 = df[df["race"]==2] 
    non_white = non_white1.dropna()
    number_white = white[col_name].mean()
    number_nonwhite = non_white[col_name].mean()
    t,p=ttest_ind(white[col_name], non_white[col_name], equal_var=False)
    
    return [number_white,number_nonwhite,p]

def n_h(n,h):
    val=[n,h[0],h[1],h[2]]
    return val

    
final = pd.DataFrame(columns = ['Variable',"White","Non-White","P-Value"])

final.loc[len(final)] =n_h("Age (mean, years)",mean_summarize(streamlined[['race','age']]))
final.loc[len(final)] =n_h("Male n  (%)",mean_summarize(streamlined[['race','sex']]))
final.loc[len(final)] =n_h("BMI (mean)",mean_summarize(streamlined[['race','bmi']]))
final.loc[len(final)] =n_h("MI",chi_handler(streamlined[["race","card_history___1"]], "card_history___1"))
final.loc[len(final)] =n_h("CVA",mean_summarize(streamlined[["race","card_history___2"]]))
final.loc[len(final)] =n_h("CAD",chi_handler(streamlined[["race","card_history___4"]], "card_history___4"))
final.loc[len(final)] =n_h("T2DM",chi_handler(streamlined[["race","card_history___13"]], "card_history___13"))
final.loc[len(final)] =n_h("Hypertension",chi_handler(streamlined[["race","card_history___11"]], "card_history___11"))
final.loc[len(final)] =n_h("Hyperlipidemia",chi_handler(streamlined[["race","card_history___9"]], "card_history___9"))
final.loc[len(final)] =n_h("Heart Failure",chi_handler(streamlined[["race","card_history___5"]], "card_history___5"))
final.loc[len(final)] =n_h("Arrythmia, history of",chi_handler(streamlined[["race","card_history___15"]], "card_history___15"))
final.loc[len(final)] =n_h("Alcohol History",chi_handler(streamlined[["race","card_history___17"]], "card_history___17"))
final.loc[len(final)] =n_h("Illicit Drug Use",chi_handler(streamlined[["race","spec_trigger___11"]], "spec_trigger___11"))
final.loc[len(final)] =n_h("Tobacco Use",chi_handler(streamlined[["race","card_history___16"]], "card_history___16"))
final.loc[len(final)] =n_h("COPD",chi_handler(streamlined[["race","other_hist___4"]], "other_hist___4"))
final.loc[len(final)] =n_h("End Stage Renal Disease",chi_handler(streamlined[["race","other_hist___2"]], "other_hist___2"))
final.loc[len(final)] =n_h("Functional Disability",chi_handler(streamlined[["race","other_hist___1"]], "other_hist___1"))
final.loc[len(final)] =n_h("Depression",chi_handler(streamlined[["race","psych_hist___1"]], "psych_hist___1"))
final.loc[len(final)] =n_h("Anxiety",chi_handler(streamlined[["race","psych_hist___6"]], "psych_hist___6"))
final.loc[len(final)] =n_h("Major Psych. Disorder",chi_handler(streamlined[["race","psych_hist___2"]], "psych_hist___2"))
final.loc[len(final)] =n_h("Dementia",count_summarize(streamlined[["race","psych_hist___4"]]))
final.loc[len(final)] =n_h("Chest Pain",chi_handler(streamlined[["race","pres_sympt___1"]], "pres_sympt___1"))
final.loc[len(final)] =n_h("Dyspnea",chi_handler(streamlined[["race","pres_sympt___2"]], "pres_sympt___2"))
final.loc[len(final)] =n_h("Syncope",chi_handler(streamlined[["race","pres_sympt___3"]], "pres_sympt___3"))
final.loc[len(final)] =n_h("Palpitations",chi_handler(streamlined[["race","pres_sympt___4"]], "pres_sympt___4"))
final.loc[len(final)] =n_h("ST Elevations",chi_handler(streamlined[["race","ecg_abnorm___2"]], "ecg_abnorm___2"))
final.loc[len(final)] =n_h("ST Depressions",chi_handler(streamlined[["race","ecg_abnorm___3"]], "ecg_abnorm___3"))
final.loc[len(final)] =n_h("TWI",chi_handler(streamlined[["race","TWI"]], "TWI"))
final.loc[len(final)] =n_h("LVEF",ttest_handler(streamlined[["race","lvef"]], "lvef"))
final.loc[len(final)] =n_h("Apical dyskinesis",chi_handler(streamlined[["race","akinesis_echo___1"]], "akinesis_echo___1"))
final.loc[len(final)] =n_h("Mid dyskinesis",chi_handler(streamlined[["race","akinesis_echo___2"]], "akinesis_echo___2"))
final.loc[len(final)] =n_h("Troponin",ttest_handler(streamlined[["race","mean_trop"]], "mean_trop"))
final.loc[len(final)] =n_h("CK",ttest_handler(streamlined[["race","ck"]], "ck"))
final.loc[len(final)] =n_h("CRP",count_summarize(streamlined[["race","crp"]]))
final.loc[len(final)] =n_h("eGFR",ttest_handler(streamlined[["race","egfr"]], "egfr"))
final.loc[len(final)] =n_h("BNP",ttest_handler(streamlined[["race","bnp"]], "bnp"))
final.loc[len(final)] =n_h("Hemoglobin",ttest_handler(streamlined[["race","hem"]], "hem"))
final.loc[len(final)] =n_h("Emotional trigger doc",ttest_handler(streamlined[["race","trigger___3"]], "trigger___3"))
final.loc[len(final)] =n_h("Physical trigger doc",ttest_handler(streamlined[["race","trigger___2"]], "trigger___2"))
final.loc[len(final)] =n_h("Physical and emotional",ttest_handler(streamlined[["race","trigger___6"]], "trigger___6"))
final.loc[len(final)] =n_h("Drug use",chi_handler(streamlined[["race","utox"]], "utox"))
final.loc[len(final)] =n_h("Prescribed aci/arb & bb ",chi_handler(streamlined[["race","meds_after_hosp___combo"]], "meds_after_hosp___combo"))
final.loc[len(final)] =n_h("Mortality data",chi_handler(streamlined[["race","alive"]], "alive"))
final.loc[len(final)] =n_h("trigger_combo_34",chi_handler(streamlined[["race","trigger_combo_34"]], "trigger_combo_34"))
final.loc[len(final)] =n_h("trigger_doc",chi_handler(streamlined[["race","trigger_doc"]], "trigger_doc"))



#print(final)
final.to_excel("output.xlsx")


streamlined[['race','age']].to_excel("test.xlsx")
print(mean_summarize(streamlined[['race','age']]))
print(streamlined[["race","mean_trop"]])
#print(summarize(streamlined[['race','age']]))
#print(summarize(streamlined[['race','sex']]))
#print(chi_handler(streamlined[["race","card_history___1"]], "card_history___1"))
#print(ttest_handler(streamlined[["race","lvef"]], "lvef"))
