SELECT DISTINCT S.CITY FROM STATION S 
WHERE LEFT(S.CITY,1) NOT IN ('A', 'E', 'I', 'O', 'U') 
OR RIGHT(S.CITY,1) NOT IN ('a', 'e', 'i', 'o', 'u');
