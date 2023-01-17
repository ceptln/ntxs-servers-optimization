import pandas as pd
import os
import datetime

def weekday_num_to_letters(num: int) -> str:
    """
    Add weekday method
    """
    if num == 0:
        return "Monday"
    elif num == 1:
        return "Tuesday"
    elif num == 2:
        return "Wednesday"
    elif num == 3:
        return "Thursday"
    elif num == 4:
        return "Friday"
    elif num == 5:
        return "Saturday"
    else:
        return "Sunday"


def closest(lst, K) -> int:
    """
    Finds closest number in a given list to K
    """
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]


def dataset_daily_reports(data_mycloud, data_iteminfo, data_itemtrend, data_zabbix, data_cockpit) -> pd.DataFrame:

    """
    Creates the full-featured dataset with all daily observations on all servers.
    """
    data = data_itemtrend.merge(data_iteminfo, how='left', on='itemid', suffixes=['_global', '_detailed'])
    data = data.merge(data_zabbix, how='left', on='hostid')

    # Uppercase for merging operation
    data['host'] = data.host.apply(lambda id: id.upper())
    data = data.merge(data_cockpit, how='left', left_on='host', right_on='name_server')
    
    # Add weekday feature
    # Clock column into date
    format = "%Y-%m-%d"
    data["analysis_date"] = data.clock.apply(lambda input: datetime.datetime.strptime(input, format))
    data["weekday_num"] = data.analysis_date.apply(lambda date: date.weekday())
    data["weekday"] = data.weekday_num.apply(lambda num: weekday_num_to_letters(num))

    # Transform RAM mbytes into n_ram to join Mycloud Config
    data['n_ram'] = data.ram.apply(lambda mbytes: closest(data_mycloud.RAM.unique(), mbytes / 1000))
    data['key'] = data.apply(lambda row: f"{row.number_cpu}#{row.n_ram}", axis=1)
    data = data.merge(data_mycloud, how='left', on='key')
    data = data[data.Price.notna()]

    # Get only a year
    one_year_data = data[data.analysis_date >= datetime.datetime(2021, 12, 21)]
    one_year_data.sort_values(by='analysis_date')  

    return one_year_data

def server_wise_dataset(dataset_daily_reports: pd.DataFrame, data_cockpit: pd.DataFrame) -> pd.DataFrame:
    """
    Creates the server dataset to be filtered for identifying undersized & oversized servers.
    """

    ### Add all nedded features - To be completed ###
    # Get the mean, max and min of avg and spread
    data_grp = dataset_daily_reports.groupby(by=['name_server', 'item_type_global']).agg({'value_avg': ['mean', 'min', 'max']}).reset_index()
    data_grp.columns = ['name_server', 'item_type_global', 'value_avg_mean', 'value_avg_min', 'value_avg_max']
    data_grp['daily_avg_max_diff'] = data_grp['value_avg_max'] - data_grp['value_avg_min']
    # Get the std
    data_grouped_std = dataset_daily_reports.groupby(by=['name_server', 'item_type_global'])[['value_avg']].std().reset_index().rename(columns={'value_avg': 'value_avg_std'})
    # Get the nb days where max 100%
    data_grp_max100 = dataset_daily_reports.groupby(by=['name_server', 'item_type_global'])['value_max'].apply(lambda x: (x==100.000000).sum()).reset_index(name='days_max100')
    # Get the nb days where max 97%
    data_grp_max97 = dataset_daily_reports.groupby(by=['name_server', 'item_type_global'])['value_max'].apply(lambda x: (x>97).sum()).reset_index(name='days_max97')
    # Get the nb days where avg sup 95%
    data_grp_avg95 = dataset_daily_reports.groupby(by=['name_server', 'item_type_global'])['value_avg'].apply(lambda x: (x>=95).sum()).reset_index(name='days_avg_sup_95')
    # Get the nb days where avg under 10%
    data_grp_avg5 = dataset_daily_reports.groupby(by=['name_server', 'item_type_global'])['value_avg'].apply(lambda x: (x<=10).sum()).reset_index(name='days_avg_lower5')

    #### TO DO ###






    ###############

    rule_based_data = dataset_daily_reports[['name_server', 'model']].drop_duplicates()
    rule_based_data = rule_based_data.merge(dataset_daily_reports[['name_server', 'key', 'Price']], how='left', on='name_server').drop(columns='model').drop_duplicates()
    # Join environment
    rule_based_data = rule_based_data.merge(data_cockpit[['name_server', 'name_environment']], how='left', on='name_server')
    # Add CPU number
    rule_based_data['CPU'] = rule_based_data.key.apply(lambda key: int(key.partition("#")[0]))
    # Add RAM number
    rule_based_data['RAM'] = rule_based_data.key.apply(lambda key: int(key.partition("#")[2]))

    # Join CPU
    data_grp_cpu = data_grp[data_grp.item_type_global == 'cpu'].drop(columns='item_type_global')
    data_grouped_std_cpu = data_grouped_std[data_grouped_std.item_type_global == 'cpu'].drop(columns='item_type_global')
    data_grp_max100_cpu = data_grp_max100[data_grp_max100.item_type_global == 'cpu'].drop(columns='item_type_global')
    data_grp_avg95_cpu = data_grp_avg95[data_grp_avg95.item_type_global == 'cpu'].drop(columns='item_type_global')
    data_grp_avg5_cpu = data_grp_avg5[data_grp_avg5.item_type_global == 'cpu'].drop(columns='item_type_global')

    rule_based_data = rule_based_data.merge(data_grp_cpu, how='left', on='name_server')
    rule_based_data = rule_based_data.merge(data_grouped_std_cpu, how='left', on='name_server')
    rule_based_data = rule_based_data.merge(data_grp_max100_cpu, how='left', on='name_server')
    rule_based_data = rule_based_data.merge(data_grp_avg95_cpu, how='left', on='name_server')
    rule_based_data = rule_based_data.merge(data_grp_avg5_cpu, how='left', on='name_server')

    #### TO DO ###






    ###############

    # Join RAM values
    data_grp_mem = data_grp[data_grp.item_type_global == 'mem'].drop(columns='item_type_global')
    data_grouped_std_mem = data_grouped_std[data_grouped_std.item_type_global == 'mem'].drop(columns='item_type_global')
    data_grp_max97_mem = data_grp_max97[data_grp_max100.item_type_global == 'mem'].drop(columns='item_type_global')
    data_grp_avg95_mem = data_grp_avg95[data_grp_avg95.item_type_global == 'mem'].drop(columns='item_type_global')
    data_grp_avg5_mem = data_grp_avg5[data_grp_avg5.item_type_global == 'mem'].drop(columns='item_type_global')

    rule_based_data = rule_based_data.merge(data_grp_mem, how='left', on='name_server', suffixes=('_cpu', '_mem'))
    rule_based_data = rule_based_data.merge(data_grouped_std_mem, how='left', on='name_server', suffixes=('_cpu', '_mem'))
    rule_based_data = rule_based_data.merge(data_grp_max97_mem, how='left', on='name_server', suffixes=('_cpu', '_mem'))
    rule_based_data = rule_based_data.merge(data_grp_avg95_mem, how='left', on='name_server', suffixes=('_cpu', '_mem'))
    rule_based_data = rule_based_data.merge(data_grp_avg5_mem, how='left', on='name_server', suffixes=('_cpu', '_mem'))

    #### TO DO ###






    ###############

    rule_based_data = rule_based_data.drop_duplicates(subset='name_server')

    return rule_based_data