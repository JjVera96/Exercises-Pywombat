words_to_delete = input("Palabras a eliminar, separadas por un espacio: ")

file = open('../resources/frankenstein.txt', 'r')
new_file = open('../resources/frankenstein_v2.txt', 'w')

for line in file:
    for word in words_to_delete.split(" "):
        if word in line:
            line = line.replace(word, "")
    new_file.write(line)

file.close()
new_file.close()