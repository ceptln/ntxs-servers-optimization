import pandas as pd

N_CPU_MIN_VALUE = 1
N_CPU_MAX_VALUE = 16
N_RAM_MIN_VALUE = 2
N_RAM_MAX_VALUE = 128

def create_servers_list(data: pd.DataFrame, config_dict: dict)-> tuple[pd.DataFrame]:
    """
    Create dataframes of servers that are undersized or oversized
    Input:
    - data: server-wise dataframe 
    - config_dict: dictionary of thresholds
    Output:
    - cpu_undersized: dataframe of servers that are undersized
    - cpu_oversized: dataframe of servers that are oversized
    - ram_undersized: dataframe of servers that are undersized
    - ram_oversized: dataframe of servers that are oversized
    """
    cpu_undersized_mask = ((data.name_environment == list(config_dict['CPU_UNDERSIZED'].keys())[0]) & (data.CPU <  config_dict['CPU_UNDERSIZED']['Prod']['MAX_N_CPU']) & (data.value_avg_mean_cpu > config_dict['CPU_UNDERSIZED']['Prod']['MIN_ANNUAL_DAILY_AVERAGE']) &(data.days_max100 > config_dict['CPU_UNDERSIZED']['Prod']['MIN_DAYS_WITH_SATURATION'])) | (
        (data.name_environment == list(config_dict['CPU_UNDERSIZED'].keys())[1]) & (data.CPU <  config_dict['CPU_UNDERSIZED']['Bench']['MAX_N_CPU']) &  (data.value_avg_mean_cpu > config_dict['CPU_UNDERSIZED']['Bench']['MIN_ANNUAL_DAILY_AVERAGE']) &  (data.days_max100 > config_dict['CPU_UNDERSIZED']['Prod']['MIN_DAYS_WITH_SATURATION'])) | (
        (data.name_environment == list(config_dict['CPU_UNDERSIZED'].keys())[2]) & (data.CPU <  config_dict['CPU_UNDERSIZED']['Test']['MAX_N_CPU']) & (data.value_avg_mean_cpu > config_dict['CPU_UNDERSIZED']['Test']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 > config_dict['CPU_UNDERSIZED']['Prod']['MIN_DAYS_WITH_SATURATION'])) |(
        (data.name_environment == list(config_dict['CPU_UNDERSIZED'].keys())[3]) & (data.CPU <  config_dict['CPU_UNDERSIZED']['Dev']['MAX_N_CPU']) & (data.value_avg_mean_cpu > config_dict['CPU_UNDERSIZED']['Dev']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 > config_dict['CPU_UNDERSIZED']['Prod']['MIN_DAYS_WITH_SATURATION'])) | (
        (data.name_environment == list(config_dict['CPU_UNDERSIZED'].keys())[4]) & (data.CPU <  config_dict['CPU_UNDERSIZED']['UAT']['MAX_N_CPU']) & (data.value_avg_mean_cpu > config_dict['CPU_UNDERSIZED']['UAT']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 > config_dict['CPU_UNDERSIZED']['Prod']['MIN_DAYS_WITH_SATURATION']))                      
    cpu_undersized = data[cpu_undersized_mask].drop(columns=['Unnamed: 0'])

        # CPU oversized
    cpu_oversized_mask = ((data.name_environment == list(config_dict['CPU_OVERSIZED'].keys())[0]) & (data.CPU >  config_dict['CPU_OVERSIZED']['Prod']['MIN_N_CPU']) & (data.value_avg_mean_cpu < config_dict['CPU_OVERSIZED']['Prod']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 > config_dict['CPU_OVERSIZED']['Prod']['MAX_DAYS_WITH_SATURATION'])) |(
        (data.name_environment == list(config_dict['CPU_OVERSIZED'].keys())[1]) & (data.CPU >  config_dict['CPU_OVERSIZED']['Bench']['MIN_N_CPU']) & (data.value_avg_mean_cpu < config_dict['CPU_OVERSIZED']['Bench']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 < config_dict['CPU_OVERSIZED']['Prod']['MAX_DAYS_WITH_SATURATION'])) |(
        (data.name_environment == list(config_dict['CPU_OVERSIZED'].keys())[2]) & (data.CPU >  config_dict['CPU_OVERSIZED']['Test']['MIN_N_CPU']) & (data.value_avg_mean_cpu < config_dict['CPU_OVERSIZED']['Test']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 < config_dict['CPU_OVERSIZED']['Prod']['MAX_DAYS_WITH_SATURATION'])) |(
        (data.name_environment == list(config_dict['CPU_OVERSIZED'].keys())[3]) & (data.CPU >  config_dict['CPU_OVERSIZED']['Dev']['MIN_N_CPU']) & (data.value_avg_mean_cpu < config_dict['CPU_OVERSIZED']['Dev']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 < config_dict['CPU_OVERSIZED']['Prod']['MAX_DAYS_WITH_SATURATION'])) |(
        (data.name_environment == list(config_dict['CPU_OVERSIZED'].keys())[4]) & (data.CPU >  config_dict['CPU_OVERSIZED']['UAT']['MIN_N_CPU']) & (data.value_avg_mean_cpu < config_dict['CPU_OVERSIZED']['UAT']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 < config_dict['CPU_OVERSIZED']['Prod']['MAX_DAYS_WITH_SATURATION']))
    cpu_oversized = data[cpu_oversized_mask].drop(columns=['Unnamed: 0'])

    # MEM undersized
    ram_undersized_mask = ((data.name_environment == list(config_dict['RAM_UNDERSIZED'].keys())[0]) & (data.RAM <  config_dict['RAM_UNDERSIZED']['Prod']['MAX_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_UNDERSIZED']['Prod']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max97> config_dict['RAM_UNDERSIZED']['Prod']['MIN_DAYS_WITH_MAX_OVER97'])) |(
        (data.name_environment == list(config_dict['RAM_UNDERSIZED'].keys())[1]) & (data.RAM <  config_dict['RAM_UNDERSIZED']['Bench']['MAX_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_UNDERSIZED']['Bench']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 > config_dict['RAM_UNDERSIZED']['Prod']['MIN_DAYS_WITH_MAX_OVER97'])) |(
        (data.name_environment == list(config_dict['RAM_UNDERSIZED'].keys())[2]) & (data.RAM <  config_dict['RAM_UNDERSIZED']['Test']['MAX_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_UNDERSIZED']['Test']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 > config_dict['RAM_UNDERSIZED']['Prod']['MIN_DAYS_WITH_MAX_OVER97'])) |(
        (data.name_environment == list(config_dict['RAM_UNDERSIZED'].keys())[3]) & (data.RAM <  config_dict['RAM_UNDERSIZED']['Dev']['MAX_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_UNDERSIZED']['Dev']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 > config_dict['RAM_UNDERSIZED']['Prod']['MIN_DAYS_WITH_MAX_OVER97'])) |(
        (data.name_environment == list(config_dict['RAM_UNDERSIZED'].keys())[4]) & (data.RAM <  config_dict['RAM_UNDERSIZED']['UAT']['MAX_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_UNDERSIZED']['UAT']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 > config_dict['RAM_UNDERSIZED']['Prod']['MIN_DAYS_WITH_MAX_OVER97']))
    ram_undersized = data[ram_undersized_mask].drop(columns=['Unnamed: 0'])

    # MEM oversized
    ram_oversized_mask = ((data.name_environment == list(config_dict['RAM_OVERSIZED'].keys())[0]) & (data.RAM <  config_dict['RAM_OVERSIZED']['Prod']['MIN_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_OVERSIZED']['Prod']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max97> config_dict['RAM_OVERSIZED']['Prod']['MAX_DAYS_WITH_MAX_OVER97'])) |(
        (data.name_environment == list(config_dict['RAM_OVERSIZED'].keys())[1]) & (data.RAM >  config_dict['RAM_OVERSIZED']['Bench']['MIN_N_RAM']) & (data.value_avg_mean_mem < config_dict['RAM_OVERSIZED']['Bench']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 < config_dict['RAM_OVERSIZED']['Prod']['MAX_DAYS_WITH_MAX_OVER97'])) |(
        (data.name_environment == list(config_dict['RAM_OVERSIZED'].keys())[2]) & (data.RAM >  config_dict['RAM_OVERSIZED']['Test']['MIN_N_RAM']) & (data.value_avg_mean_mem < config_dict['RAM_OVERSIZED']['Test']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 < config_dict['RAM_OVERSIZED']['Prod']['MAX_DAYS_WITH_MAX_OVER97'])) |(
        (data.name_environment == list(config_dict['RAM_OVERSIZED'].keys())[3]) & (data.RAM >  config_dict['RAM_OVERSIZED']['Dev']['MIN_N_RAM']) & (data.value_avg_mean_mem < config_dict['RAM_OVERSIZED']['Dev']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 < config_dict['RAM_OVERSIZED']['Prod']['MAX_DAYS_WITH_MAX_OVER97'])) |(
        (data.name_environment == list(config_dict['RAM_OVERSIZED'].keys())[4]) & (data.RAM >  config_dict['RAM_OVERSIZED']['UAT']['MIN_N_RAM']) & (data.value_avg_mean_mem < config_dict['RAM_OVERSIZED']['UAT']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 < config_dict['RAM_OVERSIZED']['Prod']['MAX_DAYS_WITH_MAX_OVER97']))
    ram_oversized = data[ram_oversized_mask].drop(columns=['Unnamed: 0'])

    # Run the steps from mycloud_config_optimizer.py
    cpu_undersized = cpu_undersized[['name_server', 'key', 'Price', 'CPU', 'RAM', 'name_environment', 'value_avg_mean_cpu', 'value_avg_mean_mem']]
    ram_undersized = ram_undersized[['name_server', 'key', 'Price', 'CPU', 'RAM', 'name_environment', 'value_avg_mean_mem', 'value_avg_mean_cpu']]
    cpu_oversized = cpu_oversized[['name_server', 'key', 'Price', 'CPU', 'RAM', 'name_environment', 'value_avg_mean_cpu', 'value_avg_mean_mem']]
    ram_oversized = ram_oversized[['name_server', 'key', 'Price', 'CPU', 'RAM', 'name_environment', 'value_avg_mean_mem', 'value_avg_mean_cpu']]

    return cpu_undersized, cpu_oversized, ram_undersized, ram_oversized


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


