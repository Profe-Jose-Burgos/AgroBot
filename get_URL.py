from azure.storage.blob import BlobServiceClient

storage_account_key = "8dAG94X/66l1ZeMSb/N6tbxLJFS5X8QVUsVzZonskerX+TsbUbZtZWPnAvRMsM5f1vgGymriXiOw+AStyXLa4g=="

storage_account_name = "storagesic"

connection_string = "DefaultEndpointsProtocol=https;AccountName=storagesic;AccountKey=LJQwoxTLtFxV1Cnn8Iw4W5ZDyfG+0rMOUeJnoOUWUFxtKKTNEe+2EoKT8tqV7LWBp6w3wc/sBXbJ+ASt3Mab/w==;EndpointSuffix=core.windows.net"

container_name = "file-holder"

def uploadToBlobStorage(file_path,file_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

    with open(file_path,"rb") as data:
        blob_client.upload_blob(data, overwrite=True)
        print(f"Uploaded{file_name}.")