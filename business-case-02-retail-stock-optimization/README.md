# 📘 Business Case 02 — Optimisation des Stocks Retail

## **Demand Planning • Inventory Optimization • Supply Chain Analytics**

---

## **🎯 OBJECTIF ET CADRE DU CAS**

Ce *Business Case* vise à simuler et résoudre les défis fondamentaux de la gestion des stocks dans un environnement de vente au détail (Retail) complexe. L'objectif est de réduire les surstocks, de prévenir les ruptures et d'optimiser l'allocation des produits sur plusieurs points de vente.

### **Jeu de Données Synthétique (Réalisme Élevé)**

Ce jeu de données a été généré de manière programmatique pour répliquer fidèlement les conditions du secteur FMCG/Retail :

* **Échelle :** 120 magasins et 500 références (SKUs).
* **Historique :** 18 mois de données de ventes et de stocks.
* **Complexité :** Intègre une saisonnalité réaliste, des événements promotionnels, des délais fournisseurs et une classification de produits (hiérarchie, *shelf-life*).

---

## **🏪 CONTEXTE BUSINESS ET ENJEUX OPÉRATIONNELS**

Les entreprises de vente au détail sont confrontées à une double contrainte critique :

* **Éviter les ruptures de stock :** Perte de chiffre d'affaires, insatisfaction client, dégradation du taux de service.
* **Éviter les surstocks :** Immobilisation du capital (fonds de roulement), risque d'obsolescence, démarques et coûts de possession.

Ce cas reproduit l'environnement nécessaire pour appliquer les méthodologies suivantes : Modélisation de la prévision, segmentation ABC/XYZ, calcul des stocks de sécurité dynamique (Safety Stock), et logique de réapprovisionnement magasin.

---

## **📦 STRUCTURE DES DONNÉES (Star Schema)**

Le jeu de données suit une architecture en **Schéma en Étoile** (*Star Schema*), garantissant sa compatibilité et sa performance pour les outils BI modernes :

* **Prêt pour :** Power BI, Python (Pandas), moteurs SQL, et *workflows* de Machine Learning.

### **Contenu des Fichiers**

| Fichier | Description |
| :--- | :--- |
| `retail_sales_18months.csv` | Ventes quotidiennes, prévisions, prix, métriques SKU/magasin. |
| `retail_stock_levels_18months.csv` | Stock d'ouverture, stock de clôture, ruptures de stock, indicateurs de réapprovisionnement. |
| `retail_products_master.csv` | Hiérarchie SKU, catégorie, sous-catégorie, marque, durée de vie produit. |
| `retail_stores_master.csv` | Attributs du magasin (taille, région, cluster, score socio-économique). |
| `retail_supplier_leadtime.csv` | Délais fournisseurs (Lead Times), MOQ, variabilité. |
| `retail_calendar_events.csv` | Calendrier promotionnel, jours fériés, événements impactants (paydays). |
| `generate_retail_dataset_single_sales.py` | Script Python permettant de régénérer l'intégralité du jeu de données. |

---

## **🧠 CAS D'USAGE ET ANALYTIQUE CLÉS**

Ce *Business Case* permet de démontrer des compétences avancées dans les domaines suivants :

1.  **Prévision de la Demande :**
    * Analyse des erreurs (`MAPE`, `WAPE`, `Bias`).
    * Modélisation de l'Uplift promotionnel et détection de saisonnalité.
    * *Dashboard* de précision à l'échelle SKU/magasin.
2.  **Optimisation des Stocks :**
    * Calcul du stock de sécurité (Safety Stock) et du Point de Commande (Reorder Point).
    * Jours de Stock (DOI) et Taux de Remplissage (Fill Rate, OSA).
3.  **Segmentation ABC/XYZ :**
    * Rationalisation du portefeuille basée sur la valeur (A/B/C) et la variabilité (X/Y/Z).
    * Définition de politiques de planification prioritaires.
4.  **Analyse des Causes Racines (Root Cause Analysis) :**
    * Analyse de l'impact des ruptures liées à la variabilité du *Lead Time* ou à la capacité logistique.
5.  **Allocation Contrainte (Optionnel) :**
    * Résolution par *Solver* (ou optimisation) pour maximiser le revenu ou le taux de service en situation de pénurie.

---

## **📊 EXEMPLES DE KPI (DAX ou Python)**

