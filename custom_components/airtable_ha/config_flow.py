import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import config_validation as cv

from .const import DOMAIN, UPDATE_INTERVAL_MINUTES

_LOGGER = logging.getLogger(__name__)

class AirtableConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Airtable."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            # Normally, start OAuth flow here and save tokens
            return self.async_create_entry(
                title="Airtable",
                data=user_input
            )
        data_schema = vol.Schema({
            vol.Required("client_id"): str,
            vol.Required("client_secret"): str,
            vol.Required("base_id"): str,
            vol.Optional("update_interval", default=UPDATE_INTERVAL_MINUTES): int,
        })
        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )

    # Add more steps for OAuth, table selection, etc.

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return AirtableOptionsFlowHandler(config_entry)

class AirtableOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)
        options_schema = vol.Schema({
            vol.Optional("update_interval", default=self.config_entry.options.get("update_interval", UPDATE_INTERVAL_MINUTES)): int,
        })
        return self.async_show_form(
            step_id="init", data_schema=options_schema
        )
