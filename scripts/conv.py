import pandas as pd

def hex_to_rgb(hex_string):
    hex_string = hex_string.lstrip("#")
    return tuple(int(hex_string[i:i + 2], 16) for i in (0, 2, 4))

input_csv = 'colornames.csv'
df = pd.read_csv(input_csv)

df['R'] = None
df['G'] = None
df['B'] = None

# Convert and populate RGB values
for i, row in df.iterrows():
    hex_value = row['hex']
    rgb_value = hex_to_rgb(hex_value)
    df.at[i, 'R'], df.at[i, 'G'], df.at[i, 'B'] = rgb_value

df.to_csv(input_csv, index=False)

print(f"RGB values have been added to {input_csv}")
