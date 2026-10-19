# 🚀 AdventureWorks E-Commerce Sales Pipeline
### Soluzione di Business Intelligence End-to-End (Data Engineering, SQL Server & Power BI)

Progetto sviluppato per il Master in Data Analytics & BI (Link Campus University ).
---

## 🏗️ Panoramica dell'Architettura
Il progetto affronta la criticità iniziale di dati di vendita frammentati, non relazionati e distribuiti in 7 file CSV indipendenti. L'obiettivo è stato trasformare i dati raw in una piattaforma analitica affidabile, governata e interattiva per il management.

Il flusso di lavoro segue una pipeline **End-to-End**:
---

## ⚙️ Fasi di Realizzazione

### 1️⃣ Fase 1: Data Engineering & ETL (Google Colab / PySpark)
* **Origine Dati:** 7 file CSV raw prelevati da Azure Blob Storage (`DimCurrency`, `DimCustomer`, `DimDate`, `DimProduct`, `DimPromotion`, `DimSalesTerritory`, `FactInternetSales`).
* **Pulizia e Trasformazione:** Utilizzo di **Apache Spark (PySpark)** in ambiente Google Colab per:
  * Gestione e pulizia di valori nulli e duplicati (es. scarti di pulizia su `DimProduct`).
  * Normalizzazione dei tipi di dato e dei formati temporali.
* **Salvataggio:** Esportazione dei dataset puliti pronti per la persistenza su database relazionale.

### 2️⃣ Fase 2: Data Modeling & Database Relazionale (SQL Server / SSMS)
* **Importazione:** Caricamento dei file CSV puliti in **SQL Server Management Studio (SSMS)** tramite procedure di importazione flat file.
* **Architettura Star Schema:** Creazione di 6 tabelle dimensionali e 1 tabella dei fatti (`FactInternetSales`), con l'impostazione di **Chiavi Primarie (PK)** e **Chiavi Esterne (FK)** per garantire l'integrità referenziale.
* **Ottimizzazione tramite Viste SQL:** Creazione della vista `dbo.vw_VenditePowerBI` per:
  * Unire lo *star schema* in un'unica vista logica coerente.
  * Integrare colonne calcolate (es. `Profitto = Ricavi - Costi`).
  * Rinominare i campi tecnici in etichette chiare e business-friendly (es. `SalesAmount` ➡️ `Ricavi`).

### 3️⃣ Fase 3: Business Intelligence & Visualizzazione (Power BI)
* **Modello Semantico:** Connessione al database SQL Server e configurazione delle relazioni semantiche.
* **Analisi e KPI:** Sviluppo di dashboard interattive orientate al management per monitorare:
  * Ricavi, profitti e volumi d'ordine nel tempo.
  * Contributo ai ricavi per prodotto, categorie e promozioni.
  * Analisi geografica e territoriale con logica di *drillthrough* (dalla panoramica di alto livello al dettaglio transazionale del singolo cliente/ordine).

---

## 🛠️ Tecnologie Utilizzate
* **Data Engineering & ETL:** Python, PySpark, Google Colab, Azure Blob Storage
* **Database & SQL:** Microsoft SQL Server, SSMS (SQL Server Management Studio), T-SQL
* **Business Intelligence:** Power BI, Modellazione DAX, Star Schema Design
