#En qué fecha AMZN tuvo el valor más bajo en el indicador CLOSE
SELECT B.NAME, B.DATE, A.CLOSE
  FROM
       (SELECT MIN(CLOSE) AS CLOSE
          FROM ALL_STOCKS
         WHERE NAME = 'AMZN') A
  JOIN
       (SELECT DATE, CLOSE, NAME
          FROM ALL_STOCKS
         WHERE NAME = 'AMZN') B
  ON A.CLOSE = B.CLOSE


#Qué empresa es la que ha tenido el indicador VOLUME más alto e indica la fecha del valor
SELECT A.NAME, B.DATE, A.VOLUME
  FROM
       (SELECT NAME, MAX(VOLUME) AS VOLUME
          FROM ALL_STOCKS A
         GROUP BY NAME
         ORDER BY 2 DESC
         LIMIT 1) A
  JOIN ALL_STOCKS B
  ON A.NAME = B.NAME AND A.VOLUME = B.VOLUME