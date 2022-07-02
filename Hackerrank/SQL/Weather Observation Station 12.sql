SELECT DISTINCT city FROM station 
WHERE city not RLIKE '^[aeiou]'
and city not rlike '[aeiou]$';