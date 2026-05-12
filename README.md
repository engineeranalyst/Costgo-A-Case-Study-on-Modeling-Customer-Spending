# 🛒 Costco : A Case Study on Modeling Customer Spending

<img width="1428" height="782" alt="Customer Spending Profile" src="https://github.com/user-attachments/assets/67659e14-0ad3-4ad2-9c89-82a0ac6d58b0" />

<img width="1422" height="565" alt="Customer Spending Velocity" src="https://github.com/user-attachments/assets/858a302d-b4a2-419a-9bb8-c077fe0a6d58" />

## 📝 1.) Executive Summary
This project simulates a "Grand Opening" scenario for a major retail expansion, focusing on the first year of transactional data across multiple warehouse sizes and geographic locations. The primary objective was to build a robust, scalable ETL pipeline and a dual-dashboard suite to monitor **Customer Spending Velocity** and **Tiered Behavioral Profiles**. By integrating Python-driven data generation with SQL-based relational modeling, this project provides a high-fidelity look at how a new market reacts to a major retail entry.

> **Disclaimer:** All data utilized in this project was synthetically generated using the Python Faker library to simulate a realistic retail environment for educational and portfolio purposes. No actual company data, proprietary records, or real-world transactions were used.

## 💻 2.) Python Code Methodology
The foundation of this project is a scalable data generation and transformation engine designed to move beyond simple "random" data into "structured realism."

### Data Generation Engine
I utilized the `Faker` library integrated with custom business logic to ensure the dataset behaved like a real-world economy:
* **Temporal Scaling:** Transactions were weighted to increase month-over-month, simulating the 12-month brand awareness ramp-up typical of a new location.
* **Behavioral Constraints:** I implemented a **2.8% Stable Success** logic for discounts. This ensured that different tiers reacted differently to promotions (e.g., Bargain hunters showing 8.2% sensitivity vs. Elite members at 0.7%).

### The `CleanData` Class & `cleaning_fun`
To ensure code reusability and professional architecture, I developed a modular transformation pipeline:
* **`CleanData` Class:** Acts as a central orchestrator for state management, ensuring every data transformation is idempotent and repeatable.
* **`cleaning_fun` Methodology:** This function executes a multi-stage "Flattening" of raw records:
    1.  **Normalization:** Converting raw CSV strings into standardized numeric and datetime formats.
    2.  **Constraint Enforcement:** Filtering out illogical data points and applying tax code mappings.
    3.  **Tier Logic Integration:** Dynamically assigning customers to tiers based on their simulated spending patterns, which feeds the primary dimensions of the EER diagram.

## 📊 3.) Power BI Dashboard Methodology
The visualization layer was designed using **Mode 33** strategic principles, focusing on high-level KPIs and granular operational efficiency.

### Customer Spending Profile
* **Objective:** Identify the "Who" behind the revenue.
* **Design:** I utilized **Clustered Bar Charts** to compare Gross vs. Net spend across tiers. 
* **Key Feature:** Implementation of a spending cluster visual to identify "Whales" (Elite) vs. "Bargain" hunters, allowing for a clear view of margin impact.

### Customer Spending Velocity
* **Objective:** Identify "Where" and "When" value is created.
* **Binning Logic:** Using Power Query, I created **Warehouse Area Bins** (Small, Medium, Large) to categorize 1,000+ simulated locations.
* **Design:** The centerpiece is a **Stacked Clustered Column Graph** displaying total spend across store sizes, stacked by customer tier. This highlights the "Brand over Building" effect—proving that new stores hit performance targets regardless of physical footprint in Year 1.

## 🏗️ 4.) EER Diagram
The project utilizes a highly normalized **Star Schema** to ensure high-performance DAX calculations and data integrity.

1.  **Dim_Customers:** Contains unique member IDs, names, and geographic data (Virginia Beach focus).
2.  **Dim_Sales:** A bridge table containing transaction-level metadata (Time, RegisterID).
3.  **Dim_CustomerTiers:** Definitive mapping for BARGAIN, STANDARD, and ELITE logic.
4.  **Dim_Warehouses:** Physical attributes, specifically the `WarehouseArea` used for efficiency metrics.
5.  **Dim_TaxCodes:** Maps internal SKU codes to state-specific tax obligations.
6.  **Dim_Products:** Detailed SKU level descriptions and base pricing.
7.  **Dim_Departments:** Hierarchical grouping (e.g., Grocery, Electronics, Automotive).
8.  **Dim_Returns:** Categorization of return reasons (Defective, Change of Mind).
9.  **Fact_Sales:** The central "Truth" table containing quantities, prices, and discount amounts.
10. **Fact_Returns:** Tracks negative revenue events linked back to the original sales records.

<img width="1604" height="726" alt="Pieter&#39;s EER Diagram" src="https://github.com/user-attachments/assets/9866d023-0af7-4b79-8613-b615c02b1544" />

## 🔍 5.) Key Insights
The following insights were derived directly from the finalized Power BI dashboards:

* **The "Medium" Dominance:** The **Medium (2k-3.5k sq. ft.)** stores are currently the highest earners, generating **$535,105** in Net Spend, outperforming the "Large" flagship stores.
* **Stable Success Metric:** The total Discount Leakage settled at **2.74%**, which is the ideal target for a healthy, profitable new market entry.
* **Bargain Sensitivity:** **Bargain** hunters account for **8.2%** of all discount leakage, confirming they are the primary drivers of promotional volume while **Elite** members maintain a low **0.72%** leakage.
* **Growth Velocity:** The region successfully ramped from negligible transactions in January to a peak of **1,510 transactions in January of Year 2**, showing a successful "Grand Opening" adoption curve.

## 💡 6.) Recommendations
1. **Refine Markdown Strategy:** Reduce discount depth for "Premium" products where price variance exceeds 10%. We recommend a cap on discounts to preserve **5–7% of the gross margin** currently lost to excessive markdowns.
2. **Standardize Regional Pricing:** Implement a tighter pricing corridor for the Electronics department to reduce the current **8% volatility**, ensuring consistent margins across different geographic locations.
3. **Optimize Low-Performing Warehouses:** For the bottom 10% of warehouses, introduce "basket-building" promotions—such as multi-buy bundles for Grocery items—to drive the average basket size up by a target of **15%**.
4. **Restructure Loyalty Incentives:** Shift the discount strategy away from "deep-cut" price reductions toward a loyalty-based rewards system. By targeting customers who have completed at least two full-price transactions, we aim to increase customer retention by **10–12%**.
5. **Dynamic Inventory Allocation:** Use the throughput insights to shift slow-moving "Gourmet" items from underperforming warehouses to the top-tier performing locations to increase regional sales velocity.
