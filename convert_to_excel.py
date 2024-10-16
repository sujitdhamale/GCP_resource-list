import re
import pandas as pd

# Read the file
input_file = '/mnt/data/data.txt'
with open(input_file, 'r') as file:
    data = file.read()

# Regular expression to match blocks of asset details
asset_blocks = re.findall(r'---\n(.*?)\n---', data, re.DOTALL)

# Extract asset details into dictionaries
asset_list = []
for block in asset_blocks:
    asset_dict = {}
    lines = block.split('\n')
    for line in lines:
        if ': ' in line:
            key, value = line.split(': ', 1)
            asset_dict[key.strip()] = value.strip()
    asset_list.append(asset_dict)

# Convert to DataFrame
df = pd.DataFrame(asset_list)


# Write to Excel
output_file = '/mnt/data/asset_data.xlsx'
df.to_excel(output_file, index=False)

print(f'Data has been successfully written to {output_file}')
