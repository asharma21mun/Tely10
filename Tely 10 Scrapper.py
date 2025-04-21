# Data Manipulation Libraaries

import pandas as pd
import numpy as np
from glob import glob

# Date Manipulation Library

from datetime import datetime

# Data Scrapping Libraries

import requests
from bs4 import BeautifulSoup
from html_table_parser.parser import HTMLTableParser


# Statistical Analysis Libraries

from sklearn import linear_model 
from sklearn.metrics import r2_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt 
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression
from scipy.stats import f_oneway





# The link for the Tely 10 race data. We have created a list with Years and the link

year_link = [
            [    1978,'https://www.nlaa.ca/results/rr/1978/19780625_Tely-10.php',                                ],
            [    1981,'https://www.nlaa.ca/results/rr/1981/19810712_54th_Tely_10.php',                           ],
            [    1982,'https://www.nlaa.ca/results/rr/1982/1982_0711_55th_Tely_10_Atlantic_Championships.php',   ],
            [    1984,'https://www.nlaa.ca/results/rr/1984/19840715_Tely_10.php',                                ],
            [    1985,'https://www.nlaa.ca/results/rr/1985/19850714_Tely_10.php',                                ],
            [    1986,'https://www.nlaa.ca/results/rr/1986/1986_07_06_59th_Tely_10.php',                         ],
            [    1987,'https://www.nlaa.ca/results/rr/1987/19870705_60th_Tely_10.php',                           ],
            [    1988, 'https://www.nlaa.ca/results/rr/1988/19880717_61st_Tely10.php',                           ],
            [    1990,'https://www.nlaa.ca/results/rr/1990/19900715_63rd_Tely_10.php',                           ],
            [    1991,'https://www.nlaa.ca/results/rr/1991/19910714_64th_Tely_10.php',                           ],
            [    1992,'https://www.nlaa.ca/results/rr/1992/19920712-Tely10.php',                                 ],
            [    1996,'https://www.nlaa.ca/results/rr/1996/19960714-tely10.php',                                 ],
            [    1997,'https://www.nlaa.ca/results/rr/1997/19970713-tely-10.php',                                 ],
            [    1998,'https://www.nlaa.ca/results/rr/1998/19980712-tely-10.php',                                ],
            [    1999,'https://www.nlaa.ca/results/rr/1999/19990711-tely-10.php',                                ],
            [    2000,'https://www.nlaa.ca/results/rr/2000/20000716-tely-10.php',                                ],
            [    2001,'https://www.nlaa.ca/results/rr/2001/20010722-tely-10.php',                                ],
            [    2002,'https://www.nlaa.ca/results/rr/2002/20020728-tely-10.php',                                ],
            [    2003,'https://www.nlaa.ca/results/rr/2003/20030727-tely-10.php',                                ],
            [    2004,'https://www.nlaa.ca/results/rr/2004/20040725-tely-10.php',                                ],
            [    2005,'https://www.nlaa.ca/results/rr/2005/20050724_tely_10.php',                                ],
            [    2006,'https://www.nlaa.ca/results/rr/2006/20060723_tely_10.php',                                ],
            [    2007,'https://www.nlaa.ca/results/rr/2007/0722tely10.php',                                      ],
            [    2008,'https://www.nlaa.ca/results/rr/2008/0727tely10.php',                                      ],
            [    2009,'https://www.nlaa.ca/results/rr/2009/0726tely10.php',                                      ],
            [    2010,'https://www.nlaa.ca/results/rr/2010/2010tely10results.php',                               ],
            [    2011,'https://www.nlaa.ca/results/rr/2011/2011tely10results.php',                               ],
            [    2012,'https://www.nlaa.ca/results/rr/2012/20120722tely10results.php',                           ],
            [    2013,'https://www.nlaa.ca/results/rr/2013/20130728tely10results.php',                           ],
            [    2014,'https://www.nlaa.ca/results/rr/2014/20140727tely10results.php',                           ],
            [    2015,'https://www.nlaa.ca/results/rr/2015/20150726tely10results.php',                           ],
            [    2016,'https://www.nlaa.ca/results/rr/2016/20160724tely10results.php',                           ],
            [    2017,'https://www.nlaa.ca/results/rr/2017/20170723tely10results.php',                           ],
            [    2018,'https://www.nlaa.ca/results/rr/2018/20180722tely10results.php',                           ],
            [    2019,'https://www.nlaa.ca/results/rr/2019/20190728-tely10-results.php',                         ],
            [    2021,'https://www.nlaa.ca/results/rr/2021/20211031-tely10-results.php',                         ],
            [    2022,'https://www.nlaa.ca/results/rr/2022/20221008-tely10-results.php',                         ],
            [    2023,'https://www.nlaa.ca/results/rr/2023/20230625-tely10-results.php'                          ]
            
            ]




