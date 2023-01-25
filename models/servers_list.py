import pandas as pd
import os
import datetime
import json

# Get config file
file_object = open("config_file.json", "r")
json_content = file_object.read()
config_dict = json.loads(json_content)

# Get servers dataset
data = pd.read_csv("data/final_data/server_wise_dataset.csv")


# Filtering dataset to get CPU, RAM oversized & undersized

# CPU undersized
cpu_undersized_mask = ((data.name_environment == list(config_dict['CPU_UNDERSIZED'].keys())[0]) & (data.CPU <  config_dict['CPU_UNDERSIZED']['Prod']['MAX_N_CPU']) & (data.value_avg_mean_cpu > config_dict['CPU_UNDERSIZED']['Prod']['MIN_ANNUAL_DAILY_AVERAGE']) &(data.days_max100 > config_dict['CPU_UNDERSIZED']['Prod']['MIN_DAYS_WITH_SATURATION'])) | (
    (data.name_environment == list(config_dict['CPU_UNDERSIZED'].keys())[1]) & (data.CPU <  config_dict['CPU_UNDERSIZED']['Bench']['MAX_N_CPU']) &  (data.value_avg_mean_cpu > config_dict['CPU_UNDERSIZED']['Bench']['MIN_ANNUAL_DAILY_AVERAGE']) &  (data.days_max100 > config_dict['CPU_UNDERSIZED']['Prod']['MIN_DAYS_WITH_SATURATION'])) | (
    (data.name_environment == list(config_dict['CPU_UNDERSIZED'].keys())[2]) & (data.CPU <  config_dict['CPU_UNDERSIZED']['Test']['MAX_N_CPU']) & (data.value_avg_mean_cpu > config_dict['CPU_UNDERSIZED']['Test']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 > config_dict['CPU_UNDERSIZED']['Prod']['MIN_DAYS_WITH_SATURATION'])) |(
    (data.name_environment == list(config_dict['CPU_UNDERSIZED'].keys())[3]) & (data.CPU <  config_dict['CPU_UNDERSIZED']['Dev']['MAX_N_CPU']) & (data.value_avg_mean_cpu > config_dict['CPU_UNDERSIZED']['Dev']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 > config_dict['CPU_UNDERSIZED']['Prod']['MIN_DAYS_WITH_SATURATION'])) | (
    (data.name_environment == list(config_dict['CPU_UNDERSIZED'].keys())[4]) & (data.CPU <  config_dict['CPU_UNDERSIZED']['UAT']['MAX_N_CPU']) & (data.value_avg_mean_cpu > config_dict['CPU_UNDERSIZED']['UAT']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 > config_dict['CPU_UNDERSIZED']['Prod']['MIN_DAYS_WITH_SATURATION']))
                      
data_cpu_undersized = data[cpu_undersized_mask].drop(columns=['Unnamed: 0'])
data_cpu_undersized.to_csv('data/final_data/cpu_undersized.csv')

# CPU oversized
cpu_oversized_mask = ((data.name_environment == list(config_dict['CPU_OVERSIZED'].keys())[0]) & (data.CPU >  config_dict['CPU_OVERSIZED']['Prod']['MIN_N_CPU']) & (data.value_avg_mean_cpu < config_dict['CPU_OVERSIZED']['Prod']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 > config_dict['CPU_OVERSIZED']['Prod']['MAX_DAYS_WITH_SATURATION'])) |(
    (data.name_environment == list(config_dict['CPU_OVERSIZED'].keys())[1]) & (data.CPU >  config_dict['CPU_OVERSIZED']['Bench']['MIN_N_CPU']) & (data.value_avg_mean_cpu < config_dict['CPU_OVERSIZED']['Bench']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 < config_dict['CPU_OVERSIZED']['Prod']['MAX_DAYS_WITH_SATURATION'])) |(
    (data.name_environment == list(config_dict['CPU_OVERSIZED'].keys())[2]) & (data.CPU >  config_dict['CPU_OVERSIZED']['Test']['MIN_N_CPU']) & (data.value_avg_mean_cpu < config_dict['CPU_OVERSIZED']['Test']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 < config_dict['CPU_OVERSIZED']['Prod']['MAX_DAYS_WITH_SATURATION'])) |(
    (data.name_environment == list(config_dict['CPU_OVERSIZED'].keys())[3]) & (data.CPU >  config_dict['CPU_OVERSIZED']['Dev']['MIN_N_CPU']) & (data.value_avg_mean_cpu < config_dict['CPU_OVERSIZED']['Dev']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 < config_dict['CPU_OVERSIZED']['Prod']['MAX_DAYS_WITH_SATURATION'])) |(
    (data.name_environment == list(config_dict['CPU_OVERSIZED'].keys())[4]) & (data.CPU >  config_dict['CPU_OVERSIZED']['UAT']['MIN_N_CPU']) & (data.value_avg_mean_cpu < config_dict['CPU_OVERSIZED']['UAT']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 < config_dict['CPU_OVERSIZED']['Prod']['MAX_DAYS_WITH_SATURATION']))
data_cpu_oversized = data[cpu_oversized_mask].drop(columns=['Unnamed: 0'])
data_cpu_oversized.to_csv('data/final_data/cpu_oversized.csv')

