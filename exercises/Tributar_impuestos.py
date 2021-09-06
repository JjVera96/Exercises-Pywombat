if __name__ == '__main__':
    l = ['You',  'will',  'rejoice',  'to',  'hear',  'that',
        'no',  'disaster', 'has',  'accompanied',  'thecommencement',  'of',
        'an',  'enterprise',  'which',  'you',  'have',  'regarded',  
        'with',  'such',  'evilforebodings.', 'I',  'arrived',  'here', 'yesterday,', 
        'and',  'my',  'first',  'task',  'is',  'to',  'assuremy',  'dear',
        'sister',  'of',  'my',  'welfare',  'and',  'increasing',  'confidence', 
        'in',  'the',  'successof',  'my',  'undertaking.']

    words = list(set(map(lambda x: (x, l.count(x)), l)))
    ordered = sorted(words, key=lambda x: x[1], reverse=True)[0:3]
    print(ordered)