# Going over the URL for Race Data. This part is mainly for Scrapping the data from the website.


for year, url in year_link:

    

    # Send GET request to the website

    response = requests.get(url)

    # Parse the HTML code using BeautifulSoup

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract relevant data from the scraped HTML code

    p = HTMLTableParser()

    table_data = soup.find('pre').text
    row = []
    ls = []

    

    # Iterating over each row of the data scrapped.


    for idx, line in enumerate(table_data.split('\n')[1:]):


    

        # The format of the race changes over years. We are extracting the data from the website. The data is stored in a list of string and we index the values. 
        # The index for the data in the list has changes over the years.

        if year == 1997:

            # 2003, 2004

            position = line[0:3]
            bib = line[6:9]
            Name = line[11:35]
            time = line[39:48]
            sex_category = line[51:52]
            sex_rank = line[63:69]
            rank_cat = line[55:60]
            chip_time = line[63:65]
            pace = line[63:65]
            location = line[63:65]

        elif year <= 2004:

            # 2003, 2004

            position = line[0:4]
            bib = line[6:10]
            Name = line[11:39]
            time = line[40:48]
            sex_category = line[49:57]
            sex_rank = line[58:64]
            rank_cat = line[65:69]
            chip_time = line[70:78]
            pace = line[79:85]
            location = line[86:]


        elif year == 2005:

            # 2005


            position = line[0:4]
            bib = line[7:10]
            Name = line[11:33]
            time = line[34:42]
            sex_category = line[43:51]
            sex_rank = line[52:57]
            rank_cat = line[61:64]
            chip_time = line[72:79]
            pace = line[65:71]
            location = line[80:]


        elif   2006 <= year <= 2014:        

            # 2006


            position = line[0:4]
            bib = line[7:10]
            Name = line[11:33]
            time = line[34:42]
            sex_category = line[43:51]
            sex_rank = line[52:57]
            rank_cat = line[61:64]
            chip_time = line[72:80]
            pace = line[67:72]
            location = line[81:]
        

        elif   2014 <= year <= 2022:       

            # 2014 onwards

            position = line[0:5]
            bib = line[6:10]
            Name = line[11:42]
            time = line[43:51]
            sex_category = line[52:59]
            sex_rank = line[60:69]
            rank_cat = line[70:73]
            chip_time = line[75:81]
            pace = line[82:90]
            location = line[91:]


        elif   year == 2023:  
            
            # 2023

            position = line[0:4]
            bib = line[7:10]
            Name = line[11:42]
            time = line[43:51]
            sex_category = line[52:59]
            sex_rank = line[60:66]
            rank_cat = line[70:75]
            chip_time = line[77:86]
            pace = line[67:77]
            location = line[86:]


        elif   year == 2024:

            # 2024

            position = line[0:5]
            bib = line[6:10]
            Name = line[11:42]
            time = line[43:51]
            sex_category = line[52:62]
            sex_rank = line[63:69]
            rank_cat = line[70:73]
            chip_time = line[75:81]
            pace = line[82:90]
            location = line[91:]





        row.append( [position,bib,Name,time,sex_category,sex_rank,rank_cat,chip_time,pace,location] )
        # row = [i for i in row if i ]


    # Creating a table to save the data.
    
    df = pd.DataFrame([])
    df = df.append(row)
    df['year'] = year

    # Saving the Data

    df.to_csv(fr'C:\Users\Monk\Codebase\Tely 10\Tely 10 data {year}.csv')





