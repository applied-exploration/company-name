import gensim
from gensim.models import KeyedVectors

from gensim.models import Word2Vec
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.test.utils import datapath, get_tmpfile

import gensim.downloader as api
import pandas as pd
import streamlit as st

@st.cache
def load_model():
    model = api.load("glove-twitter-200")
    return model

model = load_model()

@st.cache
def analogy(worda, wordb, wordc):
    top_n = 5
    results = model.most_similar(positive=[worda, wordb],negative=[wordc],  topn=top_n)
    df = pd.DataFrame([[worda,wordb, wordc] +[res[0] for res in results]], columns=['worda', 'wordb', 'wordc']+ [f'analogy_{i}' for i in range(top_n)])
    return df

@st.cache
def generate_analogies(words:list):
    df = pd.DataFrame()
    for word in words:
        df = pd.concat([df, analogy(word['worda'], word['wordb'], word['wordc'])])

    return df