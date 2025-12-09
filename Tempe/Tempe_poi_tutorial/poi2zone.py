import pandas as pd
import os

# Read original file
df_original = pd.read_csv('poi_park.csv')

# Create new dataframe with transformations
df = df_original.copy()
df['old_poi_id'] = df['poi_id']
df['zone_id'] = range(1, len(df) + 1)
df['node_id'] = df['zone_id']
df['boundary_geometry'] = df['geometry']
df['geometry'] = df['centroid']

# Extract x_coord, y_coord from centroid (POINT format)
coords = df['centroid'].str.extract(r'POINT\s*\(([^ ]+) ([^ ]+)\)')
df['x_coord'] = coords[0].astype(float)
df['y_coord'] = coords[1].astype(float)

# Select columns for output
output_cols = ['zone_id', 'node_id', 'old_poi_id', 'osm_way_id', 'osm_relation_id', 
               'building', 'amenity', 'leisure', 'way', 
               'boundary_geometry', 'geometry', 'x_coord', 'y_coord']

# Save to zone.csv
df[output_cols].to_csv('zone.csv', index=False)

print(f"Converted {len(df)} records from poi_park.csv to zone.csv")