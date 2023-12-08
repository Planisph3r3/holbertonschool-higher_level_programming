-- Listing all records based on score but excluding those that have an emply name value.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;