# MEM undersized
mem_undersized_mask = ((data.name_environment == list(config_dict['RAM_UNDERSIZED'].keys())[0]) & (data.RAM <  config_dict['RAM_UNDERSIZED']['Prod']['MAX_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_UNDERSIZED']['Prod']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max97> config_dict['RAM_UNDERSIZED']['Prod']['MIN_DAYS_WITH_MAX_OVER97'])) |(
    (data.name_environment == list(config_dict['RAM_UNDERSIZED'].keys())[1]) & (data.RAM <  config_dict['RAM_UNDERSIZED']['Bench']['MAX_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_UNDERSIZED']['Bench']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 > config_dict['RAM_UNDERSIZED']['Prod']['MIN_DAYS_WITH_MAX_OVER97'])) |(
    (data.name_environment == list(config_dict['RAM_UNDERSIZED'].keys())[2]) & (data.RAM <  config_dict['RAM_UNDERSIZED']['Test']['MAX_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_UNDERSIZED']['Test']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 > config_dict['RAM_UNDERSIZED']['Prod']['MIN_DAYS_WITH_MAX_OVER97'])) |(
    (data.name_environment == list(config_dict['RAM_UNDERSIZED'].keys())[3]) & (data.RAM <  config_dict['RAM_UNDERSIZED']['Dev']['MAX_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_UNDERSIZED']['Dev']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 > config_dict['RAM_UNDERSIZED']['Prod']['MIN_DAYS_WITH_MAX_OVER97'])) |(
    (data.name_environment == list(config_dict['RAM_UNDERSIZED'].keys())[4]) & (data.RAM <  config_dict['RAM_UNDERSIZED']['UAT']['MAX_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_UNDERSIZED']['UAT']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 > config_dict['RAM_UNDERSIZED']['Prod']['MIN_DAYS_WITH_MAX_OVER97']))
data_mem_undersized = data[mem_undersized_mask].drop(columns=['Unnamed: 0'])
data_mem_undersized.to_csv('data/final_data/ram_undersized.csv')

# MEM oversized
mem_oversized_mask = ((data.name_environment == list(config_dict['RAM_OVERSIZED'].keys())[0]) & (data.RAM <  config_dict['RAM_OVERSIZED']['Prod']['MIN_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_OVERSIZED']['Prod']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max97> config_dict['RAM_OVERSIZED']['Prod']['MAX_DAYS_WITH_MAX_OVER97'])) |(
    (data.name_environment == list(config_dict['RAM_OVERSIZED'].keys())[1]) & (data.RAM >  config_dict['RAM_OVERSIZED']['Bench']['MIN_N_RAM']) & (data.value_avg_mean_mem < config_dict['RAM_OVERSIZED']['Bench']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 < config_dict['RAM_OVERSIZED']['Prod']['MAX_DAYS_WITH_MAX_OVER97'])) |(
    (data.name_environment == list(config_dict['RAM_OVERSIZED'].keys())[2]) & (data.RAM >  config_dict['RAM_OVERSIZED']['Test']['MIN_N_RAM']) & (data.value_avg_mean_mem < config_dict['RAM_OVERSIZED']['Test']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 < config_dict['RAM_OVERSIZED']['Prod']['MAX_DAYS_WITH_MAX_OVER97'])) |(
    (data.name_environment == list(config_dict['RAM_OVERSIZED'].keys())[3]) & (data.RAM >  config_dict['RAM_OVERSIZED']['Dev']['MIN_N_RAM']) & (data.value_avg_mean_mem < config_dict['RAM_OVERSIZED']['Dev']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 < config_dict['RAM_OVERSIZED']['Prod']['MAX_DAYS_WITH_MAX_OVER97'])) |(
    (data.name_environment == list(config_dict['RAM_OVERSIZED'].keys())[4]) & (data.RAM >  config_dict['RAM_OVERSIZED']['UAT']['MIN_N_RAM']) & (data.value_avg_mean_mem < config_dict['RAM_OVERSIZED']['UAT']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 < config_dict['RAM_OVERSIZED']['Prod']['MAX_DAYS_WITH_MAX_OVER97']))
data_mem_oversized = data[mem_oversized_mask].drop(columns=['Unnamed: 0'])
data_mem_oversized.to_csv('data/final_data/ram_oversized.csv')

# Creating the Excel
writer = pd.ExcelWriter("data/excels/servers_list.xlsx", engine='xlsxwriter')

data_cpu_undersized.to_excel(writer, sheet_name='CPU undersized', startrow=1, header=False)
data_cpu_oversized.to_excel(writer, sheet_name='CPU oversized', startrow=1, header=False)
data_mem_undersized.to_excel(writer, sheet_name='RAM undersized', startrow=1, header=False)
data_mem_oversized.to_excel(writer, sheet_name='RAM oversized', startrow=1, header=False)

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet_CPU_u = writer.sheets['CPU undersized']
worksheet_CPU_o = writer.sheets['CPU oversized']
worksheet_RAM_u = writer.sheets['RAM undersized']
worksheet_RAM_o = writer.sheets['RAM oversized']

# Add a header format.
header_format = workbook.add_format({
    'bold': True,
    'text_wrap': True,
    'valign': 'top',
    'fg_color': '#D7E4BC',
    'border': 1})

# Write the column headers with the defined format.
for col_num, value in enumerate(data_cpu_undersized.columns.values):
    worksheet_CPU_u.write(0, col_num + 1, value, header_format)
for col_num, value in enumerate(data_cpu_oversized.columns.values):
    worksheet_CPU_o.write(0, col_num + 1, value, header_format)
for col_num, value in enumerate(data_mem_undersized.columns.values):
    worksheet_RAM_u.write(0, col_num + 1, value, header_format)
for col_num, value in enumerate(data_mem_oversized.columns.values):
    worksheet_RAM_o.write(0, col_num + 1, value, header_format)

# Close the Pandas Excel writer and output the Excel file.
writer.close()