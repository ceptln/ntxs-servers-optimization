import pandas as pd
import os
import datetime
import json

# Get selected servers to change
cpu_undersized = pd.read_csv('data/final_data/cpu_undersized.csv')
cpu_oversized = pd.read_csv('data/final_data/cpu_oversized.csv')
ram_undersized = pd.read_csv('data/final_data/ram_undersized.csv')
ram_oversized = pd.read_csv('data/final_data/ram_oversized.csv')

cpu_undersized = cpu_undersized[['name_server', 'key', 'Price', 'CPU', 'RAM', 'name_environment', 'value_avg_mean_cpu', 'value_avg_mean_mem']]
ram_undersized = ram_undersized[['name_server', 'key', 'Price', 'CPU', 'RAM', 'name_environment', 'value_avg_mean_mem', 'value_avg_mean_cpu']]
cpu_oversized = cpu_oversized[['name_server', 'key', 'Price', 'CPU', 'RAM', 'name_environment', 'value_avg_mean_cpu', 'value_avg_mean_mem']]
ram_oversized = ram_oversized[['name_server', 'key', 'Price', 'CPU', 'RAM', 'name_environment', 'value_avg_mean_mem', 'value_avg_mean_cpu']]

# Get the bounds from JSON config file
file_object = open("config_file.json", "r")
json_content = file_object.read()
config_dict = json.loads(json_content)

undersized_bound_cpu = {'Prod': config_dict['CPU_UNDERSIZED']['Prod']["MIN_ANNUAL_DAILY_AVERAGE"], 'Bench': config_dict['CPU_UNDERSIZED']['Bench']["MIN_ANNUAL_DAILY_AVERAGE"], 'Dev': config_dict['CPU_UNDERSIZED']['Dev']["MIN_ANNUAL_DAILY_AVERAGE"], 'Test':config_dict['CPU_UNDERSIZED']['Test']["MIN_ANNUAL_DAILY_AVERAGE"], 'UAT':config_dict['CPU_UNDERSIZED']['UAT']["MIN_ANNUAL_DAILY_AVERAGE"]}
oversized_bound_cpu = {'Prod': config_dict['CPU_OVERSIZED']['Prod']["MAX_ANNUAL_DAILY_AVERAGE"], 'Bench': config_dict['CPU_OVERSIZED']['Bench']["MAX_ANNUAL_DAILY_AVERAGE"], 'Dev': config_dict['CPU_OVERSIZED']['Dev']["MAX_ANNUAL_DAILY_AVERAGE"], 'Test':config_dict['CPU_OVERSIZED']['Test']["MAX_ANNUAL_DAILY_AVERAGE"], 'UAT':config_dict['CPU_OVERSIZED']['UAT']["MAX_ANNUAL_DAILY_AVERAGE"]}
undersized_bound_ram = {'Prod': config_dict['RAM_UNDERSIZED']['Prod']["MIN_ANNUAL_DAILY_AVERAGE"], 'Bench': config_dict['RAM_UNDERSIZED']['Bench']["MIN_ANNUAL_DAILY_AVERAGE"], 'Dev': config_dict['RAM_UNDERSIZED']['Dev']["MIN_ANNUAL_DAILY_AVERAGE"], 'Test':config_dict['RAM_UNDERSIZED']['Test']["MIN_ANNUAL_DAILY_AVERAGE"], 'UAT':config_dict['RAM_UNDERSIZED']['UAT']["MIN_ANNUAL_DAILY_AVERAGE"]}
oversized_bound_ram = {'Prod': config_dict['RAM_OVERSIZED']['Prod']["MAX_ANNUAL_DAILY_AVERAGE"], 'Bench': config_dict['RAM_OVERSIZED']['Bench']["MAX_ANNUAL_DAILY_AVERAGE"], 'Dev': config_dict['RAM_OVERSIZED']['Dev']["MAX_ANNUAL_DAILY_AVERAGE"], 'Test':config_dict['RAM_OVERSIZED']['Test']["MAX_ANNUAL_DAILY_AVERAGE"], 'UAT':config_dict['RAM_OVERSIZED']['UAT']["MAX_ANNUAL_DAILY_AVERAGE"]}

