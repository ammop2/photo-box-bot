import pysftp

def upload():
	with pysftp.Connection('qtech.io', username='root', key_filename='~/develop/key.pkk') as sftp:
		sftp.cd('public')
        