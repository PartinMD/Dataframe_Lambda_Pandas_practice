import pandas as pd #type: ignore

# Import data as a dataframe
inventory = pd.read_csv('inventory.csv')
# print(inventory.head(10))

# Save the first 10 indices to Staten Island
staten_island = inventory[0:10]

# Products available at Staten Island location
product_request = staten_island.product_description

# Seeds sold in Brooklyn location
seed_request = inventory[(inventory.location == 'Brooklyn') & (
    inventory.product_type == 'seeds')]

# Add in_stock column to inventory dataframe
inventory['in_stock'] = inventory.apply(
    lambda row: True if row.quantity > 0 else False, axis=1)
# print(inventory.head(10)) # Displays the newly added "in_stock" column

# Add total_value column to inventory dataframe
inventory['total_value'] = inventory.apply(
    lambda row: row.price * row.quantity, axis=1)
# print(inventory.head(10)) # Displays the newly added "total_value" column

# Combine the product_type and product_description columns into a single string and insert into a new column full_description


def combine_lambda(row): return \
    '{} - {}'.format(row.product_type,
                     row.product_description)


inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
print(inventory.head(10))  # Displays the newly added "full_description" column
print(inventory)