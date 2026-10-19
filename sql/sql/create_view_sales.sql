-- ==============================================================================
-- CREAZIONE DELLA VISTA DI UNIONE E BUSINESS LOGIC PER POWER BI
-- ==============================================================================
CREATE VIEW dbo.vw_VenditePowerBI AS
SELECT 
    -- 1. Attributi Temporali
    d.FullDateAlternateKey AS DataVendita, 
    d.CalendarYear AS Anno, 
    d.CalendarQuarter AS Trimestre, 
    d.MonthNumberOfYear AS NumeroMese, 
    d.EnglishMonthName AS Mese,
    
    -- 2. Dettagli Ordine
    f.SalesOrderNumber AS NumeroOrdine, 
    f.SalesOrderLineNumber AS RigaOrdine,
    
    -- 3. Attributi Prodotto
    p.ProductKey, 
    p.EnglishProductName AS Prodotto, 
    p.Color, 
    p.ProductLine,
    
    -- 4. Attributi Cliente
    c.CustomerKey, 
    c.FirstName AS NomeCliente, 
    c.LastName AS CognomeCliente, 
    c.Gender, 
    c.YearlyIncome,
    
    -- 5. Attributi Promozione
    pr.PromotionKey, 
    pr.EnglishPromotionName AS Promozione, 
    pr.EnglishPromotionType AS TipoPromozione, 
    pr.DiscountPct AS PercentualeSconto,
    
    -- 6. Attributi Territoriali
    t.SalesTerritoryGroup AS Continente, 
    t.SalesTerritoryCountry AS Paese,
    
    -- 7. Misure Numeriche e Calcolate
    f.OrderQuantity AS QuantitaVenduta, 
    f.UnitPrice AS PrezzoUnitario, 
    f.SalesAmount AS Ricavi, 
    f.TotalProductCost AS Costi, 
    (f.SalesAmount - f.TotalProductCost) AS Profitto

FROM dbo.FactInternetSales_pulita AS f
INNER JOIN dbo.DimDate_pulita AS d ON f.OrderDateKey = d.DateKey
INNER JOIN dbo.DimProduct_pulita AS p ON f.ProductKey = p.ProductKey
INNER JOIN dbo.DimCustomer_pulita AS c ON f.CustomerKey = c.CustomerKey
INNER JOIN dbo.DimPromotion_pulita AS pr ON f.PromotionKey = pr.PromotionKey
INNER JOIN dbo.DimSalesTerritory_pulita AS t ON f.SalesTerritoryKey = t.SalesTerritoryKey;
GO
