import gensim
from gensim.models import KeyedVectors

from gensim.models import Word2Vec
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.test.utils import datapath, get_tmpfile

import gensim.downloader as api
import pandas as pd


model = api.load("glove-twitter-200")


def analogy(worda, wordc, wordb):
    top_n = 5
    results = model.most_similar(positive=[worda, wordb],negative=[wordc],  topn=top_n)
    df = pd.DataFrame([[worda,wordb, wordc] +[res[0] for res in results]], columns=['worda', 'wordb', 'wordc']+ [f'analogy_{i}' for i in range(top_n)])
    return df


words = [
    {"worda": "coal", "wordb":"dumb", "wordc":"nuclear"},
    {"worda": "programmer", "wordb":"pen", "wordc":"writer"},
    {"worda": "picasso", "wordb":"painting", "wordc":"software"}
    ]

def generate_analogies(words:list):
    df = pd.DataFrame()
    for word in words:
        df = pd.concat([df, analogy(word['worda'], word['wordb'], word['wordc'])])

    df.head()