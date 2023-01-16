import streamlit as st

#st.markdown(f"<h1 style='text-align: center;'>Natixis</h1>", unsafe_allow_html=True)
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
# ...
test = {"MAX_N_CPU": MAX_N_CPU,
        "MIN_DAYS_WITH_SATURATION": MIN_DAYS_WITH_SATURATION,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE}

## Dev
# ...
dev = {"MAX_N_CPU": MAX_N_CPU,
        "MIN_DAYS_WITH_SATURATION": MIN_DAYS_WITH_SATURATION,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE}

## UAT
# ...
uat = {"MAX_N_CPU": MAX_N_CPU,
        "MIN_DAYS_WITH_SATURATION": MIN_DAYS_WITH_SATURATION,
        "MIN_ANNUAL_DAILY_AVERAGE": MIN_ANNUAL_DAILY_AVERAGE}

cpu_undersized = {"prod": prod,
                  "bench": bench,
                  "test": test,
                  "dev": dev,
                  "uat": uat}

# CPU Oversized config

#...

cpu_oversized = {"prod": prod,
                  "bench": bench,
                  "test": test,
                  "dev": dev,
                  "uat": uat}


# RAM Undersized config

#...

ram_undersized = {"prod": prod,
                  "bench": bench,
                  "test": test,
                  "dev": dev,
                  "uat": uat}

# RAM Oversized config

#...

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