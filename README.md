# IP Grabber Tool

Questo strumento è stato sviluppato a scopo educativo per creare script Python che ottengono l'indirizzo IP locale o pubblico e lo inviano a un webhook Discord.

Questo strumento consente di generare script Python che possono ottenere l'indirizzo IP locale o pubblico del dispositivo e inviarlo automaticamente a un webhook Discord. È utile per monitorare e registrare l'indirizzo IP del dispositivo utilizzato.

### Utilizzo

Il tool offre le seguenti opzioni:

1. **IP Locale**
   - Questa opzione genera uno script che ottiene l'indirizzo IP locale del dispositivo e lo invia al webhook Discord configurato.

2. **IP Pubblico**
   - Questa opzione genera uno script che ottiene l'indirizzo IP pubblico del dispositivo utilizzando il servizio ipify.org e lo invia al webhook Discord configurato.

3. **Esci**
   - Termina l'esecuzione dello script.

# Finalizzazione

Una volta creato il tutto dopo aver scelto una delle seguenti opzioni, e necessario convertire il file Python creato dalle opzioni in un file di tipo Eseguibile e poi se eseguito da un'altra persona poi verrà appunto caricato nel webhook l'ip.

### Requisiti

- Python 3.x installato sul sistema
- Moduli Python richiesti: `requests`

### Installazione dei moduli necessari

Prima di utilizzare lo script, assicurati di avere installato il modulo `requests`. Puoi installarlo eseguendo il seguente comando:

```bash
pip install requests
```

# Configurazione

Prima di utilizzare lo strumento, è necessario configurare un webhook Discord per ricevere i messaggi. Segui questi passaggi:

1. **Crea un webhook Discord**
Vai su un server Discord, fai clic destro sul canale in cui desideri ricevere i messaggi, seleziona "Modifica canale" e poi "Webhooks". Clicca su "Crea Webhook" e segui le istruzioni per generare il webhook.

1. **Copia l'URL del webhook**
Copia l'URL del webhook generato. Questo URL sarà utilizzato nello script per inviare l'IP.

# Utilizzo dello script

1. **Clona il repository**
```bash
git clone <url_del_tuo_repository>
cd ip-grabber-tool
```

2. **Esegui lo script**
Esegui il tool con Python per generare lo script desiderato:
```bash
python ip_grabber_tool.py
```
Segui le istruzioni a schermo per selezionare l'opzione desiderata (IP Locale, IP Pubblico o Esci), inserire l'URL del webhook Discord e generare lo script.

# Dichiarazioni di responsabilità

Questo strumento è stato creato esclusivamente a scopo educativo. L'autore non assume alcuna responsabilità per l'uso improprio, non autorizzato o illegale di questo strumento. È responsabilità dell'utente utilizzare questo strumento in conformità alle leggi e alle normative locali. Prima di utilizzare questo strumento su qualsiasi rete o sistema, assicurati di avere le autorizzazioni necessarie.
