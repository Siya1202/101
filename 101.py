import dropbox

class TransferData:

    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token) 
        with open (file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token='_e6xXOVH85cAAAAAAAAAAbX-FOGOw_BXEClEw6hHfEnZeuc624miCqAoff4Rsuzy'
    transferData=TransferData(access_token)
    file_from='test.txt'
    file_to='/New Folder/test.txt'
    transferData.upload_file(file_from,file_to)
    print('file has been moved')

main()