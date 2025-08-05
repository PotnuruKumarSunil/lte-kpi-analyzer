# kpi_analyzer/analyzer.py

import pandas as pd
from .rule_parser import parse_kpi_rules
from .preprocessing import preprocess_data


class KPIAnalyzer:
    def __init__(self, rule_sheet_path: str):
        """
        Initialize the analyzer with the path to the master KPI sheet.
        Parses KPI formulas and (optionally) thresholds and expectations.
        """
        self.kpi_rules = parse_kpi_rules(rule_sheet_path)

    def analyze(self, input_data: pd.DataFrame) -> pd.DataFrame:
        """
        Analyzes the input KPI data against the rules parsed from the master sheet.

        Parameters:
        - input_data: DataFrame of site-wise or time-wise KPI values.

        Returns:
        - DataFrame with an additional column 'Status' indicating:
          'Improved', 'Degraded (Expected)', 'Degraded (Anomaly)', or 'Normal'
        """
        df = preprocess_data(input_data)
        df['Status'] = 'Normal'

        for kpi, rule in self.kpi_rules.items():
            if kpi not in df.columns:
                continue

            threshold = rule.get('threshold')
            direction = rule.get('direction')
            expected = rule.get('expected')

            for index, value in df[kpi].items():
                if threshold is None or direction is None:
                    continue

                if direction == 'decrease' and value < threshold:
                    df.at[index, 'Status'] = 'Degraded (Expected)' if expected else 'Degraded (Anomaly)'
                elif direction == 'increase' and value > threshold:
                    df.at[index, 'Status'] = 'Improved'

        return df

