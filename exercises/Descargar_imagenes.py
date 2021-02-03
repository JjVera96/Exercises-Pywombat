import requests
import os

def download_image(url, path):
    if os.path.isdir(path):
        return print('Is a directory: "{}"'.format(path))
    if not os.path.isdir('/'.join(path.split('/')[0:-1])) or not os.path.exists('/'.join(path.split('/')[0:-1])):
        return print('Is not a directory: "{}"'.format('/'.join(path.split('/')[0:-1])))
    r = requests.get(url)
    if r.status_code == 200:
        with open(path, 'wb') as f:
            f.write(r.content)
        return print('Image download!')
    else:
        return print('Error in download')


download_image('https://i.imgur.com/Ce5BQk3.png', '../resources/modulo_logging.png')

download_image('https://i.imgur.com/rNYQkZC.png', '../resources/expresiones_lambdas.png')

download_image('https://i.imgur.com/dOW1cXb.png', '../resources/')
