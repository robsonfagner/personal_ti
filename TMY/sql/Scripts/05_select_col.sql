-- Explicito e melhor que implicito, sempre 

SELECT idCliente,

 --(ctrl/) Comenta todo o cod.
		QtdePontos,
		QtdePontos + 10 AS QtdePontosPlus10 ,
		QtdePontos * 2 AS QtdePontosPlus2, -- <- Aqui eu tirei a ultima virgula que estava me atrapalhando

		DtCriacao,
		substr(DtCriacao,1,19) AS dtSubstring,		
		datetime(substr(DtCriacao,1,19)) as dtCriacaonova,
		strftime('%w', datetime(substr(DtCriacao,1,19))) AS diaSemana
				
FROM clientes