# Get all configs prices
data_mycloud = pd.read_csv('data/raw_data/mycloud_20221221.csv')

# Dictionnaries of possible configs
mycloud_configs_cpu_to_ram = {
    1: [2, 4, 6, 8, 12, 16, 24, 32],
    2: [4, 8, 16, 24, 32, 64, 128],
    4: [8, 16, 24, 32, 64, 128],
    8: [16, 24, 32, 64, 128],
    12: [24, 32, 48, 64, 128],
    16: [32, 48, 64, 128]
}

mycloud_configs_ram_to_cpu = {
    2: [1],
    4: [1, 2],
    6: [1],
    8: [1, 2, 4],
    12: [1],
    16: [1, 2, 4, 8],
    24: [1, 2, 4, 8, 12],
    32: [1, 2, 4, 8, 12, 16],
    48: [12, 16],
    64: [2, 4, 8, 12, 16],
    128: [2, 4, 8, 12, 16]
}

def add_column_CPU_RAM(data_cpu: pd.DataFrame, data_ram: pd.DataFrame) -> pd.DataFrame:
    """
    Indicates if both CPU and RAM are undersized/oversized or not.
    """
    cpu_set = set(data_cpu['name_server'])
    ram_set = set(data_ram['name_server'])
    both_set = list(ram_set.intersection(cpu_set))

    data_cpu['both'] = data_cpu.name_server.apply(lambda name: True if name in both_set else False)
    data_ram['both'] = data_ram.name_server.apply(lambda name: True if name in both_set else False)

    return data_cpu, data_ram


def upper_value(num: int, list_values: list, check_same: bool=False) -> int:
    """
    Find upper bound of an int in a list
    """
    if check_same:
        listing = [item for item in list_values if item >= num]
    else:
        listing = [item for item in list_values if item > num]
    listing.sort()
    return listing[0]


def lower_value(num: int, list_values: list, check_same: bool=False) -> int:
    """
    Find upper bound of an int in a list
    """
    if check_same:
        listing = [item for item in list_values if item <= num]
    else:
        listing = [item for item in list_values if item < num]
    listing.sort(reverse=True)
    return listing[0]


def closest(lst, K) -> int:
    """
    Finds closest number in a given list to K
    """
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]


