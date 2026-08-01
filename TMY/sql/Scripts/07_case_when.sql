--Intervalos 
--de 0 a 500  -> Poney
--de 501 a 1000 - P Premium
--de 1001 a 5000 -> Aprendiz
--de 5001 a 10000 -> Mestre
--+10001 - Supremo



SELECT idCliente,
	   qtdepontos,
	   CASE
		   
	   	 WHEN qtdePontos <= 500 THEN 'Poney'
	   	 WHEN qtdePontos <=1000 THEN 'P Premium'
	     WHEN qtdePontos <=5000 THEN 'Mago Aprendiz'
	   	 WHEN qtdePontos <=10000 THEN 'Mestre'
	   	 ELSE 'Mago Supremo'
	   	
	   END As NomeGrupo,
	   
	   CASE 
	   		when qtdepontos <= 1000 then 1
	   		else 0
	   	END AS flPonei,
	   	
	   	CASE
	   		when qtdePontos > 1000 then 1
	   		else 0 
	   	end AS flMago
	       	

FROM clientes

Where flPonei = 1

ORDER BY qtdepontos DESC






