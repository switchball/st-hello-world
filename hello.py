import streamlit as st

st.write("""
# Hello World!
This is the first app created via streamlit.
""")

# Everything is accessible via the st.secrets dict:

st.write("Day Limit:", st.secrets["DAY_LIMIT"])
st.write("My cool secrets:", st.secrets["api_key"]["secret_key"])
st.write("My cool secrets:", st.secrets["api_key"]["extra_keys"])

# And the root-level secrets are also accessible as environment variables:

import os

st.write(
    "Has environment variables been set:",
    os.environ["DAY_LIMIT"] == st.secrets["DAY_LIMIT"],
)
