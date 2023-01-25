import pandas as pd
from models.utils import dataset_daily_reports, server_wise_dataset, create_servers_list, add_column_CPU_RAM, add_columns_config_changes
import json

RAW_DATA_PATH = 'data/raw_data/'

cockpit_file_path = RAW_DATA_PATH + 'cockpit_20221221.csv'
item_info_file_path = RAW_DATA_PATH + 'item_info_20221221.csv'
item_trend_file_path = RAW_DATA_PATH + 'item_trend_20221221.csv'
my_cloud_file_path = RAW_DATA_PATH + 'mycloud_20221221.csv'
tmp_hosts_zabbix_file_path = RAW_DATA_PATH + 'tmp_hosts_zabbix_20221221.csv'

def create_server_wise_dataset(cockpit_file_path: str, item_info_file_path: str, item_trend_file_path: str, 
                               my_cloud_file_path: str, tmp_hosts_zabbix_file_path: str, csv_export=False) -> pd.DataFrame:
    # Load the data                           
    data_mycloud = pd.read_csv(my_cloud_file_path).drop(columns=['Unnamed: 0'])
    data_iteminfo = pd.read_csv(item_info_file_path).drop(columns=['Unnamed: 0'])
    data_itemtrend = pd.read_csv(item_trend_file_path).drop(columns=['Unnamed: 0'])
    data_zabbix = pd.read_csv(tmp_hosts_zabbix_file_path).drop(columns=['Unnamed: 0'])
    data_cockpit = pd.read_csv(cockpit_file_path).drop(columns=['Unnamed: 0']).drop_duplicates(subset=['name_server'])
    # Daily Reports Dataset
    daily_dataset = dataset_daily_reports(data_mycloud, data_iteminfo, data_itemtrend, data_zabbix, data_cockpit)
    # Server Wise Dataset
    server_wise_dataset_df = server_wise_dataset(daily_dataset, data_cockpit)
    if csv_export:
        daily_dataset.to_csv('data/final_data/daily_reports_dataset.csv')
        server_wise_dataset_df.to_csv('data/final_data/server_wise_dataset.csv')
    return server_wise_dataset_df

def optimize_servers(server_wise_dataset_df: pd.DataFrame, config_dict: dict, csv_export=False) -> pd.DataFrame:
    
    cpu_undersized, cpu_oversized, ram_undersized, ram_oversized = create_servers_list(server_wise_dataset_df, config_dict)

    data_mycloud = pd.read_csv('data/default_input_files/mycloud_20221221.csv')

    cpu_undersized, ram_undersized = add_column_CPU_RAM(cpu_undersized, ram_undersized)
    cpu_undersized = add_columns_config_changes(cpu_undersized, undersized=True, cpu_bool=True, config_dict=config_dict)
    ram_undersized = add_columns_config_changes(ram_undersized, undersized=True, cpu_bool=False, config_dict=config_dict)
    cpu_oversized, ram_oversized = add_column_CPU_RAM(cpu_oversized, ram_oversized)
    cpu_oversized = add_columns_config_changes(cpu_oversized, undersized=False, cpu_bool=True, config_dict=config_dict)
    ram_oversized = add_columns_config_changes(ram_oversized, undersized=False, cpu_bool=False, config_dict=config_dict)

    # Create dataframe with all server and prices evolution
    cpu_u_for_join = cpu_undersized[['name_server', 'key', 'Price', 'value_avg_mean_cpu', 'value_avg_mean_mem', 'new_config', 'new_avg_mean_CPU', 'new_avg_mean_RAM']]
    cpu_o_for_join = cpu_oversized[['name_server', 'key', 'Price', 'value_avg_mean_cpu', 'value_avg_mean_mem','new_config', 'new_avg_mean_CPU', 'new_avg_mean_RAM']]
    ram_u_for_join = ram_undersized[['name_server', 'key', 'Price', 'value_avg_mean_cpu', 'value_avg_mean_mem','new_config', 'new_avg_mean_CPU', 'new_avg_mean_RAM']]
    ram_o_for_join = ram_oversized[['name_server', 'key', 'Price', 'value_avg_mean_cpu', 'value_avg_mean_mem', 'new_config', 'new_avg_mean_CPU', 'new_avg_mean_RAM']]

    all_changes = pd.concat([cpu_u_for_join, cpu_o_for_join, ram_u_for_join, ram_o_for_join], axis=0).drop_duplicates(subset='name_server')
    all_changes = all_changes.merge(data_mycloud[['key', 'Price']], left_on='new_config', right_on='key', how='left', suffixes=['_old', '_new'])
    all_changes['price_delta'] =  all_changes['Price_new'] - all_changes['Price_old']
    if csv_export:
        all_changes.to_csv('data/final_data/all_changes.csv')
    return all_changes

if __name__ == '__main__':
    # Create the server wise dataset
    server_wise_dataset_df = create_server_wise_dataset(cockpit_file_path, item_info_file_path, item_trend_file_path, 
                                                       my_cloud_file_path, tmp_hosts_zabbix_file_path, csv_export=False)
    # Load the default config file                                                   
    by_default_config_file = open("data/default_input_files/config_file.json", "r")
    by_default_config_dict = json.loads(by_default_config_file.read())
    # Optimize the servers
    all_changes = optimize_servers(server_wise_dataset_df, by_default_config_dict, csv_export=False)
    print(all_changes)

