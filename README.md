# 🛒 Costco Invoice Analytics: End-to-End Data Engineering & Visualization

* A comprehensive study in building a robust, production-grade data pipeline from synthetic generation to high-level executive visualization.
* This project demonstrates the full lifecycle of data—from designing a schema to deriving actionable business intelligence.

## 📝 1.) Executive Summary 📈
This project serves as a comprehensive simulation of a high-volume retail transactional environment. By utilizing Python’s `Faker` library, I generated a large-scale, relational dataset that mirrors real-world retail operations, including SKU-specific pricing, regional warehouse distributions, and customer behavioral patterns.

**Disclaimer:** All data contained within this project, including customer names, addresses, and transaction history, is **100% synthetic**. It was generated using the Python `Faker` library for the sole purpose of demonstrating data engineering, modeling, and dashboarding capabilities. No real individual or corporate entity data is involved.

## 💻 2.) Python Code Methodology ⚙️
To ensure scalability and modularity, I designed a specialized `CleanData` class using an Object-Oriented approach. This framework employs a **Strategy Pattern**, allowing for the "injection" of custom cleaning and simulation logic into the workflow.

* **Modular Architecture:** The `CleanData` class encapsulates file path management and environment detection (Cloud vs. Local), ensuring the pipeline is portable.
* **The Simulation Engine (`cleaning_fun`):**
    * **Master Pricing Logic:** Instead of broad department-level pricing, I implemented an **Item-Level Master Price File** using a dictionary to map specific min/max constraints to every SKU.
    * **Stochastic Noise:** I utilized `random.uniform(-2.00, 2.00)` to inject controlled variance into prices, ensuring data remains realistic yet audit-ready.
    * **Normalization:** The engine handles the construction of primary fact records, joining customer, warehouse, and product dimensions in real-time, resulting in a ready-to-consume CSV format.

## 📊 3.) Power BI Dashboard Methodology 🖼️
The dashboard is designed to transition stakeholders from "what happened" to "why it happened."

* **KPI Overview:** High-level cards provide immediate visibility into total revenue, volume, and discount impact.
* **Variance Analysis:** By comparing actual `Price` against the `BasePrice` stored in the master file, the dashboard highlights pricing volatility and markdown efficiency.
* **Interactive Drill-Down:** The design utilizes slicers for Date, Warehouse, and Department, enabling managers to pinpoint performance issues at a specific store location or product category.
* **Visual Hierarchy:** The layout prioritizes trend lines and distribution charts to make complex sales data intuitive.

## 🏗️ 4.) The Data Model 📐
To ensure high performance and clear relationship mapping, the project utilizes a normalized **Star Schema**. This design separates transactional activity from descriptive attributes, allowing for efficient DAX calculations.

* **Fact_LineItems:** The central hub of the model, containing granular transactional data, including the link between `TransactionID`, `SKU`, and `WarehouseID`, along with `Quantity` and `Price` metrics.
* **Dim_Transactions:** Stores unique metadata for each event, such as `TransactionDate`, `RegisterID`, and `Time`.
* **Dim_Products:** The master reference for all items, including `SKU`, `ProductDescription`, and the `BasePrice`.
* **Dim_Departments:** Defines the hierarchy of retail categories, enabling grouping and aggregate reporting across `DepartmentID`.
* **Dim_Warehouses:** Contains location-specific attributes including `WarehouseName`, `WarehouseCity`, and total `WarehouseArea`.
* **Dim_Customers:** Provides customer demographic context, including names and geographic data (`City`, `State`, `ZipCode`).
* **Dim_TaxCodes:** A lookup table defining the tax classification for items (e.g., distinguishing between taxed vs. exempt items), allowing for accurate net vs. gross revenue reporting.

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
