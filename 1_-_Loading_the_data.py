import streamlit as st
import pandas as pd
from models.utils import dataset_daily_reports, server_wise_dataset

### SIDEBAR
# for i in range(8):
#     st.sidebar.title(" ")
st.sidebar.markdown(f"<h3 style='text-align: left;'>💻 Our work</h3>", unsafe_allow_html=True)
st.sidebar.info("GitHub Repository: <https://github.com/ceptln/ntxs-servers-optimization>")

st.sidebar.markdown(f"<h3 style='text-align: left;'>📬 Contact</h3>", unsafe_allow_html=True)
markdown = """
camille.epitalon@hec.edu
charles.proye@hec.edu
martin.quievre@hec.edu
nathan.aim@hec.edu
sarah.mayer@hec.edu
"""
st.sidebar.info(markdown)


### MAIN PAGE
col1, col2, col3 = st.columns(3)
col1.write("")
col2.image(
    ".streamlit/natixis.png",
    width=200,
)
col3.write("")

st.markdown(f"<h1 style='text-align: center;'>DATA LOADING</h1>", unsafe_allow_html=True)

cockpit_file = st.file_uploader("Upload the cockpit file", type=["csv"])
item_info_file = st.file_uploader("Upload the item info file", type=["csv"])
item_trend_file = st.file_uploader("Uploaed the item trend file", type=["csv"])
my_cloud_file = st.file_uploader("Upload the mycloud file", type=["csv"])
tmp_hosts_zabbix_file = st.file_uploader("Upload the zabbix file", type=["csv"])

if all([my_cloud_file, item_info_file, item_trend_file, tmp_hosts_zabbix_file, cockpit_file]):

    if st.button("Create dataset"):
        with st.spinner("Creating dataset..."):

            data_mycloud = pd.read_csv(my_cloud_file).drop(columns=['Unnamed: 0'])

            data_iteminfo = pd.read_csv(item_info_file).drop(columns=['Unnamed: 0'])

            data_itemtrend = pd.read_csv(item_trend_file).drop(columns=['Unnamed: 0'])

            data_zabbix = pd.read_csv(tmp_hosts_zabbix_file).drop(columns=['Unnamed: 0'])

            data_cockpit = pd.read_csv(cockpit_file).drop(columns=['Unnamed: 0']).drop_duplicates(subset=['name_server'])

            daily_dataset = dataset_daily_reports(data_mycloud, data_iteminfo, data_itemtrend, data_zabbix, data_cockpit)
            daily_dataset.to_csv('data/final_data/daily_reports_dataset.csv')
            server_wise_dataset_df = server_wise_dataset(daily_dataset, data_cockpit)
            # server_wise_dataset_df.to_csv('data/final_data/server_wise_dataset.csv')

        st.success("Done! You can download the csv file")

        st.dataframe(data=server_wise_dataset_df, width=None, height=None, use_container_width=True)

        csv = server_wise_dataset_df.to_csv(index=False).encode('utf-8')
        cols = st.columns(3)
        cols[1].download_button(
            "Download the csv file here 📂",
            csv,
            "server_wise_dataset.csv",
            "text/csv",
            key='download-csv',
        )