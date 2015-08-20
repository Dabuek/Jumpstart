#!/usr/bin/python
# Developed by Daniel Stewart
# Release 0.1 18/09/2015
import os, zipfile

if not os.path.exists('/opt/oracle'):
	os.makedirs('/opt/oracle')

os.system("cd /opt/oracle")

dir_name = '/opt/oracle'

for x in range(0,2):
	for item in os.listdir(dir_name):
		if item.endswith('.zip'):
			file_name = os.path.abspath(item)
			zip_ref = zipfile.ZipFile(file_name)
			zip_ref.extractall(dir_name)
			zip_ref.close()
			os.remove(file_name)

os.system("cd instantclient_12_1; ln libclntsh.so.12.1 libclntsh.so")
os.system("echo 'export PATH=$PATH:/opt/oracle/instantclient_12_1' >> ~/.bashrc")
os.system("echo 'export SQLPATH=/opt/oracle/instantclient_12_1' >> ~/.bashrc")
os.system("echo 'export TNS_ADMIN=/opt/oracle/instantclient_12_1' >> ~/.bashrc")
os.system("echo 'export LD_LIBRARY_PATH=/opt/oracle/instantclient_12_1' >> ~/.bashrc")
os.system("echo 'export ORACLE_HOME=/opt/oracle/instantclient_12_1' >> ~/.bashrc")
os.system("cd ruby-oci8-ruby-oci8-2.1.7; apt-get install ruby-dev; make && make install")

print "Oracle Support Complete"

