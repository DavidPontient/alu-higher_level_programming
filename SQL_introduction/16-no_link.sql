-- list all record in the database table but not rows without a name value
SELECT score, name FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;
