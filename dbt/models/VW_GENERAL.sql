with name_basics as (
  select *,
  first_value("primaryName") over (partition by nconst order by "birthYear"
  rows between unbounded preceding and unbounded following) as "first_primaryName"
  from {{source('imdb', 'TB_NAME_BASICS')}}
  where "primaryName" is not null
),
title_basics as (
  select *,
  first_value("primaryTitle") over (partition by tconst order by "startYear"
  rows between unbounded preceding and unbounded following) as "first_primaryTitle"
  from {{source('imdb', 'TB_TITLE_BASICS')}}
  where "primaryTitle" is not null
)

select
  b.tconst,
  a.nconst,
  a."first_primaryName",  -- Alterado para o novo nome
  a."birthYear",
  a."deathYear",
  a."primaryProfession",
  a."knownForTitles",
  c."titleType",
  c."first_primaryTitle",  -- Alterado para o novo nome
  c."originalTitle",
  c."isAdult",
  c."startYear",
  c."endYear",
  c."runtimeMinutes",
  c."genres",
  b."category",
  case b."job"
    when '\N' then null
    else b."job"
  end as "job",
  case b."characters"
    when '\N' then null
    else b."characters"
  end as "characters"
from name_basics a
join {{source('imdb', 'TB_TITLE_PRINCIPALS')}} b
  on a.nconst = b.nconst
join title_basics c
  on b.tconst = c.tconst
where a."first_primaryName" is not null  -- Alterado para o novo nome
  and b."category" is not null
  and c."first_primaryTitle" is not null  -- Alterado para o novo nome
  and a."birthYear" is not null
  and a."deathYear" is not null
  and a."primaryProfession" is not null
  and a."knownForTitles" is not null
  and c."titleType" is not null
  and c."originalTitle" is not null
  and c."isAdult" is not null
  and c."startYear" is not null
  and c."endYear" is not null
  and c."runtimeMinutes" is not null
  and c."genres" is not null