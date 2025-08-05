from kpi_analyzer.analyzer import KPIAnalyzer
import pandas as pd

model = KPIAnalyzer("data/KPIs Master Sheet.xlsx")

# Replace with actual or sample data path
df = pd.read_csv("data/sample_field_data.csv")
result = model.analyze(df)

print(result[['Status']])

