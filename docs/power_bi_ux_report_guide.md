# 📊 Guida Tecnica e di UX - Report Power BI (AdventureWorks)

Documentazione ufficiale dell'architettura di visualizzazione, modellazione e user experience (UX) sviluppata per il Project Work di Business Intelligence.

---

## 🏗️ 1. Architettura delle Pagine del Report
Il report Power BI è strutturato su **3 pagine di livello enterprise**, progettate per consentire al management di passare autonomamente dalla panoramica ad alto livello fino al micro-dettaglio operativo.

### 📈 Pagina 1: Overview Vendite (Executive Dashboard)
Panoramica complessiva dell'andamento commerciale aziendale.
* **KPI Principali (Card):** Ricavi, Profitti, Margine %, Ordini e Clienti (formattati con font pulito a 24pt).
* **Trend Temporale:** Grafico a linee dei ricavi mensili a confronto con lo stesso periodo dell'anno precedente (`SAMEPERIODLASTYEAR`).
* **Top 10 Prodotti:** Grafico a barre orizzontali filtrato con logica *Top N* basata sui ricavi.
* **Linee di Prodotto:** Grafico a ciambella della distribuzione dei ricavi per linea prodotto.
* **Filtri Interattivi (Slicers):** Slicer a tendina per Anno e Tipo di Promozione.

### 🗺️ Pagina 2: Comportamento Clienti e Territori
Analisi geografica e della base clienti globale.
* **Mappa Geografica Interattiva:** Posizionamento basato sui Paesi con dimensione della bolla proporzionale ai ricavi.
* **Slicer Territoriale:** Filtro dinamico per Continente (`SalesTerritoryGroup`) che propaga la selezione a tutti i visual della pagina.
* **Matrice Top Clienti:** Tabella analitica con i principali acquirenti ordinati per fatturato generato.

### 🔍 Pagina 3: Dettaglio Cliente (Drillthrough Target)
Pagina di approfondimento mono-cliente attivata tramite navigazione verticale.
* **Card Identificativa:** Nome completo del cliente filtrato contestualmente.
* **KPI di Profilo:** Ricavi, profitti, ordini e quantità acquistata dal singolo utente.
* **Tabella Prodotti Acquistati:** Dettaglio analitico degli articoli comprati, ordinati per marginalità.
* **Pulsante Indietro:** Gestione nativa del ritorno alla pagina di origine.

---

## ⚡ 2. Funzionalità Avanzate di User Experience (UX)

Per evitare l'affollamento visivo e guidare lo storytelling aziendale, sono stati implementati tre pilastri di interattività:

1. **Tooltip Personalizzati su Hovering (Pagina Dedicata):**
   * Passando il mouse sopra i Paesi nella mappa geografica, si attiva un mini-report a comparsa che mostra i KPI di area, il totale clienti, i profitti e le percentuali sul totale generale (`Clienti % Totale` e `Prodotti % Totale` calcolate con la funzione `ALL()`).
2. **Drillthrough (Navigazione Verticale):**
   * Configurato sul campo univoco `CustomerKey`. Cliccando con il tasto destro su un cliente o un prodotto da qualsiasi pagina del report, l'utente può "atterrare" nella pagina di dettaglio dedicata ereditando automaticamente il contesto di filtro.
3. **Segnalibri (Bookmarks) e Pulsanti di Reset:**
   * Creazione di pulsanti interattivi collegati a segnalibri dedicati per consentire il reset istantaneo dei filtri applicati e la pulizia della vista.

---

## 📐 3. Scelte di Design ed Ottimizzazione Motore (VertiPaq)
* **Palette di Colori Contenuta:** Utilizzo di toni professionali (blu scuro istituzionale per i titoli e i KPI, azzurro/verde petrolio per i grafici, sfondi neutri).
* **Ordinamento Cronologico Forzato:** Ordinamento della colonna `Mese` tramite una colonna numerica di supporto `AnnoMese_Ordine` (formato `YYYYMM`) per evitare l'ordinamento alfabetico di default di Power BI.
* **Best Practice RAM:** Zero colonne calcolate nella tabella dei fatti per preservare la memoria RAM del motore VertiPaq; utilizzo esclusivo di Misure DAX calcolate *on-the-fly*.
