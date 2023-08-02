import re

def line_to_space(text):
    return re.sub(r"\s+", " ", text.replace('\n', ' '))