import pandas as pd

r = [{'camp': '1', 'conversion': 10, 'hour': 1, 'spend': 100},
 {'camp': '1', 'conversion': 10, 'hour': 2, 'spend': 100},
 {'camp': '1', 'conversion': 10, 'hour': 3, 'spend': 15},
 {'camp': '1', 'conversion': 10, 'hour': 4, 'spend': 20},
 {'camp': '1', 'conversion': 10, 'hour': 5, 'spend': 10},
 {'camp': '2', 'conversion': 20, 'hour': 1, 'spend': 6},
 {'camp': '2', 'conversion': 20, 'hour': 2, 'spend': 151},
 {'camp': '2', 'conversion': 20, 'hour': 3, 'spend': 6},
 {'camp': '2', 'conversion': 20, 'hour': 4, 'spend': 15},
 {'camp': '2', 'conversion': 100, 'hour': 5, 'spend': 10},
 {'camp': '3', 'conversion': 50, 'hour': 1, 'spend': 1},
 {'camp': '3', 'conversion': 50, 'hour': 2, 'spend': 15},
 {'camp': '3', 'conversion': 50, 'hour': 3, 'spend': 100},
 {'camp': '3', 'conversion': 50, 'hour': 4, 'spend': 15},
 {'camp': '3', 'conversion': 150, 'hour': 5, 'spend': 6}]


df = pd.DataFrame(r)
total_spend = df.spend.sum()

camp_df = df.groupby('camp').agg({"conversion":sum, "spend":sum}).reset_index()

camp_df['convspend_ratio'] = camp_df.conversion / camp_df.spend

camp_df['pct_spend_to_allocate'] = camp_df.convspend_ratio / sum(camp_df.convspend_ratio) * 100

camp_df['spend_allocation'] = total_spend * (camp_df.pct_spend_to_allocate/100)

print(camp_df)