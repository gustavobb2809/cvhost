from vhost import VHost
import os

def Main():
    while(True):
        serve = input('Nome do servidor: ')
        path = input('Caminho do site: ')

        if os.path.exists(path):
            if os.path.exists(f'/etc/apache2/sites-available/{serve}.conf'):
                print('Site já existe!')
            else:
                Host = VHost(serve, path)
                break
        else:
            print('Site não existe!')

if __name__ == '__main__':
    Main()        