# Function to grooup years into a groups of 5 years. From 1978-1989, we are grouping the years into a single group since we don't have a lot of data berween those years.

def year_group(x):


    if  1978 <= x.Year <= 1989:

        return '1978-1989' 

    elif  1990 <= x.Year <= 1995:

        return '1990-1995' 


    elif  1996 <= x.Year <= 2000:

        return '1996-2000' 

    elif  2001 <= x.Year <= 2005:

        return '2001-2005' 
    
    elif  2006 <= x.Year <= 2010:

        return '2006-2010' 

    elif  2011 <= x.Year <= 2015:

        return '2011-2015' 
    
    elif  2016 <= x.Year <= 2020:

        return '2016-2020' 
    
    elif  2021 <= x.Year <= 2024:

        return '2021-2024'     
    


# df_merge['Year_group'] = df_merge.apply(lambda x: year_group(x) ,1 )



# Function to get time into seconds

def time_format_to_sec_time(x):



    if x.time_len == 2:


       corrected_time =   int(x.Time.split(':')[0].strip())*60 +   int(x.Time.split(':')[1].strip()) 
    

    elif x.time_len == 3:


       corrected_time =   int(x.Time.split(':')[0].strip())*60*60 +   int(x.Time.split(':')[1].strip())*60 +   int(x.Time.split(':')[1].strip()) 


    return corrected_time




# Function to clean gender

def gender_filter(x):


    if x in ('M','MAS','MU','M4', 'M3','M5', 'M2', 'M7', 'MU'):

        return 'M'
    
    elif x in ('F', 'F4', 'F5', 'F2', 'F3','F6'):

        return 'F'
    
    else:

        return ''
    

# df_merge['Sex'] = df_merge['Sex'].apply(lambda x: gender_filter(x)  )


# Functoin to clean Age Category

def age_cat_filter(x):


    if x in ('U19','U20','<20','-19'):

        return 'U20'
    
    elif x in ('20-29','25-29','20-24'):

        return '20-29'
    
    elif x in ('30-39','30-34','35-39'):

        return '30-39'
    
    elif x in ('40-49','40-44','45-49'):

        return '40-49'
    
    elif x in ('50-59','50-54','55-59'):

        return '50-59'

    elif x in ('60+','60-69','60-64','65-69'):

        return '60-69'

    elif x in ('70+','70-74','75-79'):

        return '70-79'
    
    elif x in ('80+','85+','80-84'):

        return '80+'

# df_merge['Age_Cat_fix'] = df_merge.Age_Cat.apply(lambda x: age_cat_filter(x),1  )



# Reading the Data

excel_file_path = r'C:\Users\Monk\Codebase\Tely 10\Tely 10 All Data v2.xlsx'
perc_90 = pd.read_excel(excel_file_path, sheet_name='10th Percentile')
perc_50 = pd.read_excel(excel_file_path, sheet_name='50th Percentile')
perc_10 = pd.read_excel(excel_file_path, sheet_name='90th Percentile')
all_data = pd.read_excel(excel_file_path, sheet_name='All Data')


# Plotting the data

# perc_90.groupby('Year_group').agg({'Mets':'mean'}).plot(kind = 'line', figsize=(8,5))
# perc_50.groupby('Year_group').agg({'Mets':'mean'}).plot(kind = 'line', figsize=(8,5))
# perc_10.groupby('Year_group').agg({'Mets':'mean'}).plot(kind = 'line', figsize=(8,5))





