"""Airtable Home Assistant Integration."""

from .const import DOMAIN

async def async_setup_entry(hass, entry):
    """Set up Airtable integration from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_unload_entry(hass, entry):
    """Unload an Airtable config entry."""
    hass.data[DOMAIN].pop(entry.entry_id)
    return True
