from itertools import chain

things_human_philosophy = ["theory of", "atlas","fiction", "verve", "phenomena", "life", "spirit", "intellect", "time",  "beginning", "positivism", "empiricism", "Renaissance", "principle"]
things_human_attribute = ["ignorance", "collective", "soul", "ego",  "essence"]
things_human_relationship = ["accord", "club", "closeness", 'family', "fondness", "passion", "sentiment"]
things_human_food = ["cake", "beacon", "coffee", "beans", "pulp"]
things_human_travel = ["movement", "park", "harmony", "nature", "Ahoy"]
things_human_animal = ["creature", "monkeys"]
things_human_activities = ["darts", "canvas", "pieces"]
things_human_music = ["tempo", "tunes", "melody"]
things_human_cultural = ["modernist", "art deco", "culture", "squeeze"]
things_human_nature = ["ocean", "people", "midnight", "sunrise", "sunset", "moon"]
things_human_thinking = ["magic", "thoughts", "conception", "conjectures"]
things_human_playful = ["play", "dreams", "-semi", "-ultra", "-alpha", "-beta", "-inter"]

things_human = things_human_philosophy + things_human_attribute + things_human_relationship + things_human_food + things_human_travel + things_human_animal + things_human_activities + things_human_music + things_human_cultural + things_human_nature + things_human_thinking + things_human_playful

things_tech_experimental = ["future", "frontier", "phenomena"]
things_tech_intelligence = ["shortcuts", "complexity", "spark"]
things_tech_algorithm = ["flow", "centroids", "clusters", "algorithms", "function", "evolution","decisions", "randomness"]
things_tech_computing = ["structure", "compute", "engima", "logic", "machines", "byte", "engine"]
things_tech_scientific = ["paradigm", "Renaissance", "shift", "landscape", "volatility", "axion", "Equilibrium", "joint", "friction", "synthesis", "projection", "hypersphere", "manifold", "vectors", "zeros", "discrete", "dimensions", "sequence", "factor",  "sphere", "fraction",   "effect", "theories", "calculus", "vertices", "matrices", "isometric", "negative"]
things_tech_abstract = ["loop"]
things_tech_audacious = ["force", "world", "universe"]

things_tech = things_tech_experimental + things_tech_intelligence + things_tech_algorithm + things_tech_computing + things_tech_scientific + things_tech_abstract + things_tech_audacious

adjs_human_food = ["deep fried", "grilled"]
adjs_human_travel = ["exotic", "breathteaking", "guided"]
adjs_human_philsophy = ["hedonistic", "stoic", "empirical"]
adjs_human_relationship = ["generous", "tender", "stereotypical", "quintessential", "mutual", "friendly"]
adjs_human_antropomorphism = ["blindfold", "secret", "thoughtful", "weird", "mysterious", "uncanny", "spark", "wunder", "unique",  "smart", "sharp", "imaginary", "original","magically", "perfect", "talking", "dancing", "human", "wicked", "lucky", "sweet", "angry", "beautiful", "handsome", "hungry", "brave"]
adjs_human_playful = ["spooky", "playful", "joyful", "joyous", "cheerful", "jubilant", "exuberant", "spirited", "delightful", "upside-down", "ease of mind", "thrilled", "euphoric", "affectionate", "wonder", "pleasant", "pleasing", "enchanted", "fascinating", "charismatic", "delightful", "youthful", "youth", "generation", "misplaced", "furry", "express", "improvised", "silly", "curious"]
# adjs_human_colors = ["yellow", "blue", "red", "black", "violet", "orange", "turquoise"]
adjs_human_nature = ["hot", "cold"]
adjs_human_audacious = ["greatest", "ingenious", "audacious", "force", "incredible", "mastery", "world", "explosion", "tide", "universal", "upward", "forward", "powerful", "dangerous", "broken"]
adjs_human_honest = ["noble", "tiny", "genuine", "candid", "sincere", "loyal", "pure", "nude", "honest", "natural", "mindful", "easy", "compact", "almost", "strange", "simple"]
adjs_human_opposite = ["bound", "opposite","impossible", "vain", "absurd", "wild", "undoable", "unreasonable"]
adjs_latin = ["pre-", "post-", "ab-", "ex-", "semi-", "ultra-", "hyper-"]

adjs_human = adjs_latin + adjs_human_food + adjs_human_travel + adjs_human_philsophy + adjs_human_relationship + adjs_human_antropomorphism + adjs_human_playful + adjs_human_nature + adjs_human_audacious + adjs_human_honest + adjs_human_opposite

adjs_tech_applied_experimental = ["compact", "scientific", "exploratory"]
adjs_tech_algorithm = ["recurrence", "volatile", "stochastic", "unknown", "algorithmic", "rapid", "deterministic", "unresolved", "random"]
adjs_tech_inventive = ["future", "breakthrough"]
adjs_tech_scientific = ["space", "infinite", "discrete", "indiscrete", "high-dimensional", "parallel", "absolute", "relative", "quantum", "super-",  "exo", "nano", "isometric", "continuous", "singular", "negative"]
adjs_tech_abstract = ["indescribable", "invariant", "Intangible", "Impalpable", "Undecidable", "Ethereal", "Spectral", "recursive", "meta"]

adjs_tech = adjs_latin + adjs_tech_applied_experimental + adjs_tech_algorithm + adjs_tech_inventive + adjs_tech_scientific + adjs_tech_abstract

words_tech = adjs_tech + things_tech
words_human = adjs_human + things_human



def tuple_to_str(tuple):
    return " ".join(tuple)

human_tech_word_combos = [tuple_to_str(combo) for combo in chain.from_iterable([list(zip(words_tech, [thing] * len(words_tech))) for thing in things_human])]
tech_human_word_combos = [tuple_to_str(combo) for combo in chain.from_iterable([list(zip(words_human, [thing] * len(words_human))) for thing in things_tech])]

# things_and_adjs = things + adjs
# of_the_words = ["algorithms", "world", "logic", "machines", "play", "dream", "universe", "theories", "future", "loop", "mind"]
# things_combined_word_combos = [combo[0] + " of the " + combo[1] for combo in chain.from_iterable([list(zip([thing] * len(things_and_adjs), things_and_adjs)) for thing in of_the_words])]


word_combos = human_tech_word_combos + tech_human_word_combos

import pprint
pprint.pprint(word_combos)
