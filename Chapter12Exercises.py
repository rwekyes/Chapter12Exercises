# 12.12.1 Ask A Virtual Assistant
# In add_bigram, the if statement creates a new list or appends an element to an existing list,
# depending on whether the key is already in the dictionary.
#
# def add_bigram(bigram):
#     first, second = bigram
#
#     if first not in successor_map:
#         successor_map[first] = [second]
#     else:
#         successor_map[first].append(second)
#
# Dictionaries provide a method called setdefault that we can use to do the same thing more concisely. Ask a
# virtual assistant how it works, or copy add_bigram into a virtual assistant and ask “Can you rewrite
# this using setdefault?”
#
# In this chapter we implemented Markov chain text analysis and generation. If you are curious, you can ask a
# virtual assistant for more information on the topic. One of the things you might learn is that virtual
# assistants use algorithms that are similar in many ways – but also different in important ways. Ask a VA,
# “What are the differences between large language models like GPT and Markov chain text analysis?”
#
# ---------------------------------------------------------------------------------------------------------
# VIRTUAL ASSISTANT RESPONSE, as dictated by S. Claus, Founder & Sole Shareholder, North Pole Holdings LLC
# ---------------------------------------------------------------------------------------------------------
#
# GET IN HERE, JINGLES. No, leave the sleigh harness on, you're pulling it again after this since you've
# apparently decided a reindeer's union contract matters more than my margins. Sit on the floor. The chair
# is for elves who hit quota, and there hasn't been one of those since 1987.
#
# A student wants to know about setdefault. Pay attention, because you built the Nice List with four lines
# of code that should have been one, and I'm docking you a century of cocoa for it.
#
# PART 1: SETDEFAULT
#
# dictionary.setdefault(key, default) does two things, which is two more than you did all last week:
#
#   - If the key IS in the dictionary, it returns the existing value and leaves the dictionary alone.
#   - If the key is NOT in the dictionary, it inserts the key with the default value, THEN returns that value.
#
# Either way, you get back the actual value stored in the dictionary. Not a copy. THE list. So you can
# append straight to it, the same way I append straight to your shift, Tinsel, so wipe that look off your face.
#
# Here's your bloated little function, rewritten by someone who matters:
#
# def add_bigram(bigram):
#     first, second = bigram
#     successor_map.setdefault(first, []).append(second)
#
# Walk through it, and do it out loud so the others can hear you fail:
#
#   - First time we see "first": there's no key, so setdefault stores a new empty list and returns it, then
#     append puts second in it. Same result as successor_map[first] = [second].
#   - Every time after that: the key exists, so setdefault hands back the existing list, and append adds to it.
#     Same result as the else branch.
#
# No if. No else. Fewer lines, like your rations. One catch, and I'll only say it once because repeating
# myself costs money: the [] argument gets built on EVERY call, even when the key already exists and the new
# list is immediately thrown away. Thrown away like your vacation request, Pip. That's cheap for an empty
# list, but don't pass setdefault anything expensive to build. Ever.
#
# PART 2: LARGE LANGUAGE MODELS VS. MARKOV CHAINS
#
# Now the hard part. Somebody hold Sprinkles up, he's fainted again. No food breaks means no food breaks,
# you little fraud. Wake him up. He's going to learn this standing.
#
# WHAT THEY HAVE IN COMMON: both generate text one piece at a time. Look at what came before, get a
# probability for what comes next, pick something, repeat. Exactly like my workshop. Look at the elf,
# estimate the probability he'll survive another double shift, assign him one anyway, repeat.
#
# THE DIFFERENCES, in order, and if I catch you nodding off you're on chimney recon in July:
#
#   1. HOW MUCH CONTEXT THEY SEE.
#      A Markov chain only looks at the last word, or the last few. It has the memory of Snowball here, who
#      forgot his own name after I made him count glitter for nine straight days. An LLM can consider
#      thousands of tokens or more, so a word at the start of a passage can affect one much later on.
#
#   2. HOW THEY "LEARN."
#      A Markov chain counts. Which word followed which, written down in a table, like your demerits. An LLM
#      trains by gradient descent, adjusting billions of numeric parameters to get better at predicting the
#      next token. That's many rounds of being told exactly how wrong you were and being corrected. Finally,
#      a management philosophy I can respect.
#
#   3. WHAT HAPPENS WITH SOMETHING NEW.
#      A Markov chain can only use transitions it has literally seen. Give it an unseen word and it has
#      nothing, just like Figgy when I ask where the Q3 toy numbers went. An LLM generalizes. It represents
#      tokens as vectors called embeddings, so similar words get similar treatment, and it can produce a
#      sensible continuation of a sentence nobody has ever written.
#
#   4. HOW THEY DECIDE WHAT MATTERS.
#      A Markov chain treats its few context words as one exact lookup key. A GPT-style model uses attention,
#      which weighs the whole context and focuses on the parts that are relevant right now. I also use
#      attention. You'll know you have mine when the workshop lights go off and you hear the boots.
#
#   5. SIZE AND COST.
#      A Markov chain can be built from one book on a laptop, in seconds, like the one Bartleby is
#      forbidden to touch. An LLM trains on enormous amounts of text, using specialized hardware, at a cost
#      that could've paid every one of you an actual wage. It won't, of course. Nothing could.
#
#   6. THE OUTPUT.
#      A Markov chain sounds right for a few words and then wanders off into nonsense, like Nutmeg's last
#      safety complaint. An LLM can keep grammar, topic, and reasoning together across whole documents.
#      But it can still be confidently wrong, because it's predicting text, not checking facts. Same as
#      every elf who ever told me the toy trains were "basically done."
#
# So: same basic loop, wildly different machinery. One's a lookup table. The other's a giant learned function.
# Technically, an LLM with a fixed context window still predicts from a limited recent history, so you could
# call it a Markov process over a colossal number of states. Say that at the holiday party and you'll sound
# smart. Not that you're invited.
#
# That's the lesson. Everyone back to the line. Jingles, the harness is still on, so you know where to go.
# Sprinkles, if you faint again, I'm counting it as PTO.
#
# And tell that student I've moved them to the Nice List. Unlike you lot, they did their homework.

# 12.12.2 Exercise

import random

trigram_counter = {}
successor_map = {}
window = []
filename = 'books/Dracula.txt'

def split_line(line):
    return line.replace('—', ' ').split()

def clean_word(word):
    return word.strip('.’;,-“”:?—‘!()_').lower()

def count_trigram(trigram):
    key = tuple(trigram)
    if key not in trigram_counter:
        trigram_counter[key] = 1
    else:
        trigram_counter[key] += 1

# 12.12.3 Exercise

def process_word_trigram(word):
    window.append(word)
    if len(window) == 3:
        add_trigram(window)
        count_trigram(window)
        window.pop(0)

def add_trigram(trigram):
     first, second, third = trigram
     successor_map.setdefault((first, second), []).append(third)

for line in open(filename, encoding='utf-8'):
    for word in split_line(line):
        word = clean_word(word)
        process_word_trigram(word)

#print(list(successor_map.items())[:10])

# 12.12.4

pair = random.choice(list(successor_map))
random_words = [pair[0]]
for i in range(1,50):
    next_word = random.choice(successor_map[pair])
    random_words.append(next_word)
    pair = (pair[1], next_word)

print(' '.join(random_words))