def config_change(row, cpu_bool: bool, undersized: bool):
    """
    Change config
    TO DO : ?? m??diter si on doit toujours d??croitre simple ou parfois double ET 
    si on doit toujours faire le moove m??me si ??a nous fait par exemple modifier la ram sans n??cessit?? 
    car la config du nv nb de cpu l'oblige (peut m??me ??tre dangereux sur une baisse de RAM)
    """
    
    cpu = row.CPU
    ram = row.RAM
    avg_mean_cpu = row.value_avg_mean_cpu
    avg_mean_ram = row.value_avg_mean_mem

    config_change_counter = 0

    if cpu_bool:
        if undersized:
            if row.both:
                while (avg_mean_cpu > undersized_bound_cpu[row.name_environment]) & (avg_mean_ram > undersized_bound_ram[row.name_environment]) & (cpu < max(list(mycloud_configs_cpu_to_ram.keys()))) & (ram < max(list(mycloud_configs_ram_to_cpu.keys()))):
                    config_change_counter += 1
                    old_cpu = cpu
                    old_ram = ram
                    cpu = upper_value(cpu, list(mycloud_configs_cpu_to_ram.keys()))
                    ram = upper_value(ram, mycloud_configs_cpu_to_ram[cpu])
                    avg_mean_cpu = avg_mean_cpu * (old_cpu / cpu)
                    avg_mean_ram = avg_mean_ram * (old_ram / ram)
                    
                while (avg_mean_cpu > undersized_bound_cpu[row.name_environment]) & (cpu < max(list(mycloud_configs_cpu_to_ram.keys()))):
                    config_change_counter += 1
                    old_cpu = cpu
                    old_ram = ram
                    cpu = upper_value(cpu, list(mycloud_configs_cpu_to_ram.keys()))
                    ram = upper_value(ram, mycloud_configs_cpu_to_ram[cpu], check_same=True)
                    avg_mean_cpu = avg_mean_cpu * (old_cpu / cpu)
                    avg_mean_ram = avg_mean_ram * (old_ram / ram)

                
                while (avg_mean_ram > undersized_bound_ram[row.name_environment]) & (ram < max(list(mycloud_configs_ram_to_cpu.keys()))):
                    config_change_counter += 1
                    old_cpu = cpu
                    old_ram = ram
                    ram = upper_value(ram, list(mycloud_configs_ram_to_cpu.keys()))
                    try:
                        cpu = upper_value(cpu, mycloud_configs_ram_to_cpu[ram], check_same=True)
                    except:
                        cpu = closest(mycloud_configs_ram_to_cpu[ram], cpu)
                    avg_mean_cpu = avg_mean_cpu * (old_cpu / cpu)
                    avg_mean_ram = avg_mean_ram * (old_ram / ram)
                return f"{cpu}#{ram}", cpu, ram, avg_mean_cpu, avg_mean_ram, config_change_counter
            else:
                while (avg_mean_cpu > undersized_bound_cpu[row.name_environment]) & (cpu < max(list(mycloud_configs_cpu_to_ram.keys()))):
                    config_change_counter += 1
                    old_cpu = cpu
                    old_ram = ram
                    cpu = upper_value(cpu, list(mycloud_configs_cpu_to_ram.keys()))
                    ram = upper_value(ram, mycloud_configs_cpu_to_ram[cpu], check_same=True)
                    avg_mean_cpu = avg_mean_cpu * (old_cpu / cpu)
                    avg_mean_ram = avg_mean_ram * (old_ram / ram)
                return f"{cpu}#{ram}", cpu, ram, avg_mean_cpu, avg_mean_ram, config_change_counter
        else:
            if row.both:
                while (avg_mean_cpu < oversized_bound_cpu[row.name_environment]) & (avg_mean_ram < oversized_bound_ram[row.name_environment]) & (ram > min(list(mycloud_configs_ram_to_cpu.keys()))) & (cpu > min(list(mycloud_configs_cpu_to_ram.keys()))):
                    config_change_counter += 1
                    old_cpu = cpu
                    old_ram = ram
                    cpu = lower_value(cpu, list(mycloud_configs_cpu_to_ram.keys()))
                    ram = lower_value(ram, mycloud_configs_cpu_to_ram[cpu])
                    avg_mean_cpu = avg_mean_cpu * (old_cpu / cpu)
                    avg_mean_ram = avg_mean_ram * (old_ram / ram)
                
                while (avg_mean_cpu < oversized_bound_cpu[row.name_environment]) & (cpu > min(list(mycloud_configs_cpu_to_ram.keys()))):
                    config_change_counter += 1
                    old_cpu = cpu
                    old_ram = ram
                    cpu = lower_value(cpu, list(mycloud_configs_cpu_to_ram.keys()))
                    ram = lower_value(ram, mycloud_configs_cpu_to_ram[cpu], check_same=True)
                    avg_mean_cpu = avg_mean_cpu * (old_cpu / cpu)
                    avg_mean_ram = avg_mean_ram * (old_ram / ram)
                
                while (avg_mean_ram < oversized_bound_ram[row.name_environment]) & (ram > min(list(mycloud_configs_ram_to_cpu.keys()))):
                    config_change_counter += 1
                    old_cpu = cpu
                    old_ram = ram
                    ram = lower_value(ram, list(mycloud_configs_ram_to_cpu.keys()))
                    try:
                        cpu = lower_value(cpu, mycloud_configs_ram_to_cpu[ram], check_same=True)
                    except:
                        cpu = closest(mycloud_configs_ram_to_cpu[ram], cpu)
                    avg_mean_cpu = avg_mean_cpu * (old_cpu / cpu)
                    avg_mean_ram = avg_mean_ram * (old_ram / ram)
                return f"{cpu}#{ram}", cpu, ram, avg_mean_cpu, avg_mean_ram, config_change_counter
            else:
                while (avg_mean_cpu < oversized_bound_cpu[row.name_environment]) & (cpu > min(list(mycloud_configs_cpu_to_ram.keys()))):
                    config_change_counter += 1
                    old_cpu = cpu
                    old_ram = ram
                    cpu = lower_value(cpu, list(mycloud_configs_cpu_to_ram.keys()))
                    ram = lower_value(ram, mycloud_configs_cpu_to_ram[cpu], check_same=True)
                    avg_mean_cpu = avg_mean_cpu * (old_cpu / cpu)
                    avg_mean_ram = avg_mean_ram * (old_ram / ram)
                return f"{cpu}#{ram}", cpu, ram, avg_mean_cpu, avg_mean_ram, config_change_counter
    else:
        if undersized:
            if row.both:
                while (avg_mean_cpu > undersized_bound_cpu[row.name_environment]) & (avg_mean_ram > undersized_bound_ram[row.name_environment]) & (cpu < max(list(mycloud_configs_cpu_to_ram.keys()))) & (ram < max(list(mycloud_configs_ram_to_cpu.keys()))):
                    config_change_counter += 1
                    old_cpu = cpu
                    old_ram = ram
                    cpu = upper_value(cpu, list(mycloud_configs_cpu_to_ram.keys()))
                    ram = upper_value(ram, mycloud_configs_cpu_to_ram[cpu])
                    avg_mean_cpu = avg_mean_cpu * (old_cpu / cpu)
                    avg_mean_ram = avg_mean_ram * (old_ram / ram)
       
                while (avg_mean_cpu > undersized_bound_cpu[row.name_environment]) & (cpu < max(list(mycloud_configs_cpu_to_ram.keys()))):
                    config_change_counter += 1
                    old_cpu = cpu
                    old_ram = ram
                    cpu = upper_value(cpu, list(mycloud_configs_cpu_to_ram.keys()))
                    ram = upper_value(ram, mycloud_configs_cpu_to_ram[cpu], check_same=True)
                    avg_mean_cpu = avg_mean_cpu * (old_cpu / cpu)
                    avg_mean_ram = avg_mean_ram * (old_ram / ram)
                
                while (avg_mean_ram > undersized_bound_ram[row.name_environment]) & (ram < max(list(mycloud_configs_ram_to_cpu.keys()))):
                    config_change_counter += 1
                    old_cpu = cpu
                    old_ram = ram
                    ram = upper_value(ram, list(mycloud_configs_ram_to_cpu.keys()))
                    try:
                        cpu = upper_value(cpu, mycloud_configs_ram_to_cpu[ram], check_same=True)
                    except:
                        cpu = closest(mycloud_configs_ram_to_cpu[ram], cpu)
                    avg_mean_cpu = avg_mean_cpu * (old_cpu / cpu)
                    avg_mean_ram = avg_mean_ram * (old_ram / ram)
                return f"{cpu}#{ram}", cpu, ram, avg_mean_cpu, avg_mean_ram, config_change_counter
            else:
                while (avg_mean_ram > undersized_bound_ram[row.name_environment]) & (ram < max(list(mycloud_configs_ram_to_cpu.keys()))):
                    config_change_counter += 1
                    old_cpu = cpu
                    old_ram = ram
                    ram = upper_value(ram, list(mycloud_configs_ram_to_cpu.keys()))
                    try:
                        cpu = upper_value(cpu, mycloud_configs_ram_to_cpu[ram], check_same=True)
                    except:
                        cpu = closest(mycloud_configs_ram_to_cpu[ram], cpu)
                    avg_mean_cpu = avg_mean_cpu * (old_cpu / cpu)
                    avg_mean_ram = avg_mean_ram * (old_ram / ram)
                return f"{cpu}#{ram}", cpu, ram, avg_mean_cpu, avg_mean_ram, config_change_counter
        else:
            if row.both:
                while (avg_mean_cpu < oversized_bound_cpu[row.name_environment]) & (avg_mean_ram < oversized_bound_ram[row.name_environment]) & (ram > min(list(mycloud_configs_ram_to_cpu.keys()))) & (cpu > min(list(mycloud_configs_cpu_to_ram.keys()))):
                    config_change_counter += 1
                    old_cpu = cpu
                    old_ram = ram
                    cpu = lower_value(cpu, list(mycloud_configs_cpu_to_ram.keys()))
                    ram = lower_value(ram, mycloud_configs_cpu_to_ram[cpu])
                    avg_mean_cpu = avg_mean_cpu * (old_cpu / cpu)
                    avg_mean_ram = avg_mean_ram * (old_ram / ram)

                while (avg_mean_cpu < oversized_bound_cpu[row.name_environment]) & (cpu > min(list(mycloud_configs_cpu_to_ram.keys()))):
                    config_change_counter += 1
                    old_cpu = cpu
                    old_ram = ram
                    cpu = lower_value(cpu, list(mycloud_configs_cpu_to_ram.keys()))
                    ram = lower_value(ram, mycloud_configs_cpu_to_ram[cpu], check_same=True)
                    avg_mean_cpu = avg_mean_cpu * (old_cpu / cpu)
                    avg_mean_ram = avg_mean_ram * (old_ram / ram)

                while (avg_mean_ram < oversized_bound_ram[row.name_environment]) & (ram > min(list(mycloud_configs_ram_to_cpu.keys()))):
                    config_change_counter += 1
                    old_cpu = cpu
                    old_ram = ram
                    ram = lower_value(ram, list(mycloud_configs_ram_to_cpu.keys()))
                    try:
                        cpu = lower_value(cpu, mycloud_configs_ram_to_cpu[ram], check_same=True)
                    except:
                        cpu = closest(mycloud_configs_ram_to_cpu[ram], cpu)
                    avg_mean_cpu = avg_mean_cpu * (old_cpu / cpu)
                    avg_mean_ram = avg_mean_ram * (old_ram / ram)
                return f"{cpu}#{ram}", cpu, ram, avg_mean_cpu, avg_mean_ram, config_change_counter
            else:
                while (avg_mean_ram < oversized_bound_ram[row.name_environment]) & (ram > min(list(mycloud_configs_ram_to_cpu.keys()))):
                    if (row.name_server == "SWDCFRQ75356") & (config_change_counter > 1):
                        print('Here')
                    config_change_counter += 1
                    old_cpu = cpu
                    old_ram = ram
                    ram = lower_value(ram, list(mycloud_configs_ram_to_cpu.keys()))
                    try:
                        cpu = lower_value(cpu, mycloud_configs_ram_to_cpu[ram], check_same=True)
                    except:
                        cpu = closest(mycloud_configs_ram_to_cpu[ram], cpu)
                    avg_mean_cpu = avg_mean_cpu * (old_cpu / cpu)
                    avg_mean_ram = avg_mean_ram * (old_ram / ram)
                return f"{cpu}#{ram}", cpu, ram, avg_mean_cpu, avg_mean_ram, config_change_counter
    

