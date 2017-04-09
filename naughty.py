def replace(string):
    bad_words = [] # list of disallowed words to replace with 'toot'
    for i in bad_words:
        string = string.replace(i, 'toot')
    return string
