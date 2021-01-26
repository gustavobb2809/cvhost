import os

class VHost:
    def __init__(self, serve, pathP):
        self.serve = serve
        self.pathP = pathP

        self.createSiteConf()
        self.createVhost()
        self.createHost()

    def createSiteConf(self):
        path = f'cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/{self.serve}.conf'
        os.system(path)

    def createVhost(self):
        vhost = """<VirtualHost *:80>
        ServerAdmin admin@host.com
        ServerName %s
        ServerAlias www.%s.com    
        DocumentRoot %s
    
        <Directory %s>
            AllowOverride All
            Require all granted
        </Directory>
</VirtualHost>""" % (self.serve, self.serve, self.pathP, self.pathP)    
   
        mpath  = f'/etc/apache2/sites-available/{self.serve}.conf'
        target = open(mpath, 'w')
        target.write(vhost)
        target.close()  

    def createHost(self):
        a2site = f'a2ensite {self.serve}.conf'
        os.system(a2site)

        nhost = f'echo 127.0.0.1 {self.serve} >> /etc/hosts'
        os.system(nhost) 

        print('Reinciando o apache...')
        os.system('systemctl restart apache2')

        print(f'Finalizado. Acesse:  {self.serve}/')      
