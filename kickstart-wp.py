import MySQLdb
import urllib
import tarfile
import os

## Requirements
# Dir /tmp/wp/ exist
# db_name does not exist

db_name = 'yourdb_name'
wp_dl = 'https://wordpress.org/latest.tar.gz'
wp_file = '/tmp/wp/wp.tar.gz'
doc_root = '/home/vhosts/domain.com/'
db_user = 'root'
db_pass = 'password'

## Create database first
db = MySQLdb.connect(host="127.0.0.1",user=db_user,passwd=db_pass)
cursor = db.cursor()
sql = 'CREATE DATABASE ' + db_name
try:
        cursor.execute(sql)
except:
        print('Something went wrong: Database exists ?')

## Download latest source code
print('Start downloading latest wordpress...\n')
urllib.urlretrieve(wp_dl, wp_file)

## Extract source
tfile = tarfile.open(wp_file, 'r:gz')
tfile.extractall('/tmp/wp')
print('Extrat done!\n')

## Sync source to DocRoot
print('Start rsync source\n')
os.system("rsync -avrz /tmp/wp/wordpress/ " + doc_root)

## Get sample nginx-php-fpm.vhost.conf, then replace with yours domain

## Reload nginx, done
