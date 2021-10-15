
import dropbox 

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A6UvZfskkM0Y20EvXx_6CcEsbhL23LkaDj6YcWf3Dhe9cEAVIf3PUa1G9fYbwHq5LUnUrP_odcRnU6TKwwgB8TSPts2Khl28-2J_HzM_QkJ7rZpTNYc-fo4-338T_bngxIjsdF0'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()