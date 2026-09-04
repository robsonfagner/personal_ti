SELECT *
FROM transacao_produto
    LEFT JOIN produtos on transacao_produto.IdProduto = produtos.IdProduto
limit 10