def config_change(row, cpu_bool: bool, undersized: bool, config_dict: dict):
    """
    Change config
    TO DO : à méditer si on doit toujours décroitre simple ou parfois double ET 
    si on doit toujours faire le moove même si ça nous fait par exemple modifier la ram sans nécessité 
    car la config du nv nb de cpu l'oblige (peut même être dangereux sur une baisse de RAM)
    """

    undersized_bound_cpu = {'Prod': config_dict['CPU_UNDERSIZED']['Prod']["MIN_ANNUAL_DAILY_AVERAGE"], 'Bench': config_dict['CPU_UNDERSIZED']['Bench']["MIN_ANNUAL_DAILY_AVERAGE"], 'Dev': config_dict['CPU_UNDERSIZED']['Dev']["MIN_ANNUAL_DAILY_AVERAGE"], 'Test':config_dict['CPU_UNDERSIZED']['Test']["MIN_ANNUAL_DAILY_AVERAGE"], 'UAT':config_dict['CPU_UNDERSIZED']['UAT']["MIN_ANNUAL_DAILY_AVERAGE"]}
    oversized_bound_cpu = {'Prod': config_dict['CPU_OVERSIZED']['Prod']["MAX_ANNUAL_DAILY_AVERAGE"], 'Bench': config_dict['CPU_OVERSIZED']['Bench']["MAX_ANNUAL_DAILY_AVERAGE"], 'Dev': config_dict['CPU_OVERSIZED']['Dev']["MAX_ANNUAL_DAILY_AVERAGE"], 'Test':config_dict['CPU_OVERSIZED']['Test']["MAX_ANNUAL_DAILY_AVERAGE"], 'UAT':config_dict['CPU_OVERSIZED']['UAT']["MAX_ANNUAL_DAILY_AVERAGE"]}
    undersized_bound_ram = {'Prod': config_dict['RAM_UNDERSIZED']['Prod']["MIN_ANNUAL_DAILY_AVERAGE"], 'Bench': config_dict['RAM_UNDERSIZED']['Bench']["MIN_ANNUAL_DAILY_AVERAGE"], 'Dev': config_dict['RAM_UNDERSIZED']['Dev']["MIN_ANNUAL_DAILY_AVERAGE"], 'Test':config_dict['RAM_UNDERSIZED']['Test']["MIN_ANNUAL_DAILY_AVERAGE"], 'UAT':config_dict['RAM_UNDERSIZED']['UAT']["MIN_ANNUAL_DAILY_AVERAGE"]}
    oversized_bound_ram = {'Prod': config_dict['RAM_OVERSIZED']['Prod']["MAX_ANNUAL_DAILY_AVERAGE"], 'Bench': config_dict['RAM_OVERSIZED']['Bench']["MAX_ANNUAL_DAILY_AVERAGE"], 'Dev': config_dict['RAM_OVERSIZED']['Dev']["MAX_ANNUAL_DAILY_AVERAGE"], 'Test':config_dict['RAM_OVERSIZED']['Test']["MAX_ANNUAL_DAILY_AVERAGE"], 'UAT':config_dict['RAM_OVERSIZED']['UAT']["MAX_ANNUAL_DAILY_AVERAGE"]}
    
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
    

