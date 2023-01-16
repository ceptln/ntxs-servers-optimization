import streamlit as st

#st.markdown(f"<h1 style='text-align: center;'>Natixis</hc1>", unsafe_allow_html=True)
st.title('Servers Optimizer')

# Upload server wise CSV file
st.header("Upload the Servers file")
data = st.file_uploader('Upload the "server wise" CSV', accept_multiple_files=False,
                                   type=["csv"], label_visibility="collapsed")

# Set up the parameters to replace config_file.json
st.header("Set up the parameters")
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

cpu_undersized = {"prod": prod,
                  "bench": bench,
                  "test": test,
                  "dev": dev,
                  "uat": uat}

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

##UAT
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

cpu_oversized = {"prod": prod,
                  "bench": bench,
                  "test": test,
                  "dev": dev,
                  "uat": uat}


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

##UAT
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
ram_undersized = {"prod": prod,
                  "bench": bench,
                  "test": test,
                  "dev": dev,
                  "uat": uat}

# RAM Oversized config
st.markdown(f"<h4 style='text-align: left;'>RAM Oversized</h4>", unsafe_allow_html=True)

ram_oversized = {"prod": prod,
                  "bench": bench,
                  "test": test,
                  "dev": dev,
                  "uat": uat}


config_dict = {"cpu_undersized": cpu_undersized,
               "cpu_oversized": cpu_oversized,
               "ram_undersized": ram_undersized,
               "ram_oversized": ram_oversized}

# Run the steps from servers_list.py without exporting the CSV

# Run the steps from mycloud_config_optimizer.py

# Display the results
