-- Lista de transações com apenas 1 ponto;

/*
SELECT * 
FROM transacoes 
WHERE transacoes.QtdePontos = 1
*/

-- Aqui selecionei apenas onde 1 ponto, no ID
SELECT idTransacao,

	   QtdePontos
	   
FROM transacoes

WHERE QtdePontos = 1

