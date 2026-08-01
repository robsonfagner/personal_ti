-- Qual cliente juntou mais pontos positivios em 2025-05?

SELECT idCliente,
		sum(qtdePontos) AS totalPontos2

from transacoes

WHERE DtCriacao >= ' 2025-05-01'
AND DtCriacao < '2025-06-01'
AND qtdePontos > 0

GROUP BY idCliente	
ORDER BY sum(QtdePontos) DESC

-- Stop 22:00
--LIMIT 1