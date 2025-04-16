-- models/basic_info.sql

SELECT
  primaryName,
  birthYear,
  deathYear
FROM name_basics
WHERE birthYear IS NOT NULL;
