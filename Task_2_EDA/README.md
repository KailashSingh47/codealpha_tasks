# Task 2 - Exploratory Data Analysis

## Objective
Perform Exploratory Data Analysis (EDA) on the books dataset collected during Task 1.

## Dataset
The dataset contains 100 books with the following columns:
- Title
- Price
- Rating
- Availability
- Product_URL

## Analysis Performed
- Dataset structure and dimensions
- Data types
- Missing value analysis
- Duplicate record detection
- Statistical summary
- Price distribution
- Rating distribution
- Availability analysis
- Price outlier detection using IQR
- Price and rating correlation analysis
- Identification of cheapest and most expensive books

## Key Findings
- Dataset contains 100 records and 5 variables.
- No missing values were found.
- No duplicate records were found.
- All 100 books were listed as in stock.
- Average book price: 34.56
- Median book price: 34.78
- Price range: 10.16 to 58.11
- No price outliers were detected using the IQR method.
- Pearson correlation between price and rating was approximately -0.122.
- The correlation was not statistically significant at the 5% significance level.

## Visualizations
The following charts are included in the screenshots folder:
- Price Distribution
- Rating Distribution
- Price by Rating
- Availability
- Correlation Heatmap
- Price Outliers

## Tools and Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

## Files
- eda.py - EDA Python script
- ooks_dataset.csv - Dataset
- eda_report.txt - Analysis report
- screenshots/ - Generated visualizations
- equirements.txt - Required Python libraries
