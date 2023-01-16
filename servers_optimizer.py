import streamlit as st
import pandas as pd
import json

#st.markdown(f"<h1 style='text-align: center;'>Natixis</hc1>", unsafe_allow_html=True)
st.title('Servers Optimizer')

# Upload server wise CSV file
st.header("Upload the Servers file")
data = st.file_uploader('Upload the "server wise" CSV', accept_multiple_files=False,
                                   type=["csv"], label_visibility="collapsed")

# Set up the parameters to replace config_file.json
st.header("Set up the parameters")
st.markdown(f"<p>You have the choice here: manually set up the parameters or upload a config file at the bottom.</p>", unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align: left;'>CPU Undersized</h4>", unsafe_allow_html=True)

# CP Udersized config

## Head of the columns
cols=st.columns(4)
with cols[1]:
    st.markdown(f"<p>Max number of CPU</p>", unsafe_allow_html=True)
with cols[2]:
    st.markdown(f"<p>Min days with saturation</p>", unsafe_allow_html=True)
with cols[3]:
    st.markdown(f"<p>Min annual daily avg</p>", unsafe_allow_html=True)

## Production
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>Production</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_N_CPU = st.number_input("Max number of CPU", min_value=1, max_value=16, value=16, step=None, format=None, key=1, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAYS_WITH_SATURATION = st.number_input("Min days with saturation", min_value=1, max_value=16, value=16, step=None, format=None, key=2, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MIN_ANNUAL_DAILY_AVERAGE = st.number_input("Min annual daily average", min_value=1, max_value=16, value=16, step=None, format=None, key=3, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
prod = {"MAX_N_CPU": MAX_N_CPU,
        "MIN_DAYS_WITH_SATURATION": MIN_DAYS_WITH_SATURATION,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE}

## Bench
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>Bench</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_N_CPU = st.number_input("Max number of CPU", min_value=1, max_value=16, value=16, step=None, format=None, key=4, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAYS_WITH_SATURATION = st.number_input("Min days with saturation", min_value=1, max_value=16, value=16, step=None, format=None, key=5, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MIN_ANNUAL_DAILY_AVERAGE = st.number_input("Min annual daily average", min_value=1, max_value=16, value=16, step=None, format=None, key=6, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
bench = {"MAX_N_CPU": MAX_N_CPU,
        "MIN_DAYS_WITH_SATURATION": MIN_DAYS_WITH_SATURATION,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE}

## Test
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>Test</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_N_CPU = st.number_input("Max number of CPU", min_value=1, max_value=16, value=16, step=None, format=None, key=7, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAYS_WITH_SATURATION = st.number_input("Min days with saturation", min_value=1, max_value=16, value=16, step=None, format=None, key=8, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MIN_ANNUAL_DAILY_AVERAGE = st.number_input("Min annual daily average", min_value=1, max_value=16, value=16, step=None, format=None, key=9, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
test = {"MAX_N_CPU": MAX_N_CPU,
        "MIN_DAYS_WITH_SATURATION": MIN_DAYS_WITH_SATURATION,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE}

## Dev
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>Dev</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_N_CPU = st.number_input("Max number of CPU", min_value=1, max_value=16, value=16, step=None, format=None, key=10, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAYS_WITH_SATURATION = st.number_input("Min days with saturation", min_value=1, max_value=16, value=16, step=None, format=None, key=11, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MIN_ANNUAL_DAILY_AVERAGE = st.number_input("Min annual daily average", min_value=1, max_value=16, value=16, step=None, format=None, key=12, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
dev = {"MAX_N_CPU": MAX_N_CPU,
        "MIN_DAYS_WITH_SATURATION": MIN_DAYS_WITH_SATURATION,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE}

## UAT
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>UAT</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_N_CPU = st.number_input("Max number of CPU", min_value=1, max_value=16, value=16, step=None, format=None, key=13, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAYS_WITH_SATURATION = st.number_input("Min days with saturation", min_value=1, max_value=16, value=16, step=None, format=None, key=14, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MIN_ANNUAL_DAILY_AVERAGE = st.number_input("Min annual daily average", min_value=1, max_value=16, value=16, step=None, format=None, key=15, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
uat = {"MAX_N_CPU": MAX_N_CPU,
        "MIN_DAYS_WITH_SATURATION": MIN_DAYS_WITH_SATURATION,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE}

cpu_undersized = {"Prod": prod,
                  "Bench": bench,
                  "Test": test,
                  "Dev": dev,
                  "UAT": uat}

# CPU Oversized config
st.markdown(f"<h4 style='text-align: left;'>CPU Overrsized</h4>", unsafe_allow_html=True)

cols=st.columns(4)
with cols[1]:
    st.markdown(f"<p>Min number of CPU</p>", unsafe_allow_html=True)
with cols[2]:
    st.markdown(f"<p>Max days with saturation</p>", unsafe_allow_html=True)
with cols[3]:
    st.markdown(f"<p>Max annual daily avg</p>", unsafe_allow_html=True)

## Production
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>Production</p>", unsafe_allow_html=True)
with cols[1]:
    MIN_N_CPU = st.number_input("Max number of CPU", min_value=0, max_value=16, value=16, step=None, format=None, key=16, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MAX_DAYS_WITH_SATURATION = st.number_input("Max days with saturation", min_value=0, max_value=16, value=16, step=None, format=None, key=17, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_ANNUAL_DAILY_AVERAGE = st.number_input("Max annual daily average", min_value=0, max_value=16, value=16, step=None, format=None, key=18, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
prod = {"MIN_N_CPU": MIN_N_CPU,
        "MAX_DAYS_WITH_SATURATION": MAX_DAYS_WITH_SATURATION,
        "MAX_ANNUAL_DAILY_AVERAGE": MAX_ANNUAL_DAILY_AVERAGE}

## Bench
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>Bench</p>", unsafe_allow_html=True)
with cols[1]:
    MIN_N_CPU = st.number_input("Max number of CPU", min_value=0, max_value=16, value=16, step=None, format=None, key=19, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MAX_DAYS_WITH_SATURATION = st.number_input("Max days with saturation", min_value=0, max_value=16, value=16, step=None, format=None, key=20, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_ANNUAL_DAILY_AVERAGE = st.number_input("Max annual daily average", min_value=0, max_value=16, value=16, step=None, format=None, key=21, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
bench = {"MIN_N_CPU": MIN_N_CPU,
        "MAX_DAYS_WITH_SATURATION": MAX_DAYS_WITH_SATURATION,
        "MAX_ANNUAL_DAILY_AVERAGE": MAX_ANNUAL_DAILY_AVERAGE}

## Test
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>Test</p>", unsafe_allow_html=True)
with cols[1]:
    MIN_N_CPU = st.number_input("Max number of CPU", min_value=0, max_value=16, value=16, step=None, format=None, key=22, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MAX_DAYS_WITH_SATURATION = st.number_input("Max days with saturation", min_value=0, max_value=16, value=16, step=None, format=None, key=23, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_ANNUAL_DAILY_AVERAGE = st.number_input("Max annual daily average", min_value=0, max_value=16, value=16, step=None, format=None, key=24, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
test = {"MIN_N_CPU": MIN_N_CPU,
        "MAX_DAYS_WITH_SATURATION": MAX_DAYS_WITH_SATURATION,
        "MAX_ANNUAL_DAILY_AVERAGE": MAX_ANNUAL_DAILY_AVERAGE}

## Dev
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>Dev</p>", unsafe_allow_html=True)
with cols[1]:
    MIN_N_CPU = st.number_input("Max number of CPU", min_value=0, max_value=16, value=16, step=None, format=None, key=25, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MAX_DAYS_WITH_SATURATION = st.number_input("Max days with saturation", min_value=0, max_value=16, value=16, step=None, format=None, key=26, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_ANNUAL_DAILY_AVERAGE = st.number_input("Max annual daily average", min_value=0, max_value=16, value=16, step=None, format=None, key=27, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
dev = {"MIN_N_CPU": MIN_N_CPU,
        "MAX_DAYS_WITH_SATURATION": MAX_DAYS_WITH_SATURATION,
        "MAX_ANNUAL_DAILY_AVERAGE": MAX_ANNUAL_DAILY_AVERAGE}

## UAT
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>UAT</p>", unsafe_allow_html=True)
with cols[1]:
    MIN_N_CPU = st.number_input("Max number of CPU", min_value=0, max_value=16, value=16, step=None, format=None, key=28, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MAX_DAYS_WITH_SATURATION = st.number_input("Max days with saturation", min_value=0, max_value=16, value=16, step=None, format=None, key=29, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_ANNUAL_DAILY_AVERAGE = st.number_input("Max annual daily average", min_value=0, max_value=16, value=16, step=None, format=None, key=30, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
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
cols=st.columns(4)
with cols[1]:
    st.markdown(f"<p>Max RAM</p>", unsafe_allow_html=True)
with cols[2]:
    st.markdown(f"<p>Min daily average</p>", unsafe_allow_html=True)
with cols[3]:
    st.markdown(f"<p>Min days over 97%</p>", unsafe_allow_html=True)


## Production
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>Production</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_RAM = st.number_input("Max RAM", min_value=0, max_value=16, value=16, step=None, format=None, key=31, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAILY_AVERAGE= st.number_input("Min daily average", min_value=0, max_value=16, value=16, step=None, format=None, key=32, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_DAYS_WITH_MAX_OVER_97 = st.number_input("Min days over 97%", min_value=0, max_value=16, value=16, step=None, format=None, key=33, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
prod = {"MAX_RAM": MAX_RAM,
        "MIN_DAILY_AVERAGE": MIN_DAILY_AVERAGE,
        "MAX_DAYS_WITH_MAX_OVER_97": MAX_DAYS_WITH_MAX_OVER_97}

## Bench
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>Bench</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_RAM = st.number_input("Max RAM", min_value=0, max_value=16, value=16, step=None, format=None, key=34, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAILY_AVERAGE= st.number_input("Min daily average", min_value=0, max_value=16, value=16, step=None, format=None, key=35, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_DAYS_WITH_MAX_OVER_97 = st.number_input("Min days over 97%", min_value=0, max_value=16, value=16, step=None, format=None, key=36, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
bench = {"MAX_RAM": MAX_RAM,
        "MIN_DAILY_AVERAGE": MIN_DAILY_AVERAGE,
        "MAX_DAYS_WITH_MAX_OVER_97": MAX_DAYS_WITH_MAX_OVER_97}

## Test
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>Test</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_RAM = st.number_input("Max RAM", min_value=0, max_value=16, value=16, step=None, format=None, key=37, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAILY_AVERAGE= st.number_input("Min daily average", min_value=0, max_value=16, value=16, step=None, format=None, key=38, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_DAYS_WITH_MAX_OVER_97 = st.number_input("Min days over 97%", min_value=0, max_value=16, value=16, step=None, format=None, key=39, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
test = {"MAX_RAM": MAX_RAM,
        "MIN_DAILY_AVERAGE": MIN_DAILY_AVERAGE,
        "MAX_DAYS_WITH_MAX_OVER_97": MAX_DAYS_WITH_MAX_OVER_97}

## Dev
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>Dev</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_RAM = st.number_input("Max RAM", min_value=0, max_value=16, value=16, step=None, format=None, key=40, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAILY_AVERAGE= st.number_input("Min daily average", min_value=0, max_value=16, value=16, step=None, format=None, key=41, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_DAYS_WITH_MAX_OVER_97 = st.number_input("Min days over 97%", min_value=0, max_value=16, value=16, step=None, format=None, key=42, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
dev = {"MAX_RAM": MAX_RAM,
        "MIN_DAILY_AVERAGE": MIN_DAILY_AVERAGE,
        "MAX_DAYS_WITH_MAX_OVER_97": MAX_DAYS_WITH_MAX_OVER_97}

## UAT
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>UAT</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_RAM = st.number_input("Max RAM", min_value=0, max_value=16, value=16, step=None, format=None, key=43, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAILY_AVERAGE= st.number_input("Min daily average", min_value=0, max_value=16, value=16, step=None, format=None, key=44, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_DAYS_WITH_MAX_OVER_97 = st.number_input("Min days over 97%", min_value=0, max_value=16, value=16, step=None, format=None, key=45, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
uat = {"MAX_RAM": MAX_RAM,
        "MIN_DAILY_AVERAGE": MIN_DAILY_AVERAGE,
        "MAX_DAYS_WITH_MAX_OVER_97": MAX_DAYS_WITH_MAX_OVER_97}
ram_undersized = {"Prod": prod,
                  "Bench": bench,
                  "Test": test,
                  "Dev": dev,
                  "UAT": uat}

# RAM Oversized config
st.markdown(f"<h4 style='text-align: left;'>RAM Oversized</h4>", unsafe_allow_html=True)

cols=st.columns(4)
with cols[1]:
    st.markdown(f"<p>Max RAM</p>", unsafe_allow_html=True)
with cols[2]:
    st.markdown(f"<p>Min daily average</p>", unsafe_allow_html=True)
with cols[3]:
    st.markdown(f"<p>Min days over 97%</p>", unsafe_allow_html=True)

## Production
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>Production</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_RAM = st.number_input("Max RAM", min_value=0, max_value=16, value=16, step=None, format=None, key=46, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAILY_AVERAGE= st.number_input("Min daily average", min_value=0, max_value=16, value=16, step=None, format=None, key=47, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_DAYS_WITH_MAX_OVER_97 = st.number_input("Min days over 97%", min_value=0, max_value=16, value=16, step=None, format=None, key=48, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
prod = {"MAX_RAM": MAX_RAM,
        "MIN_DAILY_AVERAGE": MIN_DAILY_AVERAGE,
        "MAX_DAYS_WITH_MAX_OVER_97": MAX_DAYS_WITH_MAX_OVER_97}

## Bench
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>Bench</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_RAM = st.number_input("Max RAM", min_value=0, max_value=16, value=16, step=None, format=None, key=49, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAILY_AVERAGE= st.number_input("Min daily average", min_value=0, max_value=16, value=16, step=None, format=None, key=50, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_DAYS_WITH_MAX_OVER_97 = st.number_input("Min days over 97%", min_value=0, max_value=16, value=16, step=None, format=None, key=51, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
bench = {"MAX_RAM": MAX_RAM,
        "MIN_DAILY_AVERAGE": MIN_DAILY_AVERAGE,
        "MAX_DAYS_WITH_MAX_OVER_97": MAX_DAYS_WITH_MAX_OVER_97}

## Test
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>Test</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_RAM = st.number_input("Max RAM", min_value=0, max_value=16, value=16, step=None, format=None, key=52, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAILY_AVERAGE= st.number_input("Min daily average", min_value=0, max_value=16, value=16, step=None, format=None, key=53, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_DAYS_WITH_MAX_OVER_97 = st.number_input("Min days over 97%", min_value=0, max_value=16, value=16, step=None, format=None, key=54, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
test = {"MAX_RAM": MAX_RAM,
        "MIN_DAILY_AVERAGE": MIN_DAILY_AVERAGE,
        "MAX_DAYS_WITH_MAX_OVER_97": MAX_DAYS_WITH_MAX_OVER_97}

## Dev
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>Dev</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_RAM = st.number_input("Max RAM", min_value=0, max_value=16, value=16, step=None, format=None, key=55, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAILY_AVERAGE= st.number_input("Min daily average", min_value=0, max_value=16, value=16, step=None, format=None, key=56, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_DAYS_WITH_MAX_OVER_97 = st.number_input("Min days over 97%", min_value=0, max_value=16, value=16, step=None, format=None, key=57, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
dev = {"MAX_RAM": MAX_RAM,
        "MIN_DAILY_AVERAGE": MIN_DAILY_AVERAGE,
        "MAX_DAYS_WITH_MAX_OVER_97": MAX_DAYS_WITH_MAX_OVER_97}

## UAT
cols=st.columns(4)
with cols[0]:
    st.markdown(f"<p style='text-align: center;'>UAT</p>", unsafe_allow_html=True)
with cols[1]:
    MAX_RAM = st.number_input("Max RAM", min_value=0, max_value=16, value=16, step=None, format=None, key=58, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[2]:
    MIN_DAILY_AVERAGE= st.number_input("Min daily average", min_value=0, max_value=16, value=16, step=None, format=None, key=59, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
with cols[3]:
    MAX_DAYS_WITH_MAX_OVER_97 = st.number_input("Min days over 97%", min_value=0, max_value=16, value=16, step=None, format=None, key=60, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="collapsed")
uat = {"MAX_RAM": MAX_RAM,
        "MIN_DAILY_AVERAGE": MIN_DAILY_AVERAGE,
        "MAX_DAYS_WITH_MAX_OVER_97": MAX_DAYS_WITH_MAX_OVER_97}

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
run = st.button('Run', key=None, help=None, on_click=None, args=None, kwargs=None, disabled=False)

if run:
    if config_file is not None:
        try: 
            config_dict = json.load(config_file)
        except:
            st.markdown(f"<p style='text-align: left;'>The file is not a valid json file. The model used the manually added values.</p>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: left;'>Results</h4>", unsafe_allow_html=True)
    
    # Run the steps from servers_list.py without exporting the CSV
    # Filtering dataset to get CPU, RAM oversized & undersized
    # CPU undersized
    cpu_undersized_mask = ((data.name_environment == list(config_dict['CPU_UNDERSIZED'].keys())[0]) & (data.CPU <  config_dict['CPU_UNDERSIZED']['Prod']['MAX_N_CPU']) & (data.value_avg_mean_cpu > config_dict['CPU_UNDERSIZED']['Prod']['MIN_ANNUAL_DAILY_AVERAGE']) &(data.days_max100 > config_dict['CPU_UNDERSIZED']['Prod']['MIN_DAYS_WITH_SATURATION'])) | (
        (data.name_environment == list(config_dict['CPU_UNDERSIZED'].keys())[1]) & (data.CPU <  config_dict['CPU_UNDERSIZED']['Bench']['MAX_N_CPU']) &  (data.value_avg_mean_cpu > config_dict['CPU_UNDERSIZED']['Bench']['MIN_ANNUAL_DAILY_AVERAGE']) &  (data.days_max100 > config_dict['CPU_UNDERSIZED']['Prod']['MIN_DAYS_WITH_SATURATION'])) | (
        (data.name_environment == list(config_dict['CPU_UNDERSIZED'].keys())[2]) & (data.CPU <  config_dict['CPU_UNDERSIZED']['Test']['MAX_N_CPU']) & (data.value_avg_mean_cpu > config_dict['CPU_UNDERSIZED']['Test']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 > config_dict['CPU_UNDERSIZED']['Prod']['MIN_DAYS_WITH_SATURATION'])) |(
        (data.name_environment == list(config_dict['CPU_UNDERSIZED'].keys())[3]) & (data.CPU <  config_dict['CPU_UNDERSIZED']['Dev']['MAX_N_CPU']) & (data.value_avg_mean_cpu > config_dict['CPU_UNDERSIZED']['Dev']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 > config_dict['CPU_UNDERSIZED']['Prod']['MIN_DAYS_WITH_SATURATION'])) | (
        (data.name_environment == list(config_dict['CPU_UNDERSIZED'].keys())[4]) & (data.CPU <  config_dict['CPU_UNDERSIZED']['UAT']['MAX_N_CPU']) & (data.value_avg_mean_cpu > config_dict['CPU_UNDERSIZED']['UAT']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 > config_dict['CPU_UNDERSIZED']['Prod']['MIN_DAYS_WITH_SATURATION']))
                        
    data_cpu_undersized = data[cpu_undersized_mask].drop(columns=['Unnamed: 0'])

    # CPU oversized
    cpu_oversized_mask = ((data.name_environment == list(config_dict['CPU_OVERSIZED'].keys())[0]) & (data.CPU >  config_dict['CPU_OVERSIZED']['Prod']['MIN_N_CPU']) & (data.value_avg_mean_cpu < config_dict['CPU_OVERSIZED']['Prod']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 > config_dict['CPU_OVERSIZED']['Prod']['MAX_DAYS_WITH_SATURATION'])) |(
        (data.name_environment == list(config_dict['CPU_OVERSIZED'].keys())[1]) & (data.CPU >  config_dict['CPU_OVERSIZED']['Bench']['MIN_N_CPU']) & (data.value_avg_mean_cpu < config_dict['CPU_OVERSIZED']['Bench']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 < config_dict['CPU_OVERSIZED']['Prod']['MAX_DAYS_WITH_SATURATION'])) |(
        (data.name_environment == list(config_dict['CPU_OVERSIZED'].keys())[2]) & (data.CPU >  config_dict['CPU_OVERSIZED']['Test']['MIN_N_CPU']) & (data.value_avg_mean_cpu < config_dict['CPU_OVERSIZED']['Test']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 < config_dict['CPU_OVERSIZED']['Prod']['MAX_DAYS_WITH_SATURATION'])) |(
        (data.name_environment == list(config_dict['CPU_OVERSIZED'].keys())[3]) & (data.CPU >  config_dict['CPU_OVERSIZED']['Dev']['MIN_N_CPU']) & (data.value_avg_mean_cpu < config_dict['CPU_OVERSIZED']['Dev']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 < config_dict['CPU_OVERSIZED']['Prod']['MAX_DAYS_WITH_SATURATION'])) |(
        (data.name_environment == list(config_dict['CPU_OVERSIZED'].keys())[4]) & (data.CPU >  config_dict['CPU_OVERSIZED']['UAT']['MIN_N_CPU']) & (data.value_avg_mean_cpu < config_dict['CPU_OVERSIZED']['UAT']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max100 < config_dict['CPU_OVERSIZED']['Prod']['MAX_DAYS_WITH_SATURATION']))
    data_cpu_oversized = data[cpu_oversized_mask].drop(columns=['Unnamed: 0'])

    # MEM undersized
    mem_undersized_mask = ((data.name_environment == list(config_dict['RAM_UNDERSIZED'].keys())[0]) & (data.RAM <  config_dict['RAM_UNDERSIZED']['Prod']['MAX_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_UNDERSIZED']['Prod']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max97> config_dict['RAM_UNDERSIZED']['Prod']['MIN_DAYS_WITH_MAX_OVER97'])) |(
        (data.name_environment == list(config_dict['RAM_UNDERSIZED'].keys())[1]) & (data.RAM <  config_dict['RAM_UNDERSIZED']['Bench']['MAX_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_UNDERSIZED']['Bench']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 > config_dict['RAM_UNDERSIZED']['Prod']['MIN_DAYS_WITH_MAX_OVER97'])) |(
        (data.name_environment == list(config_dict['RAM_UNDERSIZED'].keys())[2]) & (data.RAM <  config_dict['RAM_UNDERSIZED']['Test']['MAX_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_UNDERSIZED']['Test']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 > config_dict['RAM_UNDERSIZED']['Prod']['MIN_DAYS_WITH_MAX_OVER97'])) |(
        (data.name_environment == list(config_dict['RAM_UNDERSIZED'].keys())[3]) & (data.RAM <  config_dict['RAM_UNDERSIZED']['Dev']['MAX_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_UNDERSIZED']['Dev']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 > config_dict['RAM_UNDERSIZED']['Prod']['MIN_DAYS_WITH_MAX_OVER97'])) |(
        (data.name_environment == list(config_dict['RAM_UNDERSIZED'].keys())[4]) & (data.RAM <  config_dict['RAM_UNDERSIZED']['UAT']['MAX_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_UNDERSIZED']['UAT']['MIN_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 > config_dict['RAM_UNDERSIZED']['Prod']['MIN_DAYS_WITH_MAX_OVER97']))
    data_mem_undersized = data[mem_undersized_mask].drop(columns=['Unnamed: 0'])

    # MEM oversized
    mem_oversized_mask = ((data.name_environment == list(config_dict['RAM_OVERSIZED'].keys())[0]) & (data.RAM <  config_dict['RAM_OVERSIZED']['Prod']['MIN_N_RAM']) & (data.value_avg_mean_mem > config_dict['RAM_OVERSIZED']['Prod']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max97> config_dict['RAM_OVERSIZED']['Prod']['MAX_DAYS_WITH_MAX_OVER97'])) |(
        (data.name_environment == list(config_dict['RAM_OVERSIZED'].keys())[1]) & (data.RAM >  config_dict['RAM_OVERSIZED']['Bench']['MIN_N_RAM']) & (data.value_avg_mean_mem < config_dict['RAM_OVERSIZED']['Bench']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 < config_dict['RAM_OVERSIZED']['Prod']['MAX_DAYS_WITH_MAX_OVER97'])) |(
        (data.name_environment == list(config_dict['RAM_OVERSIZED'].keys())[2]) & (data.RAM >  config_dict['RAM_OVERSIZED']['Test']['MIN_N_RAM']) & (data.value_avg_mean_mem < config_dict['RAM_OVERSIZED']['Test']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 < config_dict['RAM_OVERSIZED']['Prod']['MAX_DAYS_WITH_MAX_OVER97'])) |(
        (data.name_environment == list(config_dict['RAM_OVERSIZED'].keys())[3]) & (data.RAM >  config_dict['RAM_OVERSIZED']['Dev']['MIN_N_RAM']) & (data.value_avg_mean_mem < config_dict['RAM_OVERSIZED']['Dev']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 < config_dict['RAM_OVERSIZED']['Prod']['MAX_DAYS_WITH_MAX_OVER97'])) |(
        (data.name_environment == list(config_dict['RAM_OVERSIZED'].keys())[4]) & (data.RAM >  config_dict['RAM_OVERSIZED']['UAT']['MIN_N_RAM']) & (data.value_avg_mean_mem < config_dict['RAM_OVERSIZED']['UAT']['MAX_ANNUAL_DAILY_AVERAGE']) & (data.days_max97 < config_dict['RAM_OVERSIZED']['Prod']['MAX_DAYS_WITH_MAX_OVER97']))
    data_mem_oversized = data[mem_oversized_mask].drop(columns=['Unnamed: 0'])

    # Run the steps from mycloud_config_optimizer.py
    cpu_undersized = cpu_undersized[['name_server', 'key', 'Price', 'CPU', 'RAM', 'name_environment', 'value_avg_mean_cpu', 'value_avg_mean_mem']]
    ram_undersized = ram_undersized[['name_server', 'key', 'Price', 'CPU', 'RAM', 'name_environment', 'value_avg_mean_mem', 'value_avg_mean_cpu']]
    cpu_oversized = cpu_oversized[['name_server', 'key', 'Price', 'CPU', 'RAM', 'name_environment', 'value_avg_mean_cpu', 'value_avg_mean_mem']]
    ram_oversized = ram_oversized[['name_server', 'key', 'Price', 'CPU', 'RAM', 'name_environment', 'value_avg_mean_mem', 'value_avg_mean_cpu']]

    undersized_bound_cpu = {'Prod': config_dict['CPU_UNDERSIZED']['Prod']["MIN_ANNUAL_DAILY_AVERAGE"], 'Bench': config_dict['CPU_UNDERSIZED']['Bench']["MIN_ANNUAL_DAILY_AVERAGE"], 'Dev': config_dict['CPU_UNDERSIZED']['Dev']["MIN_ANNUAL_DAILY_AVERAGE"], 'Test':config_dict['CPU_UNDERSIZED']['Test']["MIN_ANNUAL_DAILY_AVERAGE"], 'UAT':config_dict['CPU_UNDERSIZED']['UAT']["MIN_ANNUAL_DAILY_AVERAGE"]}
    oversized_bound_cpu = {'Prod': config_dict['CPU_OVERSIZED']['Prod']["MAX_ANNUAL_DAILY_AVERAGE"], 'Bench': config_dict['CPU_OVERSIZED']['Bench']["MAX_ANNUAL_DAILY_AVERAGE"], 'Dev': config_dict['CPU_OVERSIZED']['Dev']["MAX_ANNUAL_DAILY_AVERAGE"], 'Test':config_dict['CPU_OVERSIZED']['Test']["MAX_ANNUAL_DAILY_AVERAGE"], 'UAT':config_dict['CPU_OVERSIZED']['UAT']["MAX_ANNUAL_DAILY_AVERAGE"]}
    undersized_bound_ram = {'Prod': config_dict['RAM_UNDERSIZED']['Prod']["MIN_ANNUAL_DAILY_AVERAGE"], 'Bench': config_dict['RAM_UNDERSIZED']['Bench']["MIN_ANNUAL_DAILY_AVERAGE"], 'Dev': config_dict['RAM_UNDERSIZED']['Dev']["MIN_ANNUAL_DAILY_AVERAGE"], 'Test':config_dict['RAM_UNDERSIZED']['Test']["MIN_ANNUAL_DAILY_AVERAGE"], 'UAT':config_dict['RAM_UNDERSIZED']['UAT']["MIN_ANNUAL_DAILY_AVERAGE"]}
    oversized_bound_ram = {'Prod': config_dict['RAM_OVERSIZED']['Prod']["MAX_ANNUAL_DAILY_AVERAGE"], 'Bench': config_dict['RAM_OVERSIZED']['Bench']["MAX_ANNUAL_DAILY_AVERAGE"], 'Dev': config_dict['RAM_OVERSIZED']['Dev']["MAX_ANNUAL_DAILY_AVERAGE"], 'Test':config_dict['RAM_OVERSIZED']['Test']["MAX_ANNUAL_DAILY_AVERAGE"], 'UAT':config_dict['RAM_OVERSIZED']['UAT']["MAX_ANNUAL_DAILY_AVERAGE"]}

    data_mycloud = pd.read_csv('default_input_files/mycloud_20221221.csv')


# Display the results
