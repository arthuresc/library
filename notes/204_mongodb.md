# MONGODB

#### Instalando o robo3t
Install Robo3t On Ubuntu 18.04
Download the package form Robo3t or using wget
wget https://download.robomongo.org/1.2.1/linux/robo3t-1.2.1-linux-x86_64-3e50a65.tar.gz
Extract here using
tar -xvzf robo3t-1.2.1-linux-x86_64-3e50a65.tar.gz

Make a new floder in usr/local/bin from the package
sudo mkdir /usr/local/bin/robo3t

Move the extracted package to usr/local/bin
sudo mv  robo3t-1.2.1-linux-x86_64-3e50a65/* /usr/local/bin/robo3t

Change directory to cd /usr/local/bin/robo3t/bin
Now, We need to give permission to newly created directory using chmod
sudo chmod +x robo3t ./robo3t

Now we can run Robo3t ./robo3t

We can download the icon for Robo3t from and put it here as we will need to make desktop icon later
For example save it on /bin with name icon.png /usr/local/bin/robo3t/bin/icon.png

mv icon.png /usr/local/bin/robo3t/bin

To make desktop icon for Robo3t, we can make a file in usr/share/applications
sudo nano /usr/share/applications/robo3t.desktop

Paste these there and save

[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=Robo3t
Icon=/usr/local/bin/robo3t/bin/icon.png
Exec="/usr/local/bin/robo3t/bin/robo3t"
Comment=Robo3t 
Categories=Development;
Terminal=false
StartupNotify=true
Now, we can find the icon in application launcher menu by search for robo3t

### Metodo de instalar o mongo localmente
```bash
  sudo apt-get install mongodb
```

## Comandos no terminal do mongo

### mongo
Para entrar no terminal do mongodb
### show dbs
Mostra os bancos (databases) criados/em uso na maquina

### show collections
Mostra as coleções daquela base de dados

### use dbsName
Faz você dar inicio ao uso e também cria caso não exista o banco que você inseriu o nome, a gravação desse banco só será feita se for criada uma coleção (collection)

### db.createCollection('collectionName')
Cria a collection no banco em uso

### db.checklists.insert()
Insere dados

### db.checklists.save()
Inseri dados

### db.checklists.find()
Acha o valor passado

### db.checklists.deleteOne()
Acha o valor passado

