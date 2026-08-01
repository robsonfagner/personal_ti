SELECT 
	count(*),
	count(distinct IdTransacao),
	count(Distinct IdCliente )

FROM transacoes

WHERE DtCriacao >= '2025-07-01'
AND DtCriacao < '2025-08-01'

ORDER by DtCriacao DESC

