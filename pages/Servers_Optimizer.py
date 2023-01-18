import streamlit as st
import pandas as pd
import json
import utils

# This code is different for each deployed app.
CURRENT_THEME = "blue"
IS_DARK_THEME = True

col1, col2, col3 = st.columns(3)
col1.write("")
col2.image(
    ".streamlit/natixis.png",
    width=200,
)
col3.write("")

st.markdown(f"<h1 style='text-align: center;'>Servers Optimizer</hc1>", unsafe_allow_html=True)

# Upload server wise CSV file
st.header("Upload the Servers file")
data = st.file_uploader('Upload the "server wise" CSV', accept_multiple_files=False,
                                   type=["csv"], label_visibility="collapsed")

# Set up the parameters to replace config_file.json
st.header("Set up the parameters")
st.markdown(f"<p style='color:#333333'>You have the choice here: manually set up the parameters or upload a config file at the bottom.</p>", unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align: left;'>CPU Undersized</h4>", unsafe_allow_html=True)

by_default_config_file = open("default_input_files/config_file.json", "r")
json_content = by_default_config_file.read()
by_default_config_dict = json.loads(json_content)

# CP Udersized config

## Head of the columns
cols = st.columns(4)
with cols[1]:
    st.markdown(f"<p style='color:#333333'>Max number of CPU</p>", unsafe_allow_html=True)
with cols[2]:
    st.markdown(f"<p style='color:#333333'>Min days with saturation</p>", unsafe_allow_html=True)
with cols[3]:
    st.markdown(f"<p style='color:#333333'>Min annual daily avg</p>", unsafe_allow_html=True)

## Production
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>Production</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_N_CPU = st.number_input("Max number of CPU", min_value=utils.N_CPU_MIN_VALUE, max_value=utils.N_CPU_MAX_VALUE, value=by_default_config_dict['CPU_UNDERSIZED']['Prod']['MAX_N_CPU'], step=None, format=None, key=1, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAYS_WITH_SATURATION = st.number_input("Min days with saturation", min_value=0, max_value=365, value=by_default_config_dict['CPU_UNDERSIZED']['Prod']['MIN_DAYS_WITH_SATURATION'], step=None, format=None, key=2, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MIN_ANNUAL_DAILY_AVERAGE = st.number_input("Min annual daily average", min_value=0, max_value=100, value=by_default_config_dict['CPU_UNDERSIZED']['Prod']['MIN_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=3, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
prod = {"MAX_N_CPU": MAX_N_CPU,
        "MIN_DAYS_WITH_SATURATION": MIN_DAYS_WITH_SATURATION,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE}

## Bench
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>Bench</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_N_CPU = st.number_input("Max number of CPU", min_value=utils.N_CPU_MIN_VALUE, max_value=utils.N_CPU_MAX_VALUE, value=by_default_config_dict['CPU_UNDERSIZED']['Bench']['MAX_N_CPU'], step=None, format=None, key=4, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAYS_WITH_SATURATION = st.number_input("Min days with saturation", min_value=0, max_value=365, value=by_default_config_dict['CPU_UNDERSIZED']['Bench']['MIN_DAYS_WITH_SATURATION'], step=None, format=None, key=5, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MIN_ANNUAL_DAILY_AVERAGE = st.number_input("Min annual daily average", min_value=0, max_value=100, value=by_default_config_dict['CPU_UNDERSIZED']['Bench']['MIN_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=6, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
bench = {"MAX_N_CPU": MAX_N_CPU,
        "MIN_DAYS_WITH_SATURATION": MIN_DAYS_WITH_SATURATION,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE}

## Test
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>Test</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_N_CPU = st.number_input("Max number of CPU", min_value=utils.N_CPU_MIN_VALUE, max_value=utils.N_CPU_MAX_VALUE, value=by_default_config_dict['CPU_UNDERSIZED']['Test']['MAX_N_CPU'], step=None, format=None, key=7, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAYS_WITH_SATURATION = st.number_input("Min days with saturation", min_value=0, max_value=365, value=by_default_config_dict['CPU_UNDERSIZED']['Test']['MIN_DAYS_WITH_SATURATION'], step=None, format=None, key=8, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MIN_ANNUAL_DAILY_AVERAGE = st.number_input("Min annual daily average", min_value=0, max_value=100, value=by_default_config_dict['CPU_UNDERSIZED']['Test']['MIN_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=9, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
test = {"MAX_N_CPU": MAX_N_CPU,
        "MIN_DAYS_WITH_SATURATION": MIN_DAYS_WITH_SATURATION,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE}

## Dev
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>Dev</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_N_CPU = st.number_input("Max number of CPU", min_value=utils.N_CPU_MIN_VALUE, max_value=utils.N_CPU_MAX_VALUE, value=by_default_config_dict['CPU_UNDERSIZED']['Dev']['MAX_N_CPU'], step=None, format=None, key=10, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAYS_WITH_SATURATION = st.number_input("Min days with saturation", min_value=0, max_value=365, value=by_default_config_dict['CPU_UNDERSIZED']['Dev']['MIN_DAYS_WITH_SATURATION'], step=None, format=None, key=11, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MIN_ANNUAL_DAILY_AVERAGE = st.number_input("Min annual daily average", min_value=0, max_value=100, value=by_default_config_dict['CPU_UNDERSIZED']['Dev']['MIN_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=12, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
dev = {"MAX_N_CPU": MAX_N_CPU,
        "MIN_DAYS_WITH_SATURATION": MIN_DAYS_WITH_SATURATION,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE}

## UAT
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>UAT</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_N_CPU = st.number_input("Max number of CPU", min_value=utils.N_CPU_MIN_VALUE, max_value=utils.N_CPU_MAX_VALUE, value=by_default_config_dict['CPU_UNDERSIZED']['UAT']['MAX_N_CPU'], step=None, format=None, key=13, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAYS_WITH_SATURATION = st.number_input("Min days with saturation", min_value=0, max_value=365, value=by_default_config_dict['CPU_UNDERSIZED']['UAT']['MIN_DAYS_WITH_SATURATION'], step=None, format=None, key=14, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MIN_ANNUAL_DAILY_AVERAGE = st.number_input("Min annual daily average", min_value=0, max_value=100, value=by_default_config_dict['CPU_UNDERSIZED']['UAT']['MIN_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=15, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
uat = {"MAX_N_CPU": MAX_N_CPU,
        "MIN_DAYS_WITH_SATURATION": MIN_DAYS_WITH_SATURATION,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE}

cpu_undersized = {"Prod": prod,
                  "Bench": bench,
                  "Test": test,
                  "Dev": dev,
                  "UAT": uat}

# CPU Oversized config
st.markdown(f"<h4 style='text-align: left;'>CPU Oversized</h4>", unsafe_allow_html=True)

cols = st.columns(4)
with cols[1]:
    st.markdown(f"<p style='color:#333333'>Min number of CPU</p>", unsafe_allow_html=True)
with cols[2]:
    st.markdown(f"<p style='color:#333333'>Max days with satur.</p>", unsafe_allow_html=True)
with cols[3]:
    st.markdown(f"<p style='color:#333333'>Max annual daily avg</p>", unsafe_allow_html=True)

## Production
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>Production</p>", unsafe_allow_html=True)
with cols[1]:
    MIN_N_CPU = st.number_input("Max number of CPU", min_value=utils.N_CPU_MIN_VALUE, max_value=utils.N_CPU_MAX_VALUE, value=by_default_config_dict['CPU_OVERSIZED']['Prod']['MIN_N_CPU'], step=None, format=None, key=16, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MAX_DAYS_WITH_SATURATION = st.number_input("Max days with saturation", min_value=0, max_value=365, value=by_default_config_dict['CPU_OVERSIZED']['Prod']['MAX_DAYS_WITH_SATURATION'], step=None, format=None, key=17, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_ANNUAL_DAILY_AVERAGE = st.number_input("Max annual daily average", min_value=0, max_value=100, value=by_default_config_dict['CPU_OVERSIZED']['Prod']['MAX_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=18, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
prod = {"MIN_N_CPU": MIN_N_CPU,
        "MAX_DAYS_WITH_SATURATION": MAX_DAYS_WITH_SATURATION,
        "MAX_ANNUAL_DAILY_AVERAGE": MAX_ANNUAL_DAILY_AVERAGE}

## Bench
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>Bench</p>", unsafe_allow_html=True)
with cols[1]:
    MIN_N_CPU = st.number_input("Max number of CPU", min_value=utils.N_CPU_MIN_VALUE, max_value=utils.N_CPU_MAX_VALUE, value=by_default_config_dict['CPU_OVERSIZED']['Bench']['MIN_N_CPU'], step=None, format=None, key=19, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MAX_DAYS_WITH_SATURATION = st.number_input("Max days with saturation", min_value=0, max_value=365, value=by_default_config_dict['CPU_OVERSIZED']['Bench']['MAX_DAYS_WITH_SATURATION'], step=None, format=None, key=20, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_ANNUAL_DAILY_AVERAGE = st.number_input("Max annual daily average", min_value=0, max_value=100, value=by_default_config_dict['CPU_OVERSIZED']['Bench']['MAX_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=21, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
bench = {"MIN_N_CPU": MIN_N_CPU,
        "MAX_DAYS_WITH_SATURATION": MAX_DAYS_WITH_SATURATION,
        "MAX_ANNUAL_DAILY_AVERAGE": MAX_ANNUAL_DAILY_AVERAGE}

## Test
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>Test</p>", unsafe_allow_html=True)
with cols[1]:
    MIN_N_CPU = st.number_input("Max number of CPU", min_value=utils.N_CPU_MIN_VALUE, max_value=utils.N_CPU_MAX_VALUE, value=by_default_config_dict['CPU_OVERSIZED']['Test']['MIN_N_CPU'], step=None, format=None, key=22, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MAX_DAYS_WITH_SATURATION = st.number_input("Max days with saturation", min_value=0, max_value=365, value=by_default_config_dict['CPU_OVERSIZED']['Test']['MAX_DAYS_WITH_SATURATION'], step=None, format=None, key=23, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_ANNUAL_DAILY_AVERAGE = st.number_input("Max annual daily average", min_value=0, max_value=100, value=by_default_config_dict['CPU_OVERSIZED']['Test']['MAX_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=24, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
test = {"MIN_N_CPU": MIN_N_CPU,
        "MAX_DAYS_WITH_SATURATION": MAX_DAYS_WITH_SATURATION,
        "MAX_ANNUAL_DAILY_AVERAGE": MAX_ANNUAL_DAILY_AVERAGE}

## Dev
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>Dev</p>", unsafe_allow_html=True)
with cols[1]:
    MIN_N_CPU = st.number_input("Max number of CPU", min_value=utils.N_CPU_MIN_VALUE, max_value=utils.N_CPU_MAX_VALUE, value=by_default_config_dict['CPU_OVERSIZED']['Dev']['MIN_N_CPU'], step=None, format=None, key=25, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MAX_DAYS_WITH_SATURATION = st.number_input("Max days with saturation", min_value=0, max_value=365, value=by_default_config_dict['CPU_OVERSIZED']['Dev']['MAX_DAYS_WITH_SATURATION'], step=None, format=None, key=26, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_ANNUAL_DAILY_AVERAGE = st.number_input("Max annual daily average", min_value=0, max_value=100, value=by_default_config_dict['CPU_OVERSIZED']['Dev']['MAX_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=27, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
dev = {"MIN_N_CPU": MIN_N_CPU,
        "MAX_DAYS_WITH_SATURATION": MAX_DAYS_WITH_SATURATION,
        "MAX_ANNUAL_DAILY_AVERAGE": MAX_ANNUAL_DAILY_AVERAGE}

## UAT
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>UAT</p>", unsafe_allow_html=True)
with cols[1]:
    MIN_N_CPU = st.number_input("Max number of CPU", min_value=utils.N_CPU_MIN_VALUE, max_value=utils.N_CPU_MAX_VALUE, value=by_default_config_dict['CPU_OVERSIZED']['UAT']['MIN_N_CPU'], step=None, format=None, key=28, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MAX_DAYS_WITH_SATURATION = st.number_input("Max days with saturation", min_value=0, max_value=365, value=by_default_config_dict['CPU_OVERSIZED']['UAT']['MAX_DAYS_WITH_SATURATION'], step=None, format=None, key=29, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_ANNUAL_DAILY_AVERAGE = st.number_input("Max annual daily average", min_value=0, max_value=100, value=by_default_config_dict['CPU_OVERSIZED']['UAT']['MAX_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=30, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
uat = {"MIN_N_CPU": MAX_N_CPU,
        "MAX_DAYS_WITH_SATURATION": MAX_DAYS_WITH_SATURATION,
        "MAX_ANNUAL_DAILY_AVERAGE": MAX_ANNUAL_DAILY_AVERAGE}

cpu_oversized = {"Prod": prod,
                  "Bench": bench,
                  "Test": test,
                  "Dev": dev,
                  "UAT": uat}


# RAM Undersized config
st.markdown(f"<h4 style='text-align: left;'>RAM Undersized</h4>", unsafe_allow_html=True)
cols = st.columns(4)
with cols[1]:
    st.markdown(f"<p style='color:#333333'>Max RAM</p>", unsafe_allow_html=True)
with cols[2]:
    st.markdown(f"<p style='color:#333333'>Min daily average</p>", unsafe_allow_html=True)
with cols[3]:
    st.markdown(f"<p style='color:#333333'>Min days over 97%</p>", unsafe_allow_html=True)


## Production
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>Production</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_N_RAM = st.number_input("Max RAM", min_value=utils.N_RAM_MIN_VALUE, max_value=utils.N_RAM_MAX_VALUE, value=by_default_config_dict['RAM_UNDERSIZED']['Prod']['MAX_N_RAM'], step=None, format=None, key=31, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_ANNUAL_DAILY_AVERAGE= st.number_input("Min daily average", min_value=2, max_value=100, value=by_default_config_dict['RAM_UNDERSIZED']['Prod']['MIN_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=32, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MIN_DAYS_WITH_MAX_OVER97 = st.number_input("Min days over 97%", min_value=0, max_value=365, value=by_default_config_dict['RAM_UNDERSIZED']['Prod']['MIN_DAYS_WITH_MAX_OVER97'], step=None, format=None, key=33, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
prod = {"MAX_N_RAM": MAX_N_RAM,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE,
        "MIN_DAYS_WITH_MAX_OVER97": MIN_DAYS_WITH_MAX_OVER97}

## Bench
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>Bench</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_N_RAM = st.number_input("Max RAM", min_value=utils.N_RAM_MIN_VALUE, max_value=utils.N_RAM_MAX_VALUE, value=by_default_config_dict['RAM_UNDERSIZED']['Bench']['MAX_N_RAM'], step=None, format=None, key=34, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_ANNUAL_DAILY_AVERAGE= st.number_input("Min daily average", min_value=2, max_value=100, value=by_default_config_dict['RAM_UNDERSIZED']['Bench']['MIN_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=35, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MIN_DAYS_WITH_MAX_OVER97 = st.number_input("Min days over 97%", min_value=0, max_value=365, value=by_default_config_dict['RAM_UNDERSIZED']['Bench']['MIN_DAYS_WITH_MAX_OVER97'], step=None, format=None, key=36, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
bench = {"MAX_N_RAM": MAX_N_RAM,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE,
        "MIN_DAYS_WITH_MAX_OVER97": MIN_DAYS_WITH_MAX_OVER97}

## Test
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>Test</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_N_RAM = st.number_input("Max RAM", min_value=utils.N_RAM_MIN_VALUE, max_value=utils.N_RAM_MAX_VALUE, value=by_default_config_dict['RAM_UNDERSIZED']['Test']['MAX_N_RAM'], step=None, format=None, key=37, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_ANNUAL_DAILY_AVERAGE= st.number_input("Min daily average", min_value=2, max_value=100, value=by_default_config_dict['RAM_UNDERSIZED']['Test']['MIN_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=38, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MIN_DAYS_WITH_MAX_OVER97 = st.number_input("Min days over 97%", min_value=0, max_value=365, value=by_default_config_dict['RAM_UNDERSIZED']['Test']['MIN_DAYS_WITH_MAX_OVER97'], step=None, format=None, key=39, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
test = {"MAX_N_RAM": MAX_N_RAM,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE,
        "MIN_DAYS_WITH_MAX_OVER97": MIN_DAYS_WITH_MAX_OVER97}

## Dev
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>Dev</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_N_RAM = st.number_input("Max RAM", min_value=utils.N_RAM_MIN_VALUE, max_value=utils.N_RAM_MAX_VALUE, value=by_default_config_dict['RAM_UNDERSIZED']['Dev']['MAX_N_RAM'], step=None, format=None, key=40, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_ANNUAL_DAILY_AVERAGE= st.number_input("Min daily average", min_value=2, max_value=100, value=by_default_config_dict['RAM_UNDERSIZED']['Dev']['MIN_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=41, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MIN_DAYS_WITH_MAX_OVER97 = st.number_input("Min days over 97%", min_value=0, max_value=365, value=by_default_config_dict['RAM_UNDERSIZED']['Dev']['MIN_DAYS_WITH_MAX_OVER97'], step=None, format=None, key=42, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
dev = {"MAX_N_RAM": MAX_N_RAM,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE,
        "MIN_DAYS_WITH_MAX_OVER97": MIN_DAYS_WITH_MAX_OVER97}

## UAT
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>UAT</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_N_RAM = st.number_input("Max RAM", min_value=utils.N_RAM_MIN_VALUE, max_value=utils.N_RAM_MAX_VALUE, value=by_default_config_dict['RAM_UNDERSIZED']['UAT']['MAX_N_RAM'], step=None, format=None, key=43, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_ANNUAL_DAILY_AVERAGE= st.number_input("Min daily average", min_value=2, max_value=100, value=by_default_config_dict['RAM_UNDERSIZED']['UAT']['MIN_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=44, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MIN_DAYS_WITH_MAX_OVER97 = st.number_input("Min days over 97%", min_value=0, max_value=365, value=by_default_config_dict['RAM_UNDERSIZED']['UAT']['MIN_DAYS_WITH_MAX_OVER97'], step=None, format=None, key=45, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
uat = {"MAX_N_RAM": MAX_N_RAM,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE,
        "MIN_DAYS_WITH_MAX_OVER97": MIN_DAYS_WITH_MAX_OVER97}
ram_undersized = {"Prod": prod,
                  "Bench": bench,
                  "Test": test,
                  "Dev": dev,
                  "UAT": uat}

# RAM Oversized config
st.markdown(f"<h4 style='text-align: left;'>RAM Oversized</h4>", unsafe_allow_html=True)

cols = st.columns(4)
with cols[1]:
    st.markdown(f"<p style='color:#333333'>Min RAM</p>", unsafe_allow_html=True)
with cols[2]:
    st.markdown(f"<p style='color:#333333'>Max daily average</p>", unsafe_allow_html=True)
with cols[3]:
    st.markdown(f"<p style='color:#333333'>Max days over 97%</p>", unsafe_allow_html=True)

## Production
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>Production</p>", unsafe_allow_html=True)
with cols[1]:
    MIN_N_RAM = st.number_input("Max RAM", min_value=utils.N_RAM_MIN_VALUE, max_value=utils.N_RAM_MAX_VALUE, value=by_default_config_dict['RAM_OVERSIZED']['Prod']['MIN_N_RAM'], step=None, format=None, key=46, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MAX_ANNUAL_DAILY_AVERAGE= st.number_input("Min daily average", min_value=0, max_value=100, value=by_default_config_dict['RAM_OVERSIZED']['Prod']['MAX_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=47, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_DAYS_WITH_MAX_OVER97 = st.number_input("Min days over 97%", min_value=0, max_value=365, value=by_default_config_dict['RAM_OVERSIZED']['Prod']['MAX_DAYS_WITH_MAX_OVER97'], step=None, format=None, key=48, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
prod = {"MIN_N_RAM": MIN_N_RAM,
        "MAX_ANNUAL_DAILY_AVERAGE": MAX_ANNUAL_DAILY_AVERAGE,
        "MAX_DAYS_WITH_MAX_OVER97": MAX_DAYS_WITH_MAX_OVER97}

## Bench
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>Bench</p>", unsafe_allow_html=True)
with cols[1]:
    MIN_N_RAM = st.number_input("Max RAM", min_value=utils.N_RAM_MIN_VALUE, max_value=utils.N_RAM_MAX_VALUE, value=by_default_config_dict['RAM_OVERSIZED']['Bench']['MIN_N_RAM'], step=None, format=None, key=49, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MAX_ANNUAL_DAILY_AVERAGE= st.number_input("Min daily average", min_value=0, max_value=100, value=by_default_config_dict['RAM_OVERSIZED']['Bench']['MAX_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=50, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_DAYS_WITH_MAX_OVER97 = st.number_input("Min days over 97%", min_value=0, max_value=365, value=by_default_config_dict['RAM_OVERSIZED']['Bench']['MAX_DAYS_WITH_MAX_OVER97'], step=None, format=None, key=51, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
bench = {"MIN_N_RAM": MIN_N_RAM,
        "MAX_ANNUAL_DAILY_AVERAGE": MAX_ANNUAL_DAILY_AVERAGE,
        "MAX_DAYS_WITH_MAX_OVER97": MAX_DAYS_WITH_MAX_OVER97}

## Test
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>Test</p>", unsafe_allow_html=True)
with cols[1]:
    MIN_N_RAM = st.number_input("Max RAM", min_value=utils.N_RAM_MIN_VALUE, max_value=utils.N_RAM_MAX_VALUE, value=by_default_config_dict['RAM_OVERSIZED']['Test']['MIN_N_RAM'], step=None, format=None, key=52, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MAX_ANNUAL_DAILY_AVERAGE= st.number_input("Min daily average", min_value=0, max_value=100, value=by_default_config_dict['RAM_OVERSIZED']['Test']['MAX_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=53, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_DAYS_WITH_MAX_OVER97 = st.number_input("Min days over 97%", min_value=0, max_value=365, value=by_default_config_dict['RAM_OVERSIZED']['Test']['MAX_DAYS_WITH_MAX_OVER97'], step=None, format=None, key=54, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
test = {"MIN_N_RAM": MIN_N_RAM,
        "MAX_ANNUAL_DAILY_AVERAGE": MAX_ANNUAL_DAILY_AVERAGE,
        "MAX_DAYS_WITH_MAX_OVER97": MAX_DAYS_WITH_MAX_OVER97}

## Test
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>Dev</p>", unsafe_allow_html=True)
with cols[1]:
    MIN_N_RAM = st.number_input("Max RAM", min_value=utils.N_RAM_MIN_VALUE, max_value=utils.N_RAM_MAX_VALUE, value=by_default_config_dict['RAM_OVERSIZED']['Test']['MIN_N_RAM'], step=None, format=None, key=55, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MAX_ANNUAL_DAILY_AVERAGE= st.number_input("Min daily average", min_value=0, max_value=100, value=by_default_config_dict['RAM_OVERSIZED']['Test']['MAX_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=56, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_DAYS_WITH_MAX_OVER97 = st.number_input("Min days over 97%", min_value=0, max_value=365, value=by_default_config_dict['RAM_OVERSIZED']['Test']['MAX_DAYS_WITH_MAX_OVER97'], step=None, format=None, key=57, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
dev = {"MIN_N_RAM": MIN_N_RAM,
        "MAX_ANNUAL_DAILY_AVERAGE": MAX_ANNUAL_DAILY_AVERAGE,
        "MAX_DAYS_WITH_MAX_OVER97": MAX_DAYS_WITH_MAX_OVER97}

## UAT
cols = st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center; color:#333333'>UAT</p>", unsafe_allow_html=True)
with cols[1]:
    MIN_N_RAM = st.number_input("Max RAM", min_value=utils.N_RAM_MIN_VALUE, max_value=utils.N_RAM_MAX_VALUE, value=by_default_config_dict['RAM_OVERSIZED']['UAT']['MIN_N_RAM'], step=None, format=None, key=58, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MAX_ANNUAL_DAILY_AVERAGE= st.number_input("Min daily average", min_value=0, max_value=100, value=by_default_config_dict['RAM_OVERSIZED']['UAT']['MAX_ANNUAL_DAILY_AVERAGE'], step=None, format=None, key=59, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_DAYS_WITH_MAX_OVER97 = st.number_input("Min days over 97%", min_value=0, max_value=365, value=by_default_config_dict['RAM_OVERSIZED']['UAT']['MAX_DAYS_WITH_MAX_OVER97'], step=None, format=None, key=60, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
uat = {"MIN_N_RAM": MIN_N_RAM,
        "MAX_ANNUAL_DAILY_AVERAGE": MAX_ANNUAL_DAILY_AVERAGE,
        "MAX_DAYS_WITH_MAX_OVER97": MAX_DAYS_WITH_MAX_OVER97}

ram_oversized = {"Prod": prod,
                  "Bench": bench,
                  "Test": test,
                  "Dev": dev,
                  "UAT": uat}

config_dict = {"CPU_UNDERSIZED": cpu_undersized,
               "CPU_OVERSIZED": cpu_oversized,
               "RAM_UNDERSIZED": ram_undersized,
               "RAM_OVERSIZED": ram_oversized}

# Config file uploader
st.markdown(f"<h4 style='text-align: left;'>Or manually upload a config file</h4>", unsafe_allow_html=True)
config_file = st.file_uploader('Upload the config_file.json', accept_multiple_files=False,
                                   type=["json"], label_visibility="collapsed")

# Run the steps from servers_list.py without exporting the CSV
st.text('')
cols = st.columns(3)
run = cols[1].button('Optimize the servers configuration!', key=None, help=None, on_click=None, args=None, kwargs=None, disabled=False)

if run:
    if config_file is not None:
        try: 
            config_dict = json.load(config_file) # overright config_dict if a file is uploaded
        except:
            st.markdown(f"<p style='text-align: left;'>The file is not a valid json file. The model used the manually added values.</p>", unsafe_allow_html=True)   
    
    if data is None:
        data = pd.read_csv('default_input_files/server_wise_dataset.csv')

    else:
        data = pd.read_csv(data)
    
    # Run the steps from servers_list.py without exporting the CSV
    # Filtering dataset to get CPU, RAM oversized & undersized
    # CPU undersized
    cpu_undersized, cpu_oversized, ram_undersized, ram_oversized = utils.create_servers_list(data, config_dict)

    data_mycloud = pd.read_csv('default_input_files/mycloud_20221221.csv')

    cpu_undersized, ram_undersized = utils.add_column_CPU_RAM(cpu_undersized, ram_undersized)
    cpu_undersized = utils.add_columns_config_changes(cpu_undersized, undersized=True, cpu_bool=True, config_dict=config_dict)
    ram_undersized = utils.add_columns_config_changes(ram_undersized, undersized=True, cpu_bool=False, config_dict=config_dict)
    cpu_oversized, ram_oversized = utils.add_column_CPU_RAM(cpu_oversized, ram_oversized)
    cpu_oversized = utils.add_columns_config_changes(cpu_oversized, undersized=False, cpu_bool=True, config_dict=config_dict)
    ram_oversized = utils.add_columns_config_changes(ram_oversized, undersized=False, cpu_bool=False, config_dict=config_dict)

    both_oversized = pd.concat([cpu_oversized, ram_oversized]).drop_duplicates(subset='name_server')
    len_both_oversized = both_oversized[both_oversized.both == True].shape[0]
    both_undersized = pd.concat([cpu_undersized, ram_undersized]).drop_duplicates(subset='name_server')
    len_both_undersized = both_undersized[both_undersized.both == True].shape[0]

    # Create dataframe with all server and prices evolution
    cpu_u_for_join = cpu_undersized[['name_server', 'key', 'Price', 'value_avg_mean_cpu', 'value_avg_mean_mem', 'new_config', 'new_avg_mean_CPU', 'new_avg_mean_RAM']]
    cpu_o_for_join = cpu_oversized[['name_server', 'key', 'Price', 'value_avg_mean_cpu', 'value_avg_mean_mem','new_config', 'new_avg_mean_CPU', 'new_avg_mean_RAM']]
    ram_u_for_join = ram_undersized[['name_server', 'key', 'Price', 'value_avg_mean_cpu', 'value_avg_mean_mem','new_config', 'new_avg_mean_CPU', 'new_avg_mean_RAM']]
    ram_o_for_join = ram_oversized[['name_server', 'key', 'Price', 'value_avg_mean_cpu', 'value_avg_mean_mem', 'new_config', 'new_avg_mean_CPU', 'new_avg_mean_RAM']]

    all_changes = pd.concat([cpu_u_for_join, cpu_o_for_join, ram_u_for_join, ram_o_for_join], axis=0).drop_duplicates(subset='name_server')
    all_changes = all_changes.merge(data_mycloud[['key', 'Price']], left_on='new_config', right_on='key', how='left', suffixes=['_old', '_new'])
    all_changes['price_delta'] =  all_changes['Price_new'] - all_changes['Price_old']

    st.header("Results")

    # create three columns
    kpi11, kpi12, kpi13 = st.columns(3)

    # fill in those three columns with respective metrics or KPIs
    with open ('.streamlit/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    kpi11.metric(
        label="Number of CPU oversized",
        value=cpu_oversized.shape[0]
    )
    kpi12.metric(
        label="Number of RAM oversized",
        value=ram_oversized.shape[0],
    )
    kpi13.metric(
        label="Both oversized",
        value=len_both_oversized,
    )
    st.text('')
    # create three columns
    kpi21, kpi22, kpi23 = st.columns(3)

    # fill in those three columns with respective metrics or KPIs
    kpi21.metric(
        label="Number of CPU undersized",
        value=cpu_undersized.shape[0]
    )

    kpi22.metric(
        label="Number of RAM undersized",
        value=ram_undersized.shape[0]
    )

    kpi23.metric(
        label="Both undersized",
        value=len_both_undersized,
    )
    st.text('')
    # create three columns
    kpi31, kpi32, kpi33 = st.columns(3)

    # fill in those three columns with respective metrics or KPIs
    kpi31.metric(
        label="Average of formerly oversized (CPU)",
        value=f"{cpu_oversized.new_avg_mean_CPU.mean():.2f} %",
        delta=f"{cpu_oversized.new_avg_mean_CPU.mean() - cpu_oversized.value_avg_mean_cpu.mean():.2f} pts",
    )

    kpi32.metric(
        label="Average of formerly undersized (CPU)",
        value=f"{cpu_undersized.new_avg_mean_CPU.mean():.2f} %",
        delta=f"{cpu_undersized.new_avg_mean_CPU.mean() - cpu_undersized.value_avg_mean_cpu.mean():.2f} pts",
    )

    kpi33.metric(
        label="Most used configuration",
        value=f"{all_changes.new_config.mode()[0]}",
        delta=f"Previous: {all_changes.key_old.mode()[0]}",
    )

    st.text('')
    # create three columns
    kpi41, kpi42, kpi43 = st.columns(3)

    # fill in those three columns with respective metrics or KPIs
    kpi41.metric(
        label="Average of formerly oversized (RAM)",
        value=f"{ram_oversized.new_avg_mean_RAM.mean():.2f} %",
        delta=f"{ram_oversized.new_avg_mean_RAM.mean() - ram_oversized.value_avg_mean_mem.mean():.2f} pts",
    )

    kpi42.metric(
        label="Average of formerly undersized (RAM)",
        value=f"{ram_undersized.new_avg_mean_RAM.mean():.2f} %",
        delta=f"{ram_undersized.new_avg_mean_RAM.mean() - ram_undersized.value_avg_mean_mem.mean():.2f} pts",
    )

    kpi43.metric(
        label="Total Price",
        value="{:,.2f} €".format(all_changes.Price_new.sum()),
        delta="{:,.2f} €".format(all_changes.price_delta.sum()),
    )

    st.text("")
    st.text("")

    st.dataframe(data=all_changes, width=None, height=None, use_container_width=True)

    csv = all_changes.to_csv(index=False).encode('utf-8')
    cols = st.columns(3)
    cols[1].download_button(
        "Download the csv file here 📂",
        csv,
        "optimized_config.csv",
        "text/csv",
        key='download-csv',
    )