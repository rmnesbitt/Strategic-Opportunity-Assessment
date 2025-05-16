import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)

# Define customer segments and number of samples per segment
segments = ['Tech Startups', 'Healthcare Providers', 'Marketing Agencies', 'Law Firms', 'Non-Profits']
n_rows_per_segment = 200000  # Total 1,000,000 rows

# Storage list
data = []

# Segment-specific distribution assumptions
distributions = {
    'Tech Startups': {
        'avg_revenue': (12000, 3000),
        'retention_rate': (0.65, 0.1),
        'expansion_base': 0.25,
        'cost_to_serve': (2500, 500),
        'strategic_fit': (0.75, 0.1)
    },
    'Healthcare Providers': {
        'avg_revenue': (18000, 4000),
        'retention_rate': (0.78, 0.08),
        'expansion_base': 0.3,
        'cost_to_serve': (3000, 600),
        'strategic_fit': (0.85, 0.08)
    },
    'Marketing Agencies': {
        'avg_revenue': (10000, 2500),
        'retention_rate': (0.60, 0.12),
        'expansion_base': 0.2,
        'cost_to_serve': (2200, 400),
        'strategic_fit': (0.65, 0.1)
    },
    'Law Firms': {
        'avg_revenue': (22000, 5000),
        'retention_rate': (0.82, 0.07),
        'expansion_base': 0.35,
        'cost_to_serve': (2800, 550),
        'strategic_fit': (0.80, 0.09)
    },
    'Non-Profits': {
        'avg_revenue': (8000, 1500),
        'retention_rate': (0.55, 0.1),
        'expansion_base': 0.15,
        'cost_to_serve': (1800, 300),
        'strategic_fit': (0.70, 0.1)
    }
}

# Generate the data
for segment in segments:
    d = distributions[segment]
    for _ in range(n_rows_per_segment):
        revenue = max(np.random.normal(d['avg_revenue'][0], d['avg_revenue'][1]), 0)
        retention = np.clip(np.random.normal(d['retention_rate'][0], d['retention_rate'][1]), 0, 1)
        expansion = np.random.uniform(0.1, 0.6) + d['expansion_base']
        cost = max(np.random.normal(d['cost_to_serve'][0], d['cost_to_serve'][1]), 500)
        fit = np.clip(np.random.normal(d['strategic_fit'][0], d['strategic_fit'][1]), 0, 1)

        data.append({
            'Segment': segment,
            'AvgRevenue': round(revenue, 2),
            'RetentionRate': round(retention, 3),
            'ExpansionPotential': round(expansion, 3),
            'CostToServe': round(cost, 2),
            'StrategicFit': round(fit, 3)
        })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("../data/enterprise_saas_segment_data.csv", index=False)
print("CSV Saved")