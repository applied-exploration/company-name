from find_analogy import generate_analogies
from word_pairs import word_pairs
import streamlit as st
from ga import run_ga
import pandas as pd



def setup_streamlit():
    if 'analogies' not in st.session_state:
        st.session_state['analogies'] = pd.DataFrame()
    st.title("Analogy Generator")
    
def grab_analogies(words):
    st.session_state['analogies'] = generate_analogies(words)

def create_streamlit():
    setup_streamlit()

    worda = st.text_input('Positive Word 1', 'castle')
    wordb = st.text_input('Positive Word 2', 'king')
    wordc = st.text_input('Negative Word 1', 'man')
    
    st.button('Generate Analogies', on_click=lambda:grab_analogies([{"worda":worda, "wordb":wordb, "wordc":wordc}]))
    st.button('Grab Preloaded Analogies', on_click=lambda:grab_analogies(word_pairs))
    
    analogies = st.session_state['analogies']
    if analogies.size>0:
        st.dataframe(analogies)
        first_row = analogies.iloc[0].to_numpy()
        
        for element in first_row:
            st.checkbox(element)
            
        st.button('Generate', on_click=lambda:run_ga())
        
create_streamlit()