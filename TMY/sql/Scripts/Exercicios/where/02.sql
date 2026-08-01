--Lista de pedidos realizados no fim de semana;

SELECT idTransacao,
		DtCriacao,
		strftime('%w',datetime(substr(DtCriacao,1,19))) AS diaSemana
		
FROM transacoes

WHERE diaSemana IN ('6','0')