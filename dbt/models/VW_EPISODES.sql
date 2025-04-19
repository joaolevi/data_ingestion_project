WITH name_basics AS (
  SELECT
    nconst,
    "primaryName",
    "birthYear",
    "deathYear",
    "primaryProfession",
    "knownForTitles"
  FROM {{source('imdb', 'TB_NAME_BASICS')}}
  WHERE "primaryName" IS NOT NULL 
),

title_basics AS (
  SELECT 
    tconst,
    "titleType",
    "primaryTitle",
    "originalTitle",
    CASE 
      WHEN "isAdult" IS NOT NULL AND "isAdult" = 1 THEN 1
      WHEN "isAdult" is not null and "isAdult" = 0 then 0
      else null
    end as "isAdult",
    "startYear",
    "runtimeMinutes",
    "genres"
  FROM {{source('imdb', 'TB_TITLE_BASICS')}}
),

title_principals AS (
  SELECT 
    tconst,
    nconst,
    "category",
    "job",
    "characters"
  FROM {{source('imdb', 'TB_TITLE_PRINCIPALS')}}
),

title_ratings AS (
  SELECT 
    tconst,
    "averageRating",
    "numVotes"
  FROM {{source('imdb', 'TB_TITLE_RATINGS')}}
),

title_episodes AS (
  SELECT 
    tconst,
    "parentTconst",
    "seasonNumber",
    "episodeNumber"
  FROM {{source('imdb', 'TB_TITLE_EPISODE')}}
)

SELECT 
  tp."tconst",
  tp."nconst",
  n."primaryName",
  n."birthYear",
  n."deathYear",
  n."primaryProfession",
  n."knownForTitles",
  tb."titleType",
  tb."primaryTitle",
  tb."originalTitle",
  tb."isAdult",
  tb."startYear",
  tb."runtimeMinutes",
  tb."genres",
  tr."averageRating",
  tr."numVotes",
  te."parentTconst",
  te."seasonNumber",
  te."episodeNumber",
  case tp."category"
    when '\N' then null
    else tp."category"
  end as "category",
    case tp."job"
        when '\N' then null
        else tp."job"
    end as "job",
  case tp."characters"
    when '\N' then null
    else tp."characters"
    end as "characters"
FROM title_principals tp
JOIN name_basics n ON tp.nconst = n.nconst
JOIN title_basics tb ON tp.tconst = tb.tconst
LEFT JOIN title_ratings tr ON tp.tconst = tr.tconst
LEFT JOIN title_episodes te ON tp.tconst = te.tconst