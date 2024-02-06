# import pandas as pd

# def number_of_anxiety_cases(df):
#     ### Calculates the number of anxiety cases in the dataset
#     return
    
# def number_of_drugs_cases(df)L
#     return #your code here

# def number_of_depression_cases(df):
#     return #your code here

# # initialize pandas dataframe with the column names year, anixety_cases, drugs_cases, depression_cases
# compiled_data = pd.DataFrame(columns=['year', 'anxiety_cases', 'drugs_cases', 'depression_cases'])
# all_files = ['2015.csv', '2016.csv', '2017.csv', '2018.csv', '2019.csv']


# for file in all_files:
#     df = pd.read_csv(file)
    
#     year = get_year(df)
#     anxiety_cases = number_of_anxiety_cases(df)
#     drugs_cases = number_of_drugs_cases(df)
#     depression_cases = number_of_depression_cases(df)
    
#     # append the data to the dataframe
#     compiled_data = compiled_data.append({'year': year, 'anxiety_cases': anxiety_cases, 'drugs_cases': drugs_cases, 'depression_cases': depression_cases}, ignore_index=True)
    
import pandas as pd

df = pd.read_csv('resources/raw_data/Rate of Aggravated Assault Offenses Per 100000 by Population_02-01-2024.csv')

df[2,1:2]