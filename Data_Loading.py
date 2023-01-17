import streamlit as st
import pandas as pd
from utils import dataset_daily_reports, server_wise_dataset

cockpit_file = st.file_uploader("Upload the cockpit file")
item_info_file = st.file_uploader("Upload the item info file")
item_trend_file = st.file_uploader("Uploaed the item trend file")
my_cloud_file = st.file_uploader("Upload the mycloud file")
tmp_hosts_zabbix_file = st.file_uploader("Upload the zabbix file")

if all([my_cloud_file, item_info_file, item_trend_file, tmp_hosts_zabbix_file, cockpit_file]):

    data_mycloud = pd.read_csv(my_cloud_file).drop(columns=['Unnamed: 0'])

    data_iteminfo = pd.read_csv(item_info_file).drop(columns=['Unnamed: 0'])

    data_itemtrend = pd.read_csv(item_trend_file).drop(columns=['Unnamed: 0'])

    data_zabbix = pd.read_csv(tmp_hosts_zabbix_file).drop(columns=['Unnamed: 0'])

    data_cockpit = pd.read_csv(cockpit_file).drop(columns=['Unnamed: 0']).drop_duplicates(subset=['name_server'])

    daily_dataset = dataset_daily_reports(data_mycloud, data_iteminfo, data_itemtrend, data_zabbix, data_cockpit)
    daily_dataset.to_csv('data/final_data/daily_reports_dataset.csv')
    server_wise_dataset_df = server_wise_dataset(daily_dataset, data_cockpit)
    server_wise_dataset_df.to_csv('data/final_data/server_wise_dataset.csv')