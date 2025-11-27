# 📦 Business Case 04 – E-commerce Intermittent Demand (Croston)
### *Forecast intermittent demand using Croston variants and benchmark naïve models*

---

## 🛒 1. Contexte métier

Vous êtes **Demand Planner E-commerce** dans une marketplace opérant dans **12 pays**.  
Votre portefeuille comprend **2 500 produits longue traîne**, typiques du e-commerce :

- Produits saisonniers  
- Produits premium à faible rotation  
- Accessoires niche  
- Pièces détachées  
- Articles spécialisés

Plus de **70% des SKUs ont une demande intermittente** :

- Beaucoup de zéros  
- Quelques pics isolés  
- Variabilité extrême  
- Sensibilité aux promotions

Dans ce contexte, les modèles classiques (ARIMA, Holt-Winters, ETS) **échouent**.  
Vous devez identifier un modèle robuste pour prédire la demande faible, irrégulière, imprévisible.

---

## 🎯 2. Objectifs du Business Case

### 🔍 Modélisation & Analyse
- Classifier les SKUs selon leur **pattern de demande** :  
  *intermittent, lumpy, smooth, erratic*
- Implémenter les modèles spécialisés :  
  - Croston  
  - SBA (Syntetos-Boylan Approximation)  
  - TSB (Teunter-Syntetos-Babai)
- Comparer avec des modèles baseline :  
  - Naive  
  - Simple Exponential Smoothing  
  - Moving Average  
- Évaluer la performance avec les KPIs recommandés :
  - MAE, RMSE  
  - sMAPE  
  - MASE  
  - MAAPE  
  - Bias

### 📊 Production analytique
- Construire un **dashboard Power BI** avec :  
  - Forecast accuracy  
  - Classification intermittente  
  - Review SKU-level  
  - Impact inventaire / stockouts  
  - Simulation Safety Stock

### 🧭 Recommandations opérationnelles
- Sélection du **meilleur modèle par catégorie**
- Ajustement des **paramètres S&OE/S&OP**
- Optimisation inventaire (min/max, safety stock)
- Nettoyage des SKUs non rentables

---

## 📁 3. Structure des données

### ✔ Fichier 1 — `sales_ecom_intermitent.csv`  
**24 mois × 3000 SKUs (~2M lignes)**  
Colonnes :

- Date  
- SKU  
- Category  
- Subcategory  
- Country  
- Units_Sold  
- Price  
- Promo_Flag  
- Stockout_Flag  
- Channel  

**Caractéristiques du dataset :**
- 70% de valeurs nulles (demande intermittente)
- Pics irréguliers
- Promotions aléatoires
- Stockouts simulés
- Pays multi-canaux

---

### ✔ Fichier 2 — `sku_master_ecom.xlsx`

- SKU  
- Name  
- Category  
- Subcategory  
- Brand  
- Launch_Date  
- Lifestage  
- Discontinuation_Flag  

---

### ✔ Fichier 3 — `inventory_ecom.csv`

- Date  
- SKU  
- Beginning_Inventory  
- Ending_Inventory  
- Stockout_Flag  
- Lead_Time_days  

---

### ✔ Fichier 4 — `marketing_calendar.csv`

- Date  
- Campaign_Name  
- Campaign_Type  
- SKU_Targeted  
- Discount_pct  

---

## 🧠 4. Modèles à implémenter

### 🔹 Croston Method
Sépare :
- l’intervalle entre ventes  
- la quantité vendue (> 0)

Formule :  
**Forecast = Demand × Interval**

---

### 🔹 SBA (Syntetos-Boylan Approximation)
Correctif de Croston → **moins biaisé**, souvent supérieur.

---

### 🔹 TSB (Teunter-Syntetos-Babai)
Modélise :
- la probabilité d’occurrence  
- la taille de la vente

**Excellente performance quand la série contient énormément de zéros.**

---

## 🧮 5. Modèles baseline

- Naive (t = t-1)  
- Simple Exponential Smoothing (SES)  
- Moving Average (MA3, MA7)  

**Naive est indispensable** pour le calcul du MASE.

---

## 📊 6. KPIs d’évaluation

| KPI | Description |
|------|-------------|
| **MAE** | Interprétation simple, niveau erreur moyen |
| **RMSE** | Sensible aux très gros écarts |
| **MASE** | Standard pour séries intermittentes |
| **sMAPE** | Stable sur faibles volumes |
| **MAAPE** | Renforcé contre les distorsions en low-demand |
| **Bias** | Sur- ou sous-prévision |

---

## 📦 7. Tâches du Business Case

---

### 🔷 **Tâche 1 — Data Cleaning & Preprocessing**

Actions :
- Formatage des dates  
- Suppression SKUs sans ventes  
- Calcul ADI, CV²  
- Détection promotions et ruptures  
- Label : **SKU Demand Pattern**

Livrables :
- `cleaning.ipynb`  
- `sales_cleaned.csv`

---

### 🔷 **Tâche 2 — Classification Intermittente**

Règles :

ADI < 1.32 & CV² < 0.49 → smooth
ADI > 1.32 & CV² < 0.49 → erratic
ADI < 1.32 & CV² > 0.49 → intermittent
ADI > 1.32 & CV² > 0.49 → lumpy


Livrables :
- `pattern_classification.ipynb`  
- Scatterplot ADI vs CV²  

---

### 🔷 **Tâche 3 — Implémentation Croston, SBA, TSB**

Méthodes Python :
- `croston()`  
- `sba()`  
- `tsb()`

Livrables :
- `forecasting_intermitent.ipynb`  
- `forecast_results.csv`

---

### 🔷 **Tâche 4 — Benchmark Global**

Comparaison modèles :
- Croston  
- SBA  
- TSB  
- Naive  
- SES  

Livrables :
- `benchmark_models.ipynb`  
- Tableau MAE/RMSE/MASE  

---

### 🔷 **Tâche 5 — Analyse Inventaire**

Calcul :
- Safety Stock  
- Service level  
- Lost sales  
- Impact stockouts

Livrables :
- Rapport inventaire  
- Fichier Safety Stock  

---

### 🔷 **Tâche 6 — Dashboard Power BI**

Pages recommandées :

**Page 1 — Overview**
- Total SKUs  
- % intermittent  
- Accuracy globale  
- Top SKUs imprévisibles  

**Page 2 — Forecast Comparison**
- Boxplots MASE  
- Winner Model per SKU  
- Visualisations SKU-level  

**Page 3 — Inventory Impact**
- Lost Sales  
- Stockouts  
- Safety Stock Simulation  

**Page 4 — Recommendations**
- S&OP Summary  

Livrable :
- `ecommerce_croston.pbix`

---

### 🔷 **Tâche 7 — Recommandations S&OP**

Inclure :
- Quand utiliser Croston, SBA ou TSB  
- Comment intégrer au cycle S&OE / S&OP  
- Nettoyage du catalogue  
- Promos & pricing  
- Réduction lead time  

Livrable :
- PDF **S&OP Recommendations**

---

## 💼 8. Datasets

- **24 mois, 3000 SKUs**  
- Série chronologique multi-pays  
- Très forte intermittence  
- Promotions irrégulières  
- Stockouts simulés  
- Données prêtes pour Power BI, Python, Excel  

---

---

## ✨ Auteur

**Roberto Carlos TIENTCHEU**  
*Demand & Supply Chain Analyst — Data & Forecasting*  
📧 tnrc.2025@gmail.com  

---




