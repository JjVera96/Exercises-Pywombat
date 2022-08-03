# https://pywombat.com/my/exercises/521e87ef

from collections import Counter

if __name__ == '__main__':
    text = """
    These visions faded when I perused, for the first time, those poets
    whose effusions entranced my soul and lifted it to heaven.  I also
    became a poet and for one year lived in a paradise of my own creation;
    I imagined that I also might obtain a niche in the temple where the
    names of Homer and Shakespeare are consecrated.  You are well
    acquainted with my failure and how heavily I bore the disappointment.
    But just at that time I inherited the fortune of my cousin, and my
    thoughts were turned into the channel of their earlier bent.
    """

    words = text.split()
    counts = Counter(words)
    word = counts.most_common()[1]
    print('"{}" se repite {} veces.'.format(word[0], word[1]))

