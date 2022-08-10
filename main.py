import streamlit as st
import numpy as np
import pandas as pd

st.checkbox("Show stuff", key='check')
if st.session_state.check:
    st.write("Box ticked")

picker = st.selectbox("Who's better", ["Trent", "Jake"])

st.write("You picked", picker)

st.sidebar.write("JAKES APP")

import time

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)


def progress_bar():
    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i + 1}')
        bar.progress(i + 1)
        time.sleep(0.1)


if st.session_state.check:
    progress_bar()

st.markdown("# Main page 🎈")
