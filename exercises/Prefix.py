def prefix_exists(sentence, prefix):
    return prefix in sentence

print(prefix_exists('transcribe_subtitles.srt', 'transcribe_'))
print(prefix_exists('_example.txt', '_'))
print(prefix_exists('backup_20201231_pywombat', '_backup'))
