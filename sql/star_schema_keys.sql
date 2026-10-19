-- ==============================================================================
-- 1. PREPARAZIONE: IMPOSTAZIONE OBBLIGATORIA "NOT NULL" SULLE CHIAVI
-- ==============================================================================
ALTER TABLE dbo.DimProduct_pulita ALTER COLUMN ProductKey INT NOT NULL;
ALTER TABLE dbo.DimCustomer_pulita ALTER COLUMN CustomerKey INT NOT NULL;
ALTER TABLE dbo.DimDate_pulita ALTER COLUMN DateKey INT NOT NULL;
ALTER TABLE dbo.DimSalesTerritory_pulita ALTER COLUMN SalesTerritoryKey INT NOT NULL;
ALTER TABLE dbo.DimPromotion_pulita ALTER COLUMN PromotionKey INT NOT NULL;
ALTER TABLE dbo.DimCurrency_pulita ALTER COLUMN CurrencyKey INT NOT NULL;

ALTER TABLE dbo.FactInternetSales_pulita ALTER COLUMN SalesOrderNumber NVARCHAR(20) NOT NULL;
ALTER TABLE dbo.FactInternetSales_pulita ALTER COLUMN SalesOrderLineNumber TINYINT NOT NULL;
GO

-- ==============================================================================
-- 2. CREAZIONE DELLE CHIAVI PRIMARIE (PRIMARY KEYS - PK)
-- ==============================================================================
ALTER TABLE dbo.DimProduct_pulita ADD CONSTRAINT PK_DimProduct PRIMARY KEY CLUSTERED (ProductKey);
ALTER TABLE dbo.DimCustomer_pulita ADD CONSTRAINT PK_DimCustomer PRIMARY KEY CLUSTERED (CustomerKey);
ALTER TABLE dbo.DimDate_pulita ADD CONSTRAINT PK_DimDate PRIMARY KEY CLUSTERED (DateKey);
ALTER TABLE dbo.DimSalesTerritory_pulita ADD CONSTRAINT PK_DimSalesTerritory PRIMARY KEY CLUSTERED (SalesTerritoryKey);
ALTER TABLE dbo.DimPromotion_pulita ADD CONSTRAINT PK_DimPromotion PRIMARY KEY CLUSTERED (PromotionKey);
ALTER TABLE dbo.DimCurrency_pulita ADD CONSTRAINT PK_DimCurrency PRIMARY KEY CLUSTERED (CurrencyKey);

ALTER TABLE dbo.FactInternetSales_pulita ADD CONSTRAINT PK_FactInternetSales PRIMARY KEY CLUSTERED (SalesOrderNumber, SalesOrderLineNumber);
GO

-- ==============================================================================
-- 3. CREAZIONE DELLE CHIAVI ESTERNE (FOREIGN KEYS - FK / STAR SCHEMA)
-- ==============================================================================
ALTER TABLE dbo.FactInternetSales_pulita ADD CONSTRAINT FK_FactInternetSales_DimProduct FOREIGN KEY (ProductKey) REFERENCES dbo.DimProduct_pulita(ProductKey);
ALTER TABLE dbo.FactInternetSales_pulita ADD CONSTRAINT FK_FactInternetSales_DimCustomer FOREIGN KEY (CustomerKey) REFERENCES dbo.DimCustomer_pulita(CustomerKey);
ALTER TABLE dbo.FactInternetSales_pulita ADD CONSTRAINT FK_FactInternetSales_DimDate_OrderDate FOREIGN KEY (OrderDateKey) REFERENCES dbo.DimDate_pulita(DateKey);
ALTER TABLE dbo.FactInternetSales_pulita ADD CONSTRAINT FK_FactInternetSales_DimSalesTerritory FOREIGN KEY (SalesTerritoryKey) REFERENCES dbo.DimSalesTerritory_pulita(SalesTerritoryKey);
ALTER TABLE dbo.FactInternetSales_pulita ADD CONSTRAINT FK_FactInternetSales_DimPromotion FOREIGN KEY (PromotionKey) REFERENCES dbo.DimPromotion_pulita(PromotionKey);
ALTER TABLE dbo.FactInternetSales_pulita ADD CONSTRAINT FK_FactInternetSales_DimCurrency FOREIGN KEY (CurrencyKey) REFERENCES dbo.DimCurrency_pulita(CurrencyKey);
GO
