from itertools import chain

words_human_philosophy = ["verve", "anima", "phenomena", "life", "spirit", "intellect", "time",  "beginning", "positivism", "empiricism", "Renaissance", "principle"]
words_human_attribute = ["ignorance", "collective", "soul", "ego", "vitality", "essence"]
words_human_relationship = ["accord", "club", "peace", "closeness", "intimacy", 'family', "fondness", "passion", "sentiment"]
words_human_food = ["cake", "beacon", "coffee", "beans", "pulp"]
words_human_travel = ["movement", "park", "harmony", "nature", "Ahoy"]
words_human_animal = ["creature", "whale", "monkeys"]
words_human_activities = ["darts", "canvas", "pieces"]
words_human_music = ["tempo", "tunes", "melody"]
words_human_cultural = ["modernist", "art deco", "culture", ]
words_human_nature = ["people", "midnight", "sunrise", "sunset", "moon"]
words_human_thinking = ["magic", "thoughts", "conception", "conjectures", "hunch"]
words_human_playful = ["play", "dream", "tinkering"]

words_human = words_human_philosophy + words_human_attribute + words_human_relationship + words_human_food + words_human_travel + words_human_animal + words_human_activities + words_human_music + words_human_cultural + words_human_nature + words_human_thinking + words_human_playful

words_tech_experimental = ["future", "frontier"]
words_tech_intelligence = ["shortcuts", "complexity", "brain", "spark", "mind"]
words_tech_algorithm = ["algorithms", "function", "evolution","deterministic","decision", "random"]
words_tech_computing = ["compute", "engima", "logic", "machines", "byte", "engine", "kernel"]
words_tech_scientific = ["axion", "Equilibrium", "joint", "friction", "synthesis", "projection", "morphology", "hypersphere", "manifold", "vector", "zero", "x", "discrete", "indiscrete", "dimension", "sequence", "factor",  "sphere", "ripple", "fraction", "precision", "scope",  "effect", "theory", "calculus", "vertex", "isometric", "continuous", "squared", "negative"]
words_tech_abstract = ["atlas", "alpha", "beta", "loop"]
words_tech_audacious = ["force", "world", "universe"]

words_tech = words_tech_experimental + words_tech_intelligence + words_tech_algorithm + words_tech_computing + words_tech_scientific + words_tech_abstract + words_tech_audacious

adjs_human_food = ["deep fried", "grilled"]
adjs_human_travel = ["exotic", "breathteaking", "guided"]
adjs_human_philsophy = ["hedonistic", "stoic", "empirical"]
adjs_human_relationship = ["generous", "tender", "stereotypical", "quintessential", "mutual", "friendly"]
adjs_human_antropomorphism = ["spark", "wunder", "unique",  "smart", "virtuoso", "imaginative", "original","magical", "perfect", "talking", "dancing", "playing", "human", "wicked", "lucky", "sweet", "angry", "beautiful", "handsome", "hungry", "brave"]
adjs_human_playful = ["playful", "joyful", "joyous", "cheerful", "jubilant", "exuberant", "spirited", "delightful", "upside-down", "ease of mind", "thrilled", "euphoric", "affectionate", "wonder", "pleasant", "pleasing", "enchanted", "fascinating", "charismatic", "delightful", "youthful", "youth", "generation", "misplaced", "furry", "express", "improvised", "play", "silly", "curious"]
adjs_human_colors = ["yellow", "blue", "red", "black", "violet", "orange", "turquoise"]
adjs_human_nature = ["hot", "cold"]
adjs_human_audacious = ["greatest", "ingenious", "audacious", "force", "incredible", "mastery", "world", "explosion", "tide", "universal", "upward", "forward", "no limit", "powerful", "dangerous", "broken"]
adjs_human_honest = ["noble", "tiny", "genuine", "candid", "sincere", "loyal", "pure", "nude", "honest", "natural", "mindful", "easy", "compact", "almost", "strange", "simple"]
adjs_human_opposite = ["opposite","impossible", "vain", "absurd", "wild", "undoable", "unreasonable"]

adjs_human = adjs_human_food + adjs_human_travel + adjs_human_philsophy + adjs_human_relationship + adjs_human_antropomorphism + adjs_human_playful + adjs_human_colors + adjs_human_nature + adjs_human_audacious + adjs_human_honest + adjs_human_opposite

adjs_tech_applied_experimental = ["scientific", "exploratory", "frontier"]
adjs_tech_algorithm = ["unknown", "algorithmic", "rapid", "deterministic", "unresolved", "random"]
adjs_tech_inventive = ["future"]
adjs_tech_scientific = ["infinite", "discrete", "indiscrete", "high-dimensional", "parallel", "absolute", "relative", "quantum", "super-",  "exo", "nano", "isometric", "continuous", "singular", "squared", "negative"]
adjs_tech_abstract = ["indescribable", "invariant", "Intangible", "Impalpable", "Undecidable", "Ethereal", "Spectral", "recursive", "meta"]

adjs_tech = adjs_tech_applied_experimental + adjs_tech_algorithm + adjs_tech_inventive + adjs_tech_scientific + adjs_tech_abstract


def tuple_to_str(tuple):
    return " ".join(tuple)

human_tech_word_combos = [tuple_to_str(combo) for combo in chain.from_iterable([list(zip(adjs_tech, [thing] * len(adjs_tech))) for thing in words_human])]
tech_human_word_combos = [tuple_to_str(combo) for combo in chain.from_iterable([list(zip(adjs_human, [thing] * len(adjs_human))) for thing in words_tech])]

# things_and_adjs = things + adjs
# of_the_words = ["algorithms", "world", "logic", "machines", "play", "dream", "universe", "theories", "future", "loop", "mind"]
# things_combined_word_combos = [combo[0] + " of the " + combo[1] for combo in chain.from_iterable([list(zip([thing] * len(things_and_adjs), things_and_adjs)) for thing in of_the_words])]


word_combos = human_tech_word_combos + tech_human_word_combos

import pprint
pprint.pprint(word_combos)
