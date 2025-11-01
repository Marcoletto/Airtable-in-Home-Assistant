from homeassistant.helpers.entity import Entity
from .api import AirtableAPI
from .const import DOMAIN, UPDATE_INTERVAL_MINUTES

async def async_setup_entry(hass, config_entry, async_add_entities):
    api = AirtableAPI(
        access_token=config_entry.data["access_token"],
        base_id=config_entry.data["base_id"]
    )
    # Example: user selects table and columns in config
    table_name = config_entry.data.get("table_name")
    columns = config_entry.data.get("columns", [])

    sensors = []
    for col in columns:
        sensors.append(AirtableSensor(api, table_name, col))
    async_add_entities(sensors, True)

class AirtableSensor(Entity):
    def __init__(self, api, table_name, column):
        self._api = api
        self._table_name = table_name
        self._column = column
        self._state = None
        self._attr_name = f"{table_name} {column}"

    async def async_update(self):
        records = await self._api.get_records(self._table_name)
        if records and "records" in records:
            # For example: get latest record value for the column
            value = records["records"][-1]["fields"].get(self._column)
            self._state = value

    @property
    def state(self):
        return self._state

    @property
    def name(self):
        return self._attr_name
