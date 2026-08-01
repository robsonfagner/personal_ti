-- Dia 09,Novas Colunas

SELECT 
		idCliente,	
		DtCriacao,	
		substr(DtCriacao, 1, 19) AS Dtcriacaonova 
FROM clientes;

-- Padronização das datas, do campo 1 até o 10
