from dataclasses import dataclass
from datamuse import Datamuse
from typing import List, Callable
import pandas as pd

api = Datamuse()


    

options = dict(
    synonym = lambda worda, wordb: api.words(rel_syn=wordb, max=1),
    first_letter = lambda worda, wordb: api.words(rel_syn=wordb, sp=worda[0]+'*', max=1),
    approximate_rhyme = lambda worda, wordb: api.words(rel_syn=wordb, rel_nry=worda, max=1)
)

def test_api():
    print(api.words(rel_rhy='ninth', max=5))  # words that rhyme with "ninth"
    print(api.words(rel_rhy='orange', max=5))  # words that rhyme with "orange"
    print(api.words(rel_jja='yellow', max=5))  # things often described as "yellow"
    print(api.suggest(s='foo', max_results=10))  # completion suggestions for "foo"
    print(api.words(trg='frontier', max_results=5)) 
    api.words(rel_jjb='frontier', topics='startup', max=5)


def grab_option(worda:str, wordb:str, type:Callable) -> List[dict]:
    return type(worda, wordb)


def improve_word(composite_word: str, type:Callable) -> str:
    """
    Given a word, return a better word.
    """

    words_split = composite_word.split(" ")
    
    if len(words_split) == 2:
        worda, wordb = words_split
    else:
        print("🟡 Pattern doesn't match " + composite_word)
        return composite_word
    
    res = grab_option(worda, wordb, type)

    if len(res) > 0:
        wordb = res[0]['word'].capitalize()
        new_word = ' '.join([worda, wordb])
        print('✅ Improvement found for ' + composite_word + ' -> '  + new_word)
        return new_word
    else:
        print('❌ No improvement found for ' + composite_word)
        print('| Trying with reverse words...')
        res = grab_option(wordb, worda, type)
        if len(res) > 0:
            worda = res[0]['word'].capitalize()
            new_word = ' '.join([worda, wordb])
            print('✅ Improvement found for ' + composite_word + ' -> '  + new_word)
            return new_word
        else: 
            print('❌ No improvement found for reverse ' + composite_word)
            return composite_word


def run_pipeline():
    for key, type in options.items():
        print(f"--- type is: {key} ---")
        
        df = pd.read_csv('words.csv')[:5]
        df.apply(lambda row: improve_word(row['names'], type), axis=1)
        df.to_csv(f'words_improved_{key}.csv', index=False)

if __name__ == '__main__':
    run_pipeline()

# rel_jja	Popular nouns modified by the given adjective, per Google Books Ngrams	gradual → increase
# rel_jjb	Popular adjectives used to modify the given noun, per Google Books Ngrams	beach → sandy
# rel_syn	Synonyms (words contained within the same WordNet synset)	ocean → sea
# rel_trg	"Triggers" (words that are statistically associated with the query word in the same piece of text.)	cow → milking
# rel_ant	Antonyms (per WordNet)	late → early
# rel_spc	"Kind of" (direct hypernyms, per WordNet)	gondola → boat
# rel_gen	"More general than" (direct hyponyms, per WordNet)	boat → gondola
# rel_com	"Comprises" (direct holonyms, per WordNet)	car → accelerator
# rel_par	"Part of" (direct meronyms, per WordNet)	trunk → tree
# rel_bga	Frequent followers (w′ such that P(w′|w) ≥ 0.001, per Google Books Ngrams)	wreak → havoc
# rel_bgb	Frequent predecessors (w′ such that P(w|w′) ≥ 0.001, per Google Books Ngrams)	havoc → wreak
# rel_rhy	Rhymes ("perfect" rhymes, per RhymeZone)	spade → aid
# rel_nry	Approximate rhymes (per RhymeZone)	forest → chorus
# rel_hom	Homophones (sound-alike words)	course → coarse
# rel_cns	Consonant match	sample → simple
# sl sounds like
# ml means like
# sp spelled like