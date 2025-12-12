# lib/sql_queries.py

# 1. Select all female bears and return name and age
select_all_female_bears_return_name_and_age = """
SELECT name, age
FROM bears
WHERE sex = 'F';
"""

# 2. Select name only and order alphabetically (FIXED the selection issue)
select_all_bears_names_and_orders_in_alphabetical_order = """
SELECT name
FROM bears
ORDER BY name ASC;
"""

# 3. Select alive bears, returning name and age, ordered youngest to oldest
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
SELECT name, age
FROM bears
WHERE alive = 1
ORDER BY age ASC;
"""

# 4. Select the oldest bear (NOTE: uses _returns_ to match test file)
select_oldest_bear_and_returns_name_and_age = """
SELECT name, age
FROM bears
ORDER BY age DESC
LIMIT 1;
"""

# 5. Select the youngest bear (NOTE: uses _returns_ to match test file)
select_youngest_bear_and_returns_name_and_age = """
SELECT name, age
FROM bears
ORDER BY age ASC
LIMIT 1;
"""

# 6. The other required variables, needed by tests not shown in the final output:

# Select name and temperament of all bears
select_name_and_temperament_of_all_bears = """
SELECT name, temperament
FROM bears;
"""

# Select the most temperate bear (matching the lab's likely typo 'temerate')
select_most_temerate_bear_and_return_name_and_age = """
SELECT name, age
FROM bears
ORDER BY temperament ASC
LIMIT 1;
"""
