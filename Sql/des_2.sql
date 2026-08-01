SELECT id_cliente,
		[quantidade pontos],
		
		CASE
			WHEN [quantidade pontos] > 10000 THEN  'VIP'
			WHEN [quantidade pontos] >= 5000 THEN  'Membro'
			ELSE 'Iniciante'
		END as Categoria
		

FROM clientes
ORDER BY [quantidade pontos] DESC;