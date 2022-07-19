import os
import io


from service import Create_Service
from googleapiclient.http import MediaIoBaseDownload

CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
API_NAME ='drive'
API_VERSION = 'V3'
SCOPES =['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

file_ids = ['175W2NqWsNn2pmVli3W3deNcEPj', '1fJRNASBa996q9FX92c1c8K3xNXpNQRSh']
file_names = ['download.xlsm', 'retriever.jpeg']

for file_id, file_name in zip(file_ids, file_names):
     request = service.files().get_media(fileId=file_id)
     
     fh = io.BytesIO()
     downloader = MediaIoBaseDownload(fd=fh, request=request)
     
     done= False
     
     while not done: 
         status, done = downloader.next_chunk()
         print('Download progress{0}'.format(status.progress() * 100))
         
         fh.seek(0)
         
         with open(os.path.join('./Random Files', file_name), 'wb') as f:
             f.write(fh.read())
             f.close()
               
               
     


