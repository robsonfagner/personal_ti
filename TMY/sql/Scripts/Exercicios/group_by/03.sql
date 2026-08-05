--Qual client fez mais transsações no ano de 2024

SELECT idCliente,
		count(*),
		count(DISTINCT idTransacao)

FROM transacoes

WHERE DtCriacao >= '2004-01-01'
AND DtCriacao < '2025-01-01'

GROUP by idCliente
ORDER BY count(*) DESC