# 10th Percentile


model_10 = ols('Mets ~ C(Year) + Distance + Time_sec', data=perc_10).fit()
aov_table_10 = sm.stats.anova_lm(model_10, typ=2)
r2_10 = model_10.rsquared
print('RSqquare - ',r2_10)


# Tukey Table

tukey_perc_10 = pairwise_tukeyhsd(endog=perc_10['Mets'], groups=perc_10['Year_group'],alpha=0.05)
tukey_perc_10 = pd.DataFrame(tukey_perc_10.summary())


# Tukey Table
tukey_perc_10_columns = ['Group1','Group2','MeanDiff','p-adj','Lower','Upper','Rject']
tukey_perc_10.columns = tukey_perc_10_columns
tukey_perc_10 = tukey_perc_10[1:]

# Average Mets Over the years
perc_10_agg = perc_10.groupby('Year_group').agg({'Mets':'mean'}).reset_index()


# 50th Percentile

model_50 = ols('Mets ~ C(Year) + Distance + Time_sec ', data=perc_50).fit()
aov_table_50 = sm.stats.anova_lm(model_50, typ=2)
r2_50 = model_50.rsquared




tukey_perc_50 = pairwise_tukeyhsd(endog=perc_50['Mets'], groups=perc_50['Year_group'],alpha=0.05)
tukey_perc_50 = pd.DataFrame(tukey_perc_50.summary())


# Tukey Table
tukey_perc_50_columns = ['Group1','Group2','MeanDiff','p-adj','Lower','Upper','Rject']
tukey_perc_50.columns = tukey_perc_50_columns
tukey_perc_50 = tukey_perc_50[1:]

# Average Mets Over the years
perc_50_agg = perc_50.groupby('Year_group').agg({'Mets':'mean'}).reset_index()

# 90th Percentile

model_90 = ols('Mets ~ C(Year) + Distance + Time_sec ', data=perc_90).fit()
aov_table_90 = sm.stats.anova_lm(model_90, typ=2)
r2_90 = model_90.rsquared


tukey_perc_90 = pairwise_tukeyhsd(endog=perc_90['Mets'], groups=perc_90['Year_group'],alpha=0.05)
tukey_perc_90 = pd.DataFrame(tukey_perc_90.summary())

# Tukey Table
tukey_perc_90_columns = ['Group1','Group2','MeanDiff','p-adj','Lower','Upper','Rject']
tukey_perc_90.columns = tukey_perc_90_columns
tukey_perc_90 = tukey_perc_90[1:]

# Average Mets Over the years
perc_90_agg = perc_90.groupby('Year_group').agg({'Mets':'mean'}).reset_index()


# Saving all the data into Excel file.

writer = pd.ExcelWriter(r'C:\Users\Monk\Codebase\Tely 10\Statistics Tely 10.xlsx')

aov_table_10.to_excel(writer, sheet_name = 'ANOVA 10th')
print('10',r2_10)
tukey_perc_10.to_excel(writer, sheet_name = 'Tukey 10th')
perc_10_agg.to_excel(writer, sheet_name = 'Avg Data 10th')


aov_table_50.to_excel(writer, sheet_name = 'ANOVA 50th')
print('50',r2_50)
# r2_50.to_excel(writer, sheet_name = 'RSquare 50th')
tukey_perc_50.to_excel(writer, sheet_name = 'Tukey 50th')
perc_50_agg.to_excel(writer, sheet_name = 'Avg Data 50th')


aov_table_90.to_excel(writer, sheet_name = 'ANOVA 90th')
print('90',r2_90)
# r2_90.to_excel(writer, sheet_name = 'RSquare 90th')
tukey_perc_90.to_excel(writer, sheet_name = 'Tukey 90th')
perc_90_agg.to_excel(writer, sheet_name = 'Avg Data 90th')

writer.save()