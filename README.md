# Airtable in Home Assistant

Integrazione custom per Home Assistant che permette di collegare una base Airtable, autenticarsi tramite OAuth, selezionare tabelle e colonne da monitorare, e creare sensori dinamici per visualizzare i dati direttamente in Home Assistant.

## Funzionalità

- Autenticazione OAuth verso Airtable
- Configurazione tramite UI
- Selezione tabelle e colonne da monitorare
- Creazione di sensori per ogni colonna selezionata, con possibilità di legare colonne tra loro (es. spesa ↔ data)
- Aggiornamento dati ogni 30 minuti (personalizzabile)
- Pronto per dashboard e grafici Home Assistant

## Installazione

1. Copia la cartella `custom_components/airtable_ha` dentro la directory `custom_components` della tua installazione Home Assistant
2. Riavvia Home Assistant
3. Vai su Impostazioni → Integrazioni → Aggiungi Integrazione → Cerca “Airtable”
4. Segui la configurazione guidata

## Roadmap

- [x] Struttura base
- [x] Configurazione via UI e OAuth
- [x] Selettore tabelle/colonne
- [x] Sensori dinamici
- [x] Aggiornamento automatico
- [ ] Relazioni avanzate tra colonne
- [ ] Traduzioni

## Note

L’integrazione permette di monitorare dati dinamici da Airtable (es. spese giornaliere, inventario, log) e usarli in dashboard Home Assistant.