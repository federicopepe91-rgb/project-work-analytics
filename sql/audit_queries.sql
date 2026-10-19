-- ==============================================================================
-- AUDIT ANALITICO, VALIDAZIONE DELLE JOIN E CONTROLLO DI CONCILIAZIONE (SQL)
-- ==============================================================================

-- 1. QUERY DI BASELINE / SANITY CHECK (Sulla sola Fact Table pulita)
SELECT 
    COUNT(*) AS NumeroRigheVendita, 
    COUNT(DISTINCT SalesOrderNumber) AS NumeroOrdini, 
    COUNT(DISTINCT CustomerKey) AS ClientiConAcquisti, 
    COUNT(DISTINCT ProductKey) AS ProdottiVenduti, 
    SUM(OrderQuantity) AS QuantitaTotaleVenduta, 
    CAST(SUM(SalesAmount) AS DECIMAL(18, 2)) AS RicaviTotali, 
    CAST(SUM(TotalProductCost) AS DECIMAL(18, 2)) AS CostiTotali, 
    CAST(SUM(SalesAmount - TotalProductCost) AS DECIMAL(18, 2)) AS ProfittoTotale 
FROM dbo.FactInternetSales_pulita;

-- 2. ANALISI TOP 20 PRODOTTI PER FATTURATO (Test relazione Product)
SELECT TOP (20) 
    p.ProductKey, 
    p.EnglishProductName AS Prodotto, 
    p.Color, 
    p.ProductLine, 
    SUM(f.OrderQuantity) AS QuantitaVenduta, 
    CAST(SUM(f.SalesAmount) AS DECIMAL(18, 2)) AS Ricavi, 
    CAST(SUM(f.TotalProductCost) AS DECIMAL(18, 2)) AS Costi, 
    CAST(SUM(f.SalesAmount - f.TotalProductCost) AS DECIMAL(18, 2)) AS Profitto 
FROM dbo.FactInternetSales_pulita AS f 
INNER JOIN dbo.DimProduct_pulita AS p ON f.ProductKey = p.ProductKey 
GROUP BY p.ProductKey, p.EnglishProductName, p.Color, p.ProductLine 
ORDER BY Ricavi DESC;

-- 3. ANALISI TEMPORALE GIORNALIERA (Test relazione Calendar/Date)
SELECT 
    d.FullDateAlternateKey AS DataVendita, 
    d.CalendarYear AS Anno, 
    d.CalendarQuarter AS Trimestre, 
    d.MonthNumberOfYear AS NumeroMese, 
    d.EnglishMonthName AS Mese, 
    COUNT(DISTINCT f.SalesOrderNumber) AS NumeroOrdini, 
    SUM(f.OrderQuantity) AS QuantitaVenduta, 
    CAST(SUM(f.SalesAmount) AS DECIMAL(18, 2)) AS Ricavi, 
    CAST(SUM(f.TotalProductCost) AS DECIMAL(18, 2)) AS Costi, 
    CAST(SUM(f.SalesAmount - f.TotalProductCost) AS DECIMAL(18, 2)) AS Profitto 
FROM dbo.FactInternetSales_pulita AS f 
INNER JOIN dbo.DimDate_pulita AS d ON f.OrderDateKey = d.DateKey 
GROUP BY d.FullDateAlternateKey, d.CalendarYear, d.CalendarQuarter, d.MonthNumberOfYear, d.EnglishMonthName 
ORDER BY DataVendita;

-- 4. PROFILAZIONE DEI TOP CLIENTI VIP (Test relazione Customer)
SELECT TOP (20) 
    c.CustomerKey, 
    CONCAT(c.FirstName, ' ', c.LastName) AS Cliente, 
    c.EmailAddress, 
    c.Gender, 
    c.YearlyIncome, 
    COUNT(DISTINCT f.SalesOrderNumber) AS NumeroOrdini, 
    SUM(f.OrderQuantity) AS QuantitaAcquistata, 
    CAST(SUM(f.SalesAmount) AS DECIMAL(18, 2)) AS RicaviGenerati, 
    CAST(SUM(f.SalesAmount - f.TotalProductCost) AS DECIMAL(18, 2)) AS ProfittoGenerato 
FROM dbo.FactInternetSales_pulita AS f 
INNER JOIN dbo.DimCustomer_pulita AS c ON f.CustomerKey = c.CustomerKey 
GROUP BY c.CustomerKey, c.FirstName, c.LastName, c.EmailAddress, c.Gender, c.YearlyIncome 
ORDER BY RicaviGenerati DESC;

-- 5. PERFORMANCE TERRITORIALE E SEGMENTAZIONE GEOGRAFICA (Test relazione Territory)
SELECT 
    t.SalesTerritoryGroup AS Continente, 
    t.SalesTerritoryCountry AS Paese, 
    t.SalesTerritoryRegion AS Regione, 
    COUNT(DISTINCT f.CustomerKey) AS ClientiUnici, 
    COUNT(DISTINCT f.SalesOrderNumber) AS NumeroOrdini, 
    SUM(f.OrderQuantity) AS QuantitaVenduta, 
    CAST(SUM(f.SalesAmount) AS DECIMAL(18, 2)) AS Ricavi, 
    CAST(SUM(f.TotalProductCost) AS DECIMAL(18, 2)) AS Costi, 
    CAST(SUM(f.SalesAmount - f.TotalProductCost) AS DECIMAL(18, 2)) AS Profitto 
FROM dbo.FactInternetSales_pulita AS f 
INNER JOIN dbo.DimSalesTerritory_pulita AS t ON f.SalesTerritoryKey = t.SalesTerritoryKey 
GROUP BY t.SalesTerritoryGroup, t.SalesTerritoryCountry, t.SalesTerritoryRegion 
ORDER BY Ricavi DESC;

-- 6. PROVA DI CONCILIAZIONE FINALE SULLA VISTA (Audit dello Star Schema)
SELECT 
    COUNT(*) AS RigheVendita, 
    COUNT(DISTINCT NumeroOrdine) AS Ordini, 
    COUNT(DISTINCT CustomerKey) AS Clienti, 
    SUM(QuantitaVenduta) AS QuantitaVenduta, 
    SUM(Ricavi) AS RicaviTotali, 
    SUM(Costi) AS CostiTotali, 
    SUM(Profitto) AS ProfittoTotale 
FROM dbo.vw_VenditePowerBI;
