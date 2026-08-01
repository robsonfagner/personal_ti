-- Seleção de produtos com CHURN no nome

SELECT *

FROM produtos

/*
WHERE DescNomeProduto = 'Churn_10pp'
OR DescNomeProduto = 'Churn_2pp'
OR DescNomeProduto = 'Churn_5pp'
*/


-- Outra forma de consultar
-- WHERE DescNomeProduto in('Churn_10pp','Churn_2pp','Churn_5pp')

WHERE DescNomeProduto like 'Churn%'