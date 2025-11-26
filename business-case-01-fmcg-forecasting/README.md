**FMCG Multi-Country Sales Dataset (1.1M Rows)
Advanced Business Case : Demand Planning, Forecasting & FMCG Analytics**

🔗 **Dataset Kaggle :** https://www.kaggle.com/datasets/robertocarlost/fmcg-multi-country-sales-dataset

📁 **GitHub Repository (Business Cases SCM & Demand Planning)**  
https://github.com/Carlos25-afq/business-cases-scm-demand-planning


🧩 1. **Overview**

This dataset contains more than 1,100,000 rows of highly realistic FMCG sales data generated for professional demand planning, forecasting, and supply chain analytics.

It simulates a multi-country FMCG environment, with:

- 350+ SKUs

- 3 full years of daily sales

- 15 countries, 60+ cities (with real lat/lon coordinates)

- Multiple sales channels (Modern Trade, Traditional Trade, Wholesale, E-commerce)

- Promotional effects & price elasticity

- Seasonality patterns (weekly, monthly, yearly)

- ABC/XYZ segmentation

- Lead time variability

- Stockouts & safety stock parameters

This dataset is designed for real-life business cases, job interviews, portfolio projects, coursework, and professional S&OP simulations.

## 🎯 1. Objective of the Business Case

This business case simulates a **real FMCG company operating across 15 countries**,  
with **350+ SKUs**, **1,000,000+ daily sales records**, and **multi-channel distribution**.

The goal is to demonstrate **end-to-end demand forecasting capabilities**:

- Deep exploratory analysis  
- ABC/XYZ segmentation  
- Seasonality detection (MoY, DoW, holidays)  
- Promo uplift analysis  
- Baseline vs uplift separation  
- Time-series modelling  
- Holt-Winters & advanced forecasting  
- S&OP decision-making  
- Impact on safety stock & service levels  

This project reflects the **exact expectations** of real roles:  
**Demand Planner, S&OP Analyst, Supply Chain Data Analyst, Forecasting Specialist.**

---

## 📊 2. Dataset Overview

The dataset contains **over 1 million FMCG transactions** generated to replicate realistic business constraints:

### **Key dataset features**
| Feature | Description |
|--------|-------------|
| `date` | Daily sales over 3 years |
| `country` | 15 African, European & LATAM countries |
| `city` | Real cities + latitude & longitude |
| `sku_id` | 350+ unique SKUs with hierarchy |
| `category` | 4 main FMCG categories |
| `units_sold` | Daily volume (baseline + noise + promotions) |
| `unit_price` | Category-consistent prices |
| `channel` | Traditional trade, Modern trade, E-commerce |
| `is_promo` | Promo flag with uplift modelling |
| `competitor_price` | Price competition pressure |
| `weather_temp` | Contextual exogenous variable |
| `stockout_flag` | Days with zero availability |

---

## 🧠 3. Business questions answered in this case

### ✔ 1. **Which SKUs drive the most revenue?** (ABC)
### ✔ 2. **How predictable is the demand?** (XYZ)
### ✔ 3. **How strong is seasonality per country/channel?**
### ✔ 4. **What is the real promo uplift?**  
### ✔ 5. **How to build a baseline vs promo forecast?**
### ✔ 6. **Which forecasting model performs best?**
### ✔ 7. **How does forecast accuracy impact safety stock?**
### ✔ 8. **What are the prioritisation rules for S&OP?**

---

## 📘 4. What’s inside

The notebook contains **15 fully structured sections**, including:

1. Data loading  
2. Data cleaning & preprocessing  
3. Missing values strategy  
4. Time-series consistency checks  
5. Exploratory analysis  
6. ABC/XYZ segmentation  
7. Seasonality & calendar analysis  
8. Promo uplift detection  
9. Demand decomposition  
10. Baseline modelling  
11. Holt-Winters modelling  
12. Forecast evaluation (MAPE, MAD, RMSE)  
13. Impact analysis for S&OP  
14. Safety stock scenario  
15. Business recommendations  

🏢 2. Business Case Context

A multinational FMCG company faces complex challenges across multiple regions:

🚩 Key Challenges

- High demand volatility

- Frequent promotions impacting baselines

- Low forecast accuracy

- Non-optimized safety stock levels

- Stockouts on A-products and overstocks on C-products

- Large discrepancies in country-level performance

- Lack of integrated S&OP visibility

🎯 Core Objective

Build a robust data-driven demand planning framework to:

- Improve forecast accuracy

- Reduce stockouts and overstocks

- Model promotional uplift

- Optimise safety stock / service levels

- Support S&OP decision-making

- Understand market dynamics by SKU, country, and channel

- Build executive dashboards for supply chain leaders

This business case fully reflects real responsibilities of a
Demand Planner, S&OP Analyst, or Supply Chain Data Analyst.

📊 3. Dataset Schema
| Column | Description | Domain |
| :--- | :--- | :--- |
| `date` | Daily timestamp (3 years continuous) | **Time** |
| `sku` | Product identifier (350+ SKUs) | **Product** |
| `category` | FMCG category (Beverages, Snacks, Home Care…) | **Product** |
| `country` | 15 countries | **Geography** |
| `city` | 60+ cities | **Geography** |
| `latitude, longitude` | Real geographic coordinates | **Geography** |
| `channel` | MT, TT, Wholesale, E-commerce | **Distribution** |
| `units_sold` | Daily units sold (realistic distributions) | **Sales/Demand** |
| `list_price` | Base price | **Pricing** |
| `promo_flag` | 1 during promotions | **Promotion** |
| `promo_discount` | Percentage discount | **Promotion** |
| `promo_uplift` | Sales uplift (%) | **Promotion** |
| `stock_out_flag` | 1 if stockout occurred | **Customer Service** |
| `cost_per_unit` | Procurement cost | **Finance/Costs** |
| `transport_cost` | Transport cost per unit | **Logistics** |
| `gross_margin` | Margin computation | **Finance** |
| `safety_stock` | Recommended safety stock | **Inventory/Planning** |
| `demand_class` | A/B/C classification | **Analysis (Segmentation)** |
| `volatility_class` | X/Y/Z classification | **Analysis (Segmentation)** |
| `country_seasonality_factor` | Macro seasonality intensity | **Forecasting** |
| `lead_time_days` | Supplier lead time | **Logistics/Sourcing** |
| `supplier_id` | Supplier code | **Sourcing** |
| `currency` | Local currency | **Finance/Macro** |
| `revenue` | units_sold × list_price | **Finance** |
| `...` | Additional operational variables | **Operations** |
Dataset is delivered in CSV format, compatible with Python, R, Power BI, Tableau and Excel.

🧪 4. Training Instructions (Full Business Case)
Designed like a professional workshop — step-by-step.

🟦 *Exercise 1 : Exploratory Data Analysis (EDA)*

🎯 Objective

Understand market dynamics and identify drivers of demand.

🛠 To Do

- Total sales by country

- Top 20 SKUs by revenue

- Compare ABC classes per region

- Identify volatility (XYZ) by SKU

- Correlate price, promotions, and volume

- Visualise seasonality (monthly & weekly patterns)

🧠 Expected Business Insights

- Clear seasonality peaks (summer/winter depending on category)

- E-commerce may show higher volatility

- Some SKUs are promo-dependent

- Low-performing regions may require different safety stock policies

🟩 *Exercise 2 : Forecasting (Statistics + Machine Learning)*

🎯 Objective

Forecast 10 SKUs with different demand profiles.

🛠 Models to Build

1. Naive

2. Moving Average

3. Exponential Smoothing

4. Holt-Winters

5. SARIMA

6. Random Forest

7. XGBoost

8. Prophet

10. LSTM (optional)

📈 KPIs to Evaluate

1. MAPE

2. WAPE

3. Forecast Bias

4. Forecast Value Added (FVA)

🧠 Expected Insights

- Stable SKUs → Holt-Winters / SARIMA best

- Volatile SKUs → RF/XGBoost more robust

- Promo-heavy SKUs → ML significantly improves accuracy

- High-bias SKUs → need commercial alignment in S&OP

🟧 *Exercise 3 : Safety Stock & Service Level Simulation*

🎯 Objective

Calculate optimal safety stock and quantify service level trade-offs.

🛠 Required Calculations

1. Safety Stock = Z × σDLT × √LT

You must compute:

- Demand variability

- Lead time variability

- Target service levels (80–99%)

- Stockout risk curves

- Total landed cost impact

🧠 Expected Insights

1. Z-class SKUs → high safety stock requirement

2. Improving service level from 92% → 96% increases cost significantly

3. Countries with high lead time variability require different policies

🟥 *Exercise 4 : Promotional Analysis*

🎯 Objective

- Analyse baseline vs promo performance to measure:

- Promo uplift

- Cannibalisation

- Margin erosion

- Long-term demand effects

🛠 Techniques to Use

- Difference vs baseline curve

- Regression with discount rate as predictor

- Cross-category correlation analysis

🧠 Expected Insights

- Some SKUs lose margin despite uplift

- Strong promo elasticity can reveal stock risks

- Promotions may distort forecasting models if not isolated

🟦 *Exercise 5 : Executive Dashboard (Power BI / Tableau)*

🎯 Objective

Build an S&OP-ready dashboard.

📊 Recommended Sections

- Forecast Accuracy (MAPE/WAPE/Bias)

- Promo Uplift Analysis

- ABC/XYZ segmentation

- Revenue by Region

- Service Level Performance

- Stockouts & Overstock Heatmaps

- Lead Time Variability

- Country/City Map (lat/lon)

- This dashboard becomes a high-value portfolio asset.



📦 File Description
fmcg_sales_3years_1M_rows.csv
└── 1,100,000+ rows
└── 30+ variables
└── Multi-country FMCG dataset


🏆 6.  Why This Dataset Matters

This dataset helps you demonstrate:

✔ Real-world demand planning expertise
✔ ML forecasting applied to FMCG
✔ Understanding of volatility, promotions, seasonality
✔ Business storytelling through dashboards
✔ Capability to handle big datasets (+1M rows)
✔ Alignment with industry S&OP processes
✔ Cross-functional analytical thinking

This dataset is ideal for:

- Portfolio Projects

- Job Applications

- MSc/PhD Assignments

- Case Studies

- Kaggle Competitions

- Supply Chain Hackathons


