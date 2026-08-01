--SELECT * --
--FROM clientes
--ORDER BY qtdePontos DESC 
--limit 10;


SELECT *

from clientes 

where flTwitch =1

ORDER by DtCriacao ASC, qtdePontos DESC;

