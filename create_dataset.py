import pandas as pd
import os
from utils import server_wise_dataset, dataset_daily_reports


# Get raw data
csvs = os.listdir("data/raw_data")[0:]
csvs = ['data/raw_data/' + csv for csv in csvs]
data_mycloud = pd.read_csv(csvs[0]).drop(columns=['Unnamed: 0'])
data_iteminfo = pd.read_csv(csvs[1]).drop(columns=['Unnamed: 0'])
data_itemtrend = pd.read_csv(csvs[2]).drop(columns=['Unnamed: 0'])
data_zabbix = pd.read_csv(csvs[3]).drop(columns=['Unnamed: 0'])
data_cockpit = pd.read_csv(csvs[4]).drop(columns=['Unnamed: 0']).drop_duplicates(subset=['name_server'])

if __name__ == '__main__':
    # Creating csv files
    daily_dataset = dataset_daily_reports(data_mycloud, data_iteminfo, data_itemtrend, data_zabbix, data_cockpit)
    daily_dataset.to_csv('data/final_data/daily_reports_dataset.csv')
    server_wise_dataset_df = server_wise_dataset(daily_dataset)
    server_wise_dataset_df.to_csv('data/final_data/server_wise_dataset.csv')