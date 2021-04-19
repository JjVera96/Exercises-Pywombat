import zipfile

files = {
    'anubisdb': ['Backups/anubisdb20210317.sql'],
    'egcdb': ['Backups/egcdb20200831.sql','Backups/egcdb20200916.sql']
}

NAME  = 'comprimido.zip'
with zipfile.ZipFile(NAME, 'w') as zip_file:
    for key, value in files.items():
        for f in value:
            zip_file.write(f, '{}/{}'.format(key, f.split('/')[-1]))
