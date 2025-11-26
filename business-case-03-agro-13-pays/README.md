# 📦 BUSINESS CASE 03 – AGRO-FOOD MULTI-COUNTRY (13 PAYS)

## **Demand Planning • Supply Chain • Forecasting • Power BI • FMCG Analytics**

---

### **👋 INTRODUCTION & CONTEXTE**

Ce cas pratique place l'analyste au cœur d'une multinationale agro-alimentaire opérant dans 13 marchés européens distincts. Le rôle exige la capacité à **centraliser, harmoniser et modéliser des données complexes et multi-dimensionnelles** afin de résoudre les défis réels d'un environnement FMCG (Fast-Moving Consumer Goods).

Le cœur de l'enjeu réside dans la standardisation des informations pour comprendre l'impact des facteurs macroéconomiques (météo, jours fériés, promotions) sur la demande et optimiser le service client à l'échelle continentale.

---

### **🎯 OBJECTIF STRATÉGIQUE DU BUSINESS CASE**

L'objectif est double : **Standardiser l'analyse** et **Modéliser la performance** pour :

* Améliorer la **Forecast Accuracy** (WAPE, MAPE, BIAS) par l'intégration de *drivers* de demande spécifiques.
* Construire une **vision unifiée** de l'activité sur les 13 pays pour supporter les équipes **S&OP** dans leurs arbitrages.
* Fournir un **Dashboard Exécutif** prêt à l'emploi en comité de direction pour des recommandations opérationnelles concrètes.

**🌍 PAYS INCLUS (EUROPE)** : France, Allemagne, Royaume-Uni, Italie, Espagne, Pays-Bas, Pologne, Belgique, Suisse, Portugal, Suède, Norvège, Danemark.

---

### **📁 STRUCTURE DU PROJET & DES DONNÉES**

Le projet est organisé pour une exécution fluide et une analyse Python/Power BI optimisée.

#### **Arborescence Principale**
business-case-03-agro-13-pays/ │ ├── data/ ├── analysis/ ├── dashboard/ ├── notebooks/ ├── README.md └── requirements.txt
#### **Description des Fichiers Clés**

| Fichier | Contenu | Rôle Analytique |
| :--- | :--- | :--- |
| `BC03_SALES_FACT_13C.csv` | Ventes réelles, Prix, Promotions, Stockouts, Météo (Table de faits principale). | **Forecasting & Impact Analysis** |
| `BC03_FORECAST_PLAN_13C.xlsx` | Prévisions mensuelles (Volume/Valeur) et modèles utilisés. | **KPIs de Précision (WAPE, MAPE)** |
| `BC03_PRODUCT_MASTER.xlsx` | Hiérarchie SKU, Catégories (FMCG), Marque, Durée de vie. | **Dimensions (Modèle en Étoile)** |
| `BC03_WEATHER_DATA.csv` | Température, Pluviométrie, Index Météo (0–1). | **Modélisation de Causalité** |
| `BC03_CANNIBALISATION_MATRIX.xlsx` | SKU → SKU cannibalisé, Taux (5 à 40 %), Type overlap. | **Analyse d'Élasticité Croisée** |
| `BC03_SUPPLY_CHAIN_LEADTIMES.xlsx`| Lead time entrepôt, Politique de sécurité, Fiabilité fournisseur. | **Service Level & Stock de Sécurité** |

---

### **🔍 ANALYSES RÉALISÉES ET MODÉLISATION**

Ce *Business Case* couvre l'intégralité du cycle analytique, du *Data Cleaning* à la recommandation exécutive :

#### **1. Data Cleaning & Standardisation (Preprocessing)**
* Normalisation des formats (dates ISO, devises).
* Harmonisation des données multi-sources.
* Traitement des anomalies, des *outliers* et des ruptures.

#### **2. Performance et Précision (Forecast Accuracy)**
* Calcul et décomposition des KPIs (WAPE, MAPE, BIAS, *Rolling 3 months accuracy*).
* Analyse de l'**Impact des Ruptures** (*Lost Sales*).

#### **3. Modélisation Avancée**
* **Price Elasticity Analysis :** Corrélation Prix → Volume, élasticité directe et croisée.
* **Seasonality Modeling :** Détection des patterns par pays (impact été/boissons, Noël, Ramadan).
* **Supply Chain & Service Level :** Analyse de la fiabilité du *Lead Time* et calcul du *Safety Stock* (Min/Max, Service Level).

#### **4. S&OP & Recommandations Exécutives**
Le rendu final inclut un **Executive Summary** pour le comité S&OP :
* **Amélioration des Modèles :** Recommandations pour l'intégration du Machine Learning et la réduction des biais historiques.
* **Standardisation Pays :** Plan d'action pour harmoniser les processus de *forecasting* et les niveaux de stock de sécurité.
* **Cockpit Exécutif :** Création d'un *dashboard* consolidé multi-marchés.

---

### **💼 LIVRABLES INCLUS & CONTACT**

| Livrable | Format | Description |
| :--- | :--- | :--- |
| **Power BI Dashboard** | `.pbix` | Cockpit exécutif multi-pays, prêt pour la présentation direction. |
| **Notebooks d'analyse** | `.ipynb` | Scripts Python (saisonnalité, KPIs, Price Elasticity). |
| **Données brutes** | `.csv, .xlsx` | 8 tables structurées et complètes. |
| **Documentation** | `.pdf` | Plan d'amélioration S&OP et documentation Data Model. |

<br>

**Auteur :** Roberto Carlos Tientcheu
*Pour toute question ou collaboration :*
* **📧 Email :** tnrc.2025@gmail.com
* **🌐 LinkedIn :** https://www.linkedin.com/in/robertotientcheu