def add_columns_config_changes(dataset, undersized, cpu_bool, config_dict: dict) -> pd.DataFrame:
    """
    Add columns change in config
    """
    dataset['new_CPU'] = dataset['CPU']
    dataset['new_RAM'] = dataset['RAM']

    dataset['new_config'] = dataset.apply(lambda row: config_change(row, cpu_bool=cpu_bool, undersized=undersized, config_dict=config_dict)[0], axis=1)
    dataset['new_CPU'] = dataset.apply(lambda row: config_change(row, cpu_bool=cpu_bool, undersized=undersized, config_dict=config_dict)[1], axis=1)
    dataset['new_RAM'] = dataset.apply(lambda row: config_change(row, cpu_bool=cpu_bool, undersized=undersized, config_dict=config_dict)[2], axis=1)
    dataset['new_avg_mean_CPU'] = dataset.apply(lambda row: config_change(row, cpu_bool=cpu_bool, undersized=undersized, config_dict=config_dict)[3], axis=1)
    dataset['new_avg_mean_RAM'] = dataset.apply(lambda row: config_change(row, cpu_bool=cpu_bool, undersized=undersized, config_dict=config_dict)[4], axis=1)
    dataset['n_change_iterations'] = dataset.apply(lambda row: config_change(row, cpu_bool=cpu_bool, undersized=undersized, config_dict=config_dict)[5], axis=1)

    if cpu_bool:
        dataset['unnecessary_change_in_ram'] = dataset.apply(lambda row: row.new_RAM - row.RAM,axis=1)
    else:
        dataset['unnecessary_change_in_cpu'] = dataset.apply(lambda row: row.new_CPU - row.CPU,axis=1)

    return dataset