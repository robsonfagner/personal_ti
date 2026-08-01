SELECT
    t3.UUID AS IdCustomer,
    t3.Name,
    t2.IdTransaction,
    t1.DtTransaction,
    t1.Points,
    t2.Product,
    t2.Quantity

 FROM tb_transactions As t1

LEFT JOIN tb_transactions_cart AS t2
on t1.UUID = t2.IdTransaction

LEFT JOIN tb_customers AS t3
ON t1.IdCustomer = t3.UUID