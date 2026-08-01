-- SELECT IdProduto,
-- 		count(*)
-- 
-- FROM transacao_produto
-- 
-- group by IdProduto


SELECT idCliente, 
		sum(QtdePontos),
		count(IdTransacao)
		
		
FROM transacoes


WHERE DtCriacao >= '2025-07-01'
AND DtCriacao < '2025-08-01'

GROUP BY idCliente

ORDER BY sum(QtdePontos) DESC

LIMIT 10



