# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 13:28:42 2022

@author: jbaer
"""

import numpy as np
import pandas as pd

# load dataframe with country names, the names of inhibtants and adjectives
country_data = pd.DataFrame(np.loadtxt('D:\Studium\PhD\Media Tenor\Preprocessing\countries.txt', dtype = str, skiprows = 2, encoding = 'utf-8'))
# drop columns with definite articles 'der' and 'die
country_data.drop(columns = [1,3], inplace = True)

# rename columns
country_data.rename(columns = {0 : 'country', 2 : 'male', 4 : 'female', 5 : 'adjective'}, inplace = True)

# convert uppercases letters to lowercase letters
country_data['country'] = [word.lower() for word in country_data['country']]
country_data['male'] = [word.lower() for word in country_data['male']]
country_data['female'] = [word.lower() for word in country_data['female']]

# clean data from '_' and ',' characters
country_data['country'] = [word.replace('_', ' ') for word in country_data['country']]
country_data['male'] = [word.replace(',', '') for word in country_data['male']]

# drop words related to Germany
country_data.drop([34], inplace = True)

# transform dataframe to list
country_list = list(country_data.stack())

# delete '-' and '–' characters from country list
country_list  = [word for word in country_list if word != '-' and word != '–'] 

# seperate 'albaner/albanier' and 'albanerin/albanierin'
country_list[9:11] = ['albaner', 'albanier', 'albanerin', 'albanierin']

# load list with capital names and clean it
capital_data = pd.DataFrame(np.loadtxt('D:\Studium\PhD\Media Tenor\Preprocessing\capitals.txt', dtype = str, skiprows = 2, encoding = 'utf-8'))
capital_data.rename(columns = {0 : 'capital'}, inplace = True)
capital_data['capital'] = [word.lower() for word in capital_data['capital']]
capital_data['capital'] = [word.replace('_', ' ') for word in capital_data['capital']]

# transform dataframe to list
capital_list = list(capital_data['capital'])

# combine both lists
country_and_capital_list = country_list + capital_list

# save list
pd.DataFrame(set(country_and_capital_list)).to_excel('D:\Studium\PhD\Media Tenor\Preprocessing\country_and_capital_list.xlsx')