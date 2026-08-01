--Lista de clientes com 100 a 200 pontos (inclusive ambos);

SELECT idCliente,
	qtdePontos

FROM clientes

where qtdePontos >=100 AND qtdePontos <= 200

-- Ao invés de usar o between é melhor deixar explicito

