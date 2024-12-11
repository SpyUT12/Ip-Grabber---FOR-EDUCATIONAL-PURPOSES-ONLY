# IP Grabber Tool

Questo strumento è stato sviluppato a scopo educativo per creare script Python che ottengono l'indirizzo IP locale o pubblico e lo inviano a un webhook Discord.

## Funzionamento

### Descrizione

Questo strumento consente di generare script Python che possono ottenere l'indirizzo IP locale o pubblico del dispositivo e inviarlo automaticamente a un webhook Discord. È utile per monitorare e registrare l'indirizzo IP del dispositivo utilizzato.

### Utilizzo

Il tool offre le seguenti opzioni:

1. **IP Locale**
   - Questa opzione genera uno script che ottiene l'indirizzo IP locale del dispositivo e lo invia al webhook Discord configurato.

2. **IP Pubblico**
   - Questa opzione genera uno script che ottiene l'indirizzo IP pubblico del dispositivo utilizzando il servizio ipify.org e lo invia al webhook Discord configurato.

3. **Esci**
   - Termina l'esecuzione dello script.

### Requisiti

- Python 3.x installato sul sistema
- Moduli Python richiesti: `requests`

### Installazione dei moduli necessari

Prima di utilizzare lo script, assicurati di avere installato il modulo `requests`. Puoi installarlo eseguendo il seguente comando:

```bash
pip install requests