| KPI | Formule Conceptuelle |
| :--- | :--- |
| **Forecast Accuracy** | $1 - \frac{\sum | \text{Ventes réelles} - \text{Prévision finale} |}{\sum \text{Ventes réelles}}$ |
| **Service Level** | $\frac{\sum \text{Quantité Servie}}{\sum \text{Demande Totale}}$ |
| **Bias** | $\frac{\sum (\text{Prévision finale}) - \sum (\text{Ventes réelles})}{\sum \text{Ventes réelles}}$ |

---

## **🛠️ UTILISATION ET COMPÉTENCES DÉMONTRÉES**

### **How to Use This Business Case**

1.  Clone the repository:
    ```sh
    git clone [https://github.com/Carlos25-afq/business-cases-scm-demand-planning.git](https://github.com/Carlos25-afq/business-cases-scm-demand-planning.git)
    ```
2.  Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3.  Regenerate the dataset (optional):
    ```sh
    python generate_retail_dataset_single_sales.py
    ```
4.  Load into Power BI or Python and start your analytics based on the Star Schema.

### **Applications Professionnelles**

Ce cas reproduit fidèlement les tâches d'un :

* **Demand Planner** / **Supply Planner**
* **Inventory Controller**
* **S&OP Analyst**
* **Business/Data Analyst** (Secteur FMCG/Retail)

### **Compétences Démontrées**

* *Data Engineering* (génération de données synthétiques)
* *Forecast Modeling*
* Compréhension fine de la Supply Chain Retail
* Optimisation des stocks
* Modélisation avancée Power BI
* *Workflows* d'analyse Python.

---


# 🚀 BUSINESS CASE — 8 TÂCHES PROFESSIONNELLES AVEC PROBLÈMES RÉELS

Ce répertoire propose une série d'exercices structurés, progressifs et réalistes (niveau croissant) pour évaluer et développer des compétences d'expert en Supply Chain, Demand Planning et Data Analytics. Chaque tâche est orientée vers la résolution d'un problème opérationnel réel.

---

## **I. DIAGNOSTIC ET ÉVALUATION DE LA DEMANDE (TÂCHES 1-3)**

### **🟦 TÂCHE 1 — Comprendre le Comportement des Ventes et la Structure Produit (DIAGNOSTIC INITIAL)**

| Bloc | Détail |
| :--- | :--- |
| **❗ Problème** | L’entreprise observe des variations importantes de ventes sans comprendre les produits stratégiques, les magasins moteurs et les saisons clés pour optimiser les stocks. |
| **📁 Fichiers** | `retail_sales_18months.csv`, `retail_products_master.csv`, `retail_stores_master.csv` |
| **🧠 Analyse Attendue** | Détection des produits importants (80/20), identification des périodes de haute et basse saison, segmentation des régions/magasins. |
| **🛠️ Outils** | Excel (TCD, Graphiques), Python (Pandas, Seaborn, Prophet), Power BI (Vues régionales, Cartes). |
| **🎯 Niveau** | Débutant–Intermédiaire (Diagnostic de base mais structuré). |

### **🟩 TÂCHE 2 — Évaluer la Qualité des Prévisions (Forecast KPIs)**

| Bloc | Détail |
| :--- | :--- |
| **❗ Problème** | La direction se plaint d’un manque de fiabilité (MAPE trop élevé, biais négatif entraînant des ruptures, écarts importants entre catégories). Objectif : mesurer précisément la performance. |
| **📁 Fichiers** | `retail_sales_18months.csv` |
| **🧠 Analyse Attendue** | Calcul des **MAPE, WAPE, Biais**, analyse par SKU / Catégorie / Région / Magasin. Identification des prévisions “dangereuses” et recommandations concrètes. |
| **🛠️ Outils** | Excel (Formules, TCD), Python (Forecast Error Metrics), Power BI (Heatmap MAPE). |
| **🎯 Niveau** | Intermédiaire (Prévision & Diagnostic Avancé). |

### **🟧 TÂCHE 3 — Construire la Segmentation ABC/XYZ (Priorisation du Portefeuille)**

| Bloc | Détail |
| :--- | :--- |
| **❗ Problème** | Impossibilité de consacrer du temps de planning à chaque SKU. Nécessité de prioriser les 500 SKUs selon la valeur (CA), la volatilité et la criticité. |
| **📁 Fichiers** | `retail_sales_18months.csv`, `retail_products_master.csv` |
| **🧠 Analyse Attendue** | Classification ABC (CA), XYZ (Volatilité), Segmentation croisée (9 familles ABC/XYZ). Élaboration de **politiques de prévision différenciées** par segment. |
| **🛠️ Outils** | Excel (Classification automatique), Python (Pandas, Variances), Power BI (Scatter Plot). |
| **🎯 Niveau** | Intermédiaire–Avancé (Segmentation Stratégique). |

