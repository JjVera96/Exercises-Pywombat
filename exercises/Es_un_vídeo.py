import os.path as path

def is_video(file):
    if path.exists(file) and file.split('.')[-1] == 'mp4': return True
    return False
    
print(is_video('../resources/frankenstein.txt'))  # False
print(is_video('C:/Users/JJ/Videos/2020-05-12 08-49-11.mp4'))  # True
