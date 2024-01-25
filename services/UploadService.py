import asyncio
import yadisk

class UploadService:
    def __init__(self, client_id):
        self.client = yadisk.AsyncClient(token=client_id)
        self.token = client_id

    async def upload_all(self, backups):
        print("[LOG] LOADING STARTED...")
        tasks = [self.upload_backup(backup) for backup in backups]
        await asyncio.gather(*tasks)

    async def validate_token(self):
        print(await self.client.check_token(self.token))
        
    async def upload_backup(self, backup):
        await self.client.upload(backup.get_path(), backup.get_dst_path())

