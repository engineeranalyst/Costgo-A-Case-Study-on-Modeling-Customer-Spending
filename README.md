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

### Customer Spending Profile
* **November Revenue Surge:** Spending remained steady through Q3, followed by a massive **Black Friday spike in November**, peaking at **$485,381.11**.
* **Transaction Peak:** While revenue peaked in November, **Transaction Counts** climbed steadily throughout the year, hitting a maximum of **1,319 in December**. This shows successful customer retention following the holiday rush.
* **Top 5 Product Departments (Net Spend):** 1. Hardlines/Electronics: **$325,104**
    2. Hardware/Tools: **$298,442**
    3. Home/Housewares: **$275,102**
    4. Specialty Foods/Gourmet: **$210,443**
    5. Media/Books: **$185,332**
* **Top 5 Hero Products (Net Spend):**
    1. HEADPHONES: **$85,221**
    2. POWER DRILL: **$72,443**
    3. COFFEE MAKER: **$68,112**
    4. TOASTER: **$55,332**
    5. BED SHEETS: **$48,119**
* **Discount Dynamics:** Only **18.4% of products** were discounted, yet **72.1% of customers** used a discount, showing that even limited promotions are a major driver for the majority of the customer base.
* **Returns & Quality:** The store maintained high satisfaction with only **1.2% of products** returned and just **4.8% of customers** initiating a return.

### Customer Spending Velocity
* **Tier Revenue Proportion:** **Standard members** contributed the largest share of revenue at **$1.87M**, followed by **Elite members** at **$1.49M** and **Bargain hunters** at **$526.0K**.
* **Spending Velocity (Scatter Plot):** The scatter plot reveals that **Elite members** maintain high net spend with minimal days between trips, while **Bargain hunters** have much longer gaps between store visits.
* **Tier Heatmap:** **Standard members** represent the most consistent foot traffic density throughout the week, while **Elite members** show concentrated clusters during specific weekend "Power Shopping" blocks.
* **Store Area Efficiency:** The column chart shows a remarkably even distribution of success across store sizes, with **Medium stores (2k-3.5k sq. ft.)** reaching an average spend of **$1.57M**, slightly outpacing Large and Small formats.

## 💡 6.) Recommendations
I propose the following recommendations for increasing revenue and profitability:

* **Optimize for Medium Footprints:** Future expansion should prioritize the **2,500–3,000 sq. ft.** warehouse size, as it matches the revenue of Large stores with lower overhead.
* **Post-Holiday Retention:** Launch a "Year 2 Continuity" campaign in late December to capitalize on the peak transaction volume (**1,319**) and keep shoppers active into Q1.
* **Tier-Specific Product Bundles:** Create exclusive bundles for the **Hardlines/Electronics** and **Hardware** departments (the top two earners) specifically targeted at **Elite members** to further reduce their already low days-between-trips.
* **Incentivize Bargain Migration:** Since **72.1% of customers** are discount-motivated, offer "Standard Tier" membership upgrades that include permanent discounts on the **Top 5 Hero Products** (like Headphones and Power Drills) to convert infrequent Bargain hunters into high-velocity shoppers.