---

## **II. OPTIMISATION DES STOCKS ET DES RISQUES (TÂCHES 4-5)**

### **🟥 TÂCHE 4 — Détection des Ruptures et Analyse des Causes (Stockout RCA)**

| Bloc | Détail |
| :--- | :--- |
| **❗ Problème** | Les ruptures fréquentes impactent ventes, image client et coûts. La direction veut comprendre les causes racines : mauvaise prévision ? Lead time variable ? Erreurs de livraison ? |
| **📁 Fichiers** | `retail_stock_levels_18months.csv`, `retail_sales_18months.csv`, `retail_supplier_leadtime.csv` |
| **🧠 Analyse Attendue** | Détection des jours de rupture, calcul des **"lost sales"**, corrélation Ruptures ↔ Retards Fournisseurs. Construction d'un Rapport RCA (Root Cause Analysis) chiffré. |
| **🛠️ Outils** | Power BI (Indicateurs visuels, Correlation Chart), Python (Merge, Mask, Heatmaps). |
| **🎯 Niveau** | Avancé (Analyse de causes profondes). |

### **🟪 TÂCHE 5 — Calculer Safety Stock & Reorder Point (Dimensionnement des Stocks)**

| Bloc | Détail |
| :--- | :--- |
| **❗ Problème** | Trop d'overstocks (coûts élevés) et trop de ruptures (ventes perdues). Nécessité de dimensionner des niveaux de stock intelligents basés sur la variabilité de la demande, du *lead time* et du niveau de service cible. |
| **📁 Fichiers** | `retail_sales_18months.csv`, `retail_supplier_leadtime.csv` |
| **🧠 Analyse Attendue** | Calcul scientifique du **Safety Stock** et du **ROP** (Reorder Point). Comparaison SS recommandé vs SS actuel et hiérarchisation des produits critiques. |
| **🛠️ Outils** | Excel (Modèle complet de stock), Python (Calcul distribué pour 500 SKUs), Power BI (Vue interactive SS vs Demand). |
| **🎯 Niveau** | Avancé (Science du stock + Optimisation). |

---

## **III. SIMULATION ET OPTIMISATION AVANCÉE (TÂCHES 6-8)**

### **🟦 TÂCHE 6 — Simulation 90 Jours (Projection Stock vs Demande)**

| Bloc | Détail |
| :--- | :--- |
| **❗ Problème** | La direction demande l'évaluation du risque de rupture, de surstock et d'obsolescence sur les 3 prochains mois. |
| **📁 Fichiers** | `retail_sales_18months.csv`, `retail_stock_levels_18months.csv` |
| **🧠 Analyse Attendue** | Projection (Prophet/modèle naïf), simulation jour par jour du stock, détection future des ruptures et des overstocks. Analyse par magasin / catégorie. |
| **🛠️ Outils** | Python (Simulation boucle jour par jour), Excel (Modèle projection 90 jours), Power BI (Visualisation interactive). |
| **🎯 Niveau** | Expert (Projection dynamique). |

### **🟧 TÂCHE 7 — Optimisation de l’Allocation en Cas de Pénurie (Solver)**

| Bloc | Détail |
| :--- | :--- |
| **❗ Problème** | Un fournisseur critique annonce une réduction de livraison (seulement 60 % livrés). Il faut allouer la quantité disponible aux magasins pour maximiser le CA, le service ou répartir équitablement. |
| **📁 Fichiers** | `retail_sales_18months.csv`, `retail_stores_master.csv` |
| **🧠 Analyse Attendue** | Modélisation de l'équation d’objectif, intégration des contraintes (minimum par magasin), optimisation via solver. |
| **🛠️ Outils** | Excel Solver, Python OR-Tools / PuLP. |
| **🎯 Niveau** | Expert (Optimisation mathématique). |

### **🟥 TÂCHE 8 — Construction d’un Dashboard Executive (S&OP / Direction Supply Chain)**

| Bloc | Détail |
| :--- | :--- |
| **❗ Problème** | La direction n’a aucune vue consolidée sur la supply chain (précision prévisionnelle, volume de stocks, ruptures, risques futurs). |
| **📁 Fichiers** | Tous les fichiers du *business case*. |
| **🧠 Analyse Attendue** | Architecture du modèle (star schema), construction d’un **dashboard multi-page complet** (KPIs clés, Scénarios S&OP, Vue risques : ruptures & overstocks). |
| **🛠️ Outils** | Power BI (recommandé), Excel Power Pivot, Python (preprocessing). |
| **🎯 Niveau** | Expert + Présentation Exécutive (VP Supply Chain). |
