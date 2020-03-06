apt-get update
apt-get -u upgrade
apt-get install python3-dev
update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
update-alternatives --install /usr/bin/python python /usr/bin/python3.7 2
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py

# https://dev.mysql.com/doc/refman/8.0/en/linux-installation-debian.html
wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-server_8.0.19-1debian10_amd64.deb-bundle.tar
tar -xvf mysql-server_8.0.19-1debian10_amd64.deb-bundle.tar
apt-get install libaio1
dpkg-preconfigure mysql-community-server_8.0.19-1debian10_amd64.deb
dpkg -i mysql-common_8.0.19-1debian10_amd64.deb
dpkg -i mysql-community-client-core_8.0.19-1debian10_amd64.deb
dpkg -i mysql-community-client_8.0.19-1debian10_amd64.deb
dpkg -i mysql-client_8.0.19-1debian10_amd64.deb
dpkg -i mysql-community-server-core_8.0.19-1debian10_amd64.deb
apt-get -f install
dpkg -i mysql-community-server-core_8.0.19-1debian10_amd64.deb
dpkg -i mysql-community-server_8.0.19-1debian10_amd64.deb
apt-get -f install
dpkg -i mysql-community-server_8.0.19-1debian10_amd64.deb
dpkg -i libmysqlclient21_8.0.19-1debian10_amd64.deb
dpkg -i libmysqlclient-dev_8.0.19-1debian10_amd64.deb

apt-get install gcc libssl-dev

pip install mysqlclient
pip install django
apt-get install git

wget https://gist.githubusercontent.com/yoshiomori/1e6a1a21c608e339ecf23c8b64d7e2e0/raw/ac05cebddda11ec6a1a1a9c21b80fa0b4197da5a/configdb.sql
mysql -p -e "source configdb.sql"
git clone https://github.com/yoshiomori/Investment.git
cd Investment

# Você pode precisar configurar as variávei de ambiente para rodar os
# seguinte comando
python manage.py migrate

python manage.py loaddata menu-bar

python manage.py createsuperuser
python manage.py runserver 0.0.0.0:80