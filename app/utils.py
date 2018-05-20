import re


def count_unique_word(text):
    WORD_SPLIT_PATTERN = r"[^\W\d_]+"

    word_gen = (i.group(0) for i in re.finditer(WORD_SPLIT_PATTERN, text))
    set_count = {w for w in word_gen}
    return len(set_count)
