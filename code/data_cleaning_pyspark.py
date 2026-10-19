# ==============================================================================
# PIPELINE ETL DI DATA CLEANSING CON PYSPARK (GOOGLE COLAB)
# AdventureWorks - Preparazione dati per ingestione SQL Server
# ==============================================================================

# 1. Installazione e Importazione delle Dipendenze
!pip install pyspark -q

import os
import glob
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from google.colab import files

# 2. Inizializzazione della SparkSession in modalità distribuita locale
spark = SparkSession.builder \
    .appName("Data_Cleaning_Pipeline_Enterprise") \
    .master("local[*]") \
    .getOrCreate()

print("[+] SparkSession avviata con successo! Versione:", spark.version)

# 3. Ingestione Dati con Inferenza Automatica dello Schema
# (Sostituisci "dataset_grezzo.csv" con il nome del file caricato su Colab)
raw_df = spark.read.csv("dataset_grezzo.csv", header=True, inferSchema=True)
print(f"[+] Dataset Grezzo Caricato. Righe totali: {raw_df.count()}")

# 4. Pulizia Dati: Deduplicazione Totale
df_dedup = raw_df.dropDuplicates()

# 5. Gestione Selettiva dei Valori Mancanti sulle Colonne Critiche (es. Vendite/Clienti)
cleaned_df = df_dedup.dropna(subset=["SalesOrderNumber", "CustomerKey", "ProductKey", "OrderDateKey"])
print(f"[+] Pulizia completata. Righe finali validate: {cleaned_df.count()}")

# 6. Consolidamento a Singola Partizione di Memoria per Export CSV
output_dir = "temp_export"
cleaned_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(output_dir)

# 7. Post-Processing: Rinomina Dinamica e Standardizzazione del File
part_file = glob.glob(f"{output_dir}/part-*.csv")[0]
final_filename = "FactInternetSales_pulita.csv"
os.rename(part_file, final_filename)

print(f"[+] File pronto: {final_filename}. Avvio del download automatico sul computer...")
files.download(final_filename)
