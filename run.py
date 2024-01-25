import asyncio
from services.ConfigService import ConfigService
from services.UploadService import UploadService

def runner(): 
    configData = ConfigService.get_clientData_instance('config.yml')
    token = configData.get_token()
    backups = configData.get_backups()

    uploadService = UploadService(token)

    asyncio.run(uploadService.upload_all(backups))
    return 0

runner()
print("[LOG] LOADING FINISHED")
