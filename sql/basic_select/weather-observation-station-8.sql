SELECT S.CITY 
FROM STATION S 
WHERE RIGHT(S.CITY,1) IN ('a', 'e', 'i', 'o', 'u') AND LEFT(S.CITY, 1) IN ('A', 'E', 'I', 'O', 'U');