def add_columns_config_changes(dataset, undersized, cpu_bool) -> pd.DataFrame:
    """
    Add columns change in config
    """
    dataset['new_CPU'] = dataset['CPU']
    dataset['new_RAM'] = dataset['RAM']

    dataset['new_config'] = dataset.apply(lambda row: config_change(row, cpu_bool=cpu_bool, undersized=undersized)[0], axis=1)
    dataset['new_CPU'] = dataset.apply(lambda row: config_change(row, cpu_bool=cpu_bool, undersized=undersized)[1], axis=1)
    dataset['new_RAM'] = dataset.apply(lambda row: config_change(row, cpu_bool=cpu_bool, undersized=undersized)[2], axis=1)
    dataset['new_avg_mean_CPU'] = dataset.apply(lambda row: config_change(row, cpu_bool=cpu_bool, undersized=undersized)[3], axis=1)
    dataset['new_avg_mean_RAM'] = dataset.apply(lambda row: config_change(row, cpu_bool=cpu_bool, undersized=undersized)[4], axis=1)
    dataset['n_change_iterations'] = dataset.apply(lambda row: config_change(row, cpu_bool=cpu_bool, undersized=undersized)[5], axis=1)

    if cpu_bool:
        dataset['unnecessary_change_in_ram'] = dataset.apply(lambda row: row.new_RAM - row.RAM,axis=1)
    else:
        dataset['unnecessary_change_in_cpu'] = dataset.apply(lambda row: row.new_CPU - row.CPU,axis=1)

    return dataset


# Create dataframe for each category, will be Excel tab
cpu_undersized, ram_undersized = add_column_CPU_RAM(cpu_undersized, ram_undersized)
cpu_undersized = add_columns_config_changes(cpu_undersized, undersized=True, cpu_bool=True)
ram_undersized = add_columns_config_changes(ram_undersized, undersized=True, cpu_bool=False)
cpu_oversized, ram_oversized = add_column_CPU_RAM(cpu_oversized, ram_oversized)
cpu_oversized = add_columns_config_changes(cpu_oversized, undersized=False, cpu_bool=True)
ram_oversized = add_columns_config_changes(ram_oversized, undersized=False, cpu_bool=False)

# Create dataframe with all server and prices evolution
cpu_u_for_join = cpu_undersized[['name_server', 'key', 'Price', 'new_config']]
cpu_o_for_join = cpu_oversized[['name_server', 'key', 'Price', 'new_config']]
ram_u_for_join = ram_undersized[['name_server', 'key', 'Price', 'new_config']]
ram_o_for_join = ram_oversized[['name_server', 'key', 'Price', 'new_config']]

all_changes = pd.concat([cpu_u_for_join, cpu_o_for_join, ram_u_for_join, ram_o_for_join], axis=0).drop_duplicates(subset='name_server')
all_changes = all_changes.merge(data_mycloud[['key', 'Price']], left_on='new_config', right_on='key', how='left', suffixes=['_old', '_new'])
all_changes['price_delta'] =  all_changes['Price_new'] - all_changes['Price_old']

# Creating the Excel
writer = pd.ExcelWriter("data/excels/change_config.xlsx", engine='xlsxwriter')

cpu_undersized.to_excel(writer, sheet_name='CPU undersized', startrow=1, header=False)
cpu_oversized.to_excel(writer, sheet_name='CPU oversized', startrow=1, header=False)
ram_undersized.to_excel(writer, sheet_name='RAM undersized', startrow=1, header=False)
ram_oversized.to_excel(writer, sheet_name='RAM oversized', startrow=1, header=False)
all_changes.to_excel(writer, sheet_name='Expenses variation', startrow=1, header=False)

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet_CPU_u = writer.sheets['CPU undersized']
worksheet_CPU_o = writer.sheets['CPU oversized']
worksheet_RAM_u = writer.sheets['RAM undersized']
worksheet_RAM_o = writer.sheets['RAM oversized']
worksheet_pricing = writer.sheets['Expenses variation']

# Add a header format.
header_format = workbook.add_format({
    'bold': True,
    'text_wrap': True,
    'valign': 'top',
    'fg_color': '#D7E4BC',
    'border': 1})

# Write the column headers with the defined format.
for col_num, value in enumerate(cpu_undersized.columns.values):
    worksheet_CPU_u.write(0, col_num + 1, value, header_format)
for col_num, value in enumerate(cpu_oversized.columns.values):
    worksheet_CPU_o.write(0, col_num + 1, value, header_format)
for col_num, value in enumerate(ram_undersized.columns.values):
    worksheet_RAM_u.write(0, col_num + 1, value, header_format)
for col_num, value in enumerate(ram_oversized.columns.values):
    worksheet_RAM_o.write(0, col_num + 1, value, header_format)
for col_num, value in enumerate(all_changes.columns.values):
    worksheet_pricing.write(0, col_num + 1, value, header_format)

# Close the Pandas Excel writer and output the Excel file.
writer.close()