SELECT IdTransacao, 
		qtdePontos,
		
		CASE 
			WHEN qtdePontos < 10 THEN 'Baixo'
			WHEN qtdePontos < 500 THEN 'Medio'
			ELSE 'Alto'
		END as FlQtdePontos
			

FROM transacoes

ORDER by qtdePontos desc