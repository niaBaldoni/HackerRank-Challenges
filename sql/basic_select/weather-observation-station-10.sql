SELECT DISTINCT S.CITY 
FROM STATION S 
WHERE RIGHT(S.CITY, 1) NOT IN ('a', 'e', 'i', 'o', 'u');