--desafio 1

SELECT id_cliente,
	   [quantidade pontos]as semUnderLine
   
FROM clientes
WHERE fl_twitch = 1
oRDER by [quantidade pontos] DESC
LIMIT 5 


-- Teste de comentário,