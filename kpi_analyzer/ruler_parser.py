# kpi_analyzer/rule_parser.py

import pandas as pd

def parse_kpi_rules(excel_path: str, sheet_name: str = "Sheet1") -> dict:
    """
    Parses the master KPI sheet and extracts KPI formulas.
    
    Returns a dictionary like:
    {
        'Payload-DL (GB)': {
            'formula': 'PdcpDLBytesConsumed/(1024*1024*1024)',
            'threshold': None,
            'direction': None,
            'expected': None
        },
        ...
    }
    """
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    rule_map = {}

    for _, row in df.iterrows():
        kpi_name = str(row['KPI Name']).strip()
        formula = str(row['VIL Formula']).strip()

        rule_map[kpi_name] = {
            'formula': formula,
            'threshold': None,     # You can enhance this by adding columns in Excel
            'direction': None,     # 'increase' or 'decrease'
            'expected': None       # True or False
        }

    return rule_map

