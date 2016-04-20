# Auto install new wordpress website with python
## How it works
This script will auto the following tasks for you to create new website wordpress
- Connect MySQL + create new database
- Download latest wordpress source code to doc_root
- Create nginx_vhost php-fpm with defined domain.com
## Requirments
- Directory /tmp/wp must be exist
- Database empty
- nginx_vhost php-fpm sample (i'm working on it.)
## Usage
Download script then defined your input params (database conneciton information, doc_root....)
python2.7 kickstart-wp.py

