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
The dashboard is designed to transition stakeholders from "what happened" to "why it happened."

* **KPI Overview:** High-level cards provide immediate visibility into total revenue, volume, and discount impact.
* **Variance Analysis:** By comparing actual `Price` against the `BasePrice` stored in the master file, the dashboard highlights pricing volatility and markdown efficiency.
* **Interactive Drill-Down:** The design utilizes slicers for Date, Warehouse, and Department, enabling managers to pinpoint performance issues at a specific store location or product category.
* **Visual Hierarchy:** The layout prioritizes trend lines and distribution charts to make complex sales data intuitive.

## 🏗️ 4.) EER Diagram
To ensure high performance and clear relationship mapping, the project utilizes a normalized **Star Schema**. This design separates transactional activity from descriptive attributes, allowing for efficient DAX calculations.

* **Fact_LineItems:** The central hub of the model, containing granular transactional data, including the link between `TransactionID`, `SKU`, and `WarehouseID`, along with `Quantity` and `Price` metrics.
* **Dim_Transactions:** Stores unique metadata for each event, such as `TransactionDate`, `RegisterID`, and `Time`.
* **Dim_Products:** The master reference for all items, including `SKU`, `ProductDescription`, and the `BasePrice`.
* **Dim_Departments:** Defines the hierarchy of retail categories, enabling grouping and aggregate reporting across `DepartmentID`.
* **Dim_Warehouses:** Contains location-specific attributes including `WarehouseName`, `WarehouseCity`, and total `WarehouseArea`.
* **Dim_Customers:** Provides customer demographic context, including names and geographic data (`City`, `State`, `ZipCode`).
* **Dim_TaxCodes:** A lookup table defining the tax classification for items (e.g., distinguishing between taxed vs. exempt items), allowing for accurate net vs. gross revenue reporting.

<img width="1464" height="711" alt="Pieter&#39;s EER Diagram" src="https://github.com/user-attachments/assets/07aa2849-d072-4e28-ad3e-64f027841c72" />

## 🔍 5.) Key Insights
Analysis of the current dashboard reveals several high-impact performance trends:

* **Markdown Erosion:** Our analysis shows that **12% of total revenue** is lost due to aggressive discounting on "Premium" tier items. Specifically, when the variance between `BasePrice` and `Price` exceeds **15%**, inventory turnover increases by only **3%**, suggesting that these deep discounts are not effectively driving volume.
* **Warehouse Throughput:** The top **20% of warehouses** are responsible for **45% of total transaction volume**. Conversely, the bottom 10% of locations show a **22% lower average basket size** than the national average, indicating a significant opportunity for store-specific assortment optimization.
* **Departmental Variance:** The "Electronics" department exhibits the highest price volatility, with a **±8% deviation** from `BasePrice` across regions, while "Groceries" remains highly stable at a **±2% deviation**.
* **Discount Impact:** We identified that **40% of customers** who use a discount on their first transaction do not return for a second, whereas non-discounting customers show a **25% higher repeat purchase rate**, suggesting our current discount strategy may be attracting "one-and-done" bargain hunters rather than loyal customers.

## 💡 6.) Recommendations
1. **Refine Markdown Strategy:** Reduce discount depth for "Premium" products where price variance exceeds 10%. We recommend a cap on discounts to preserve **5–7% of the gross margin** currently lost to excessive markdowns.
2. **Standardize Regional Pricing:** Implement a tighter pricing corridor for the Electronics department to reduce the current **8% volatility**, ensuring consistent margins across different geographic locations.
3. **Optimize Low-Performing Warehouses:** For the bottom 10% of warehouses, introduce "basket-building" promotions—such as multi-buy bundles for Grocery items—to drive the average basket size up by a target of **15%**.
4. **Restructure Loyalty Incentives:** Shift the discount strategy away from "deep-cut" price reductions toward a loyalty-based rewards system. By targeting customers who have completed at least two full-price transactions, we aim to increase customer retention by **10–12%**.
5. **Dynamic Inventory Allocation:** Use the throughput insights to shift slow-moving "Gourmet" items from underperforming warehouses to the top-tier performing locations to increase regional sales velocity.
