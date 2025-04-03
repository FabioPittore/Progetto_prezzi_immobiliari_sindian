### Predizione dei Prezzi Immobiliari a Sindian (Taipei, Taiwan)
L'obiettivo del progetto è quello di sviluppare un modello di regressione lineare per stimare il prezzo al metro quadro (NT$/m²) 
degli immobili nella regione di Sindian, Nuova Taipei, Taiwan, utilizzando il dataset https://archive.ics.uci.edu/ml/datasets/Real+estate+valuation+data+set

### Dataset
- Variabili originali: 
      - età immobile
      - distanza MRT 
      - numero di minimarket
      - latitudine
      - longitudine 
      - prezzo per Ping.
Il prezzo è stato convertito in NT$/m².

### Descrizione del Modello
- Regressione OLS implementata con `statsmodels`.
- Variabili indipendenti:
  - `X5 latitude` -> latitudine dell'abitazione
  - `X6 longitude` -> longitudine dell'abitazione
- Target:
  - `Y house price per m2` -> prezzo al metro quadro dell'abitazione, espresso in dollari taiwanesi.

### Come Eseguire l'Applicazione
1. Scaricare il progetto
2. Installare le librerie necessarie per far girare l'app visibili nel file requirements.txt 
   (anche semplicemente eseguendo il file requirements.ipynb)
3. Avviare la web app streamlit con il comando: streamlit run app.py
4. Saranno visibili i prezzi stimati dal modello alle latitudini e longitudini del quartiere Sindian di Taipei, Taiwan.

### Mappa Interattiva dei Prezzi Immobiliari
Per esplorare i prezzi degli immobili geolocalizzati, consultare la visualizzazione interattiva su Tableau Public:
(https://public.tableau.com/app/profile/filippo.picciriello/viz/PrezziimmobiliariaSindianTaipei/Foglio1)
La mappa mostra ogni immobile con la sua posizione (latitudine e longitudine) e il prezzo al metro quadro (NT$/m²).  




