def remove_prefix(sentence , prefix):
    return sentence.replace(prefix, "")

print(remove_prefix('transcribe_subtitles.srt', 'transcribe_'))
print(remove_prefix('_example.txt', '_'))
print(remove_prefix('backup_20201231_pywombat', 'backup_'))