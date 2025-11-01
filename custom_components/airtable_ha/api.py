import aiohttp
import logging

_LOGGER = logging.getLogger(__name__)

class AirtableAPI:
    def __init__(self, access_token, base_id):
        self.access_token = access_token
        self.base_id = base_id
        self.base_url = f"https://api.airtable.com/v0/{base_id}"

    async def get_tables(self):
        # Fetch tables metadata (Airtable does not provide direct endpoint for tables, so you need to know table names)
        # In production, this may come from user input or config
        pass

    async def get_records(self, table_name):
        url = f"{self.base_url}/{table_name}"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    return await response.json()
                _LOGGER.error("Failed to fetch data: %s", await response.text())
                return None
