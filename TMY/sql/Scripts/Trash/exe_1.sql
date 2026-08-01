-- Selecione todos os clientes com email cadastrado
/*
	SELECT *
	FROM clientes c 
	where c.flEmail = 1
*/
--Selecione todos clientes com mais de 500 pontos
/*
	SELECT * 
	FROM transacoes t 
	WHERE QtdePontos > 500
*/

--SELECT * FROM produtos p 

SELECT * FROM produtos 

WHERE DescNomeProduto like 'Churn%'

