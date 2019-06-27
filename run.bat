@echo off
set FLASK_CONFIG=development
set FLASK_APP=run.py
flask run

pause
mysql -u root
CREATE USER ''@'' IDENTIFIED BY '';
CREATE DATABASE ;
GRANT ALL PRIVILEGES ON  . * TO ''@'';

rem to create migrations directory.
flask db init

rem create migration.
flask db migrate

rem upgrade.
flask db upgrade

pause

mysql
root: root
pass: jabed

useraccounts: jabed
pass: 123456
mysql -u root -p

user: jabed_admin
pass: 239416

prjct database
database  jabedproject_db
pass : 239416
