import os
import re

def salty_language(text):
    """
    Inspired by this:https://pythonz.net/references/named/re.sub/
    and this:
    https://stackoverflow.com/questions/41662001/uppercasing-letters-after-and-signs-in-python
    Transforms normal text to 'solyanoy' language:
    Adds 'с' after each vowel and repaets this vowel after 'c'.
    Returns the transformed text.
    """
    output_text = re.sub(r'([аеёиоыуэюяАЕЁИОУЭЮЯЫ])', r'\1c\1', text)
    punc_filter = re.compile('([.!?]\s*)')
    split_with_punctuation = punc_filter.split(output_text)
    final = ''.join([i.capitalize() for i in split_with_punctuation])
    return final


def extract_chords(file_path = 'data/song.txt'):
    """
    Extract chords from a text file containing them and song lyrics.
    As input takes a text file containing song lyrics.
    Returns a set of unique chords found in the song lyrics.
    """
    pattern = re.compile(r'\b[A-Z]\S*')
    with open(file_path, 'r') as file:
        text = file.read()
        chords = re.findall(pattern, text)
    return set(chords)

    return chords_found

