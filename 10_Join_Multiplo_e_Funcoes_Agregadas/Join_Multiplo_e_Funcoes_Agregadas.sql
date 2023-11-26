SELECT Clientes.NomeCliente, Pedidos.PedidoID, SUM(Produtos.Quantidade)
FROM Clientes
JOIN Pedidos 
ON Clientes.ClienteID = Pedidos.ClienteID
JOIN Produtos
ON Pedidos.ProdutoID = Produtos.ProdutoID
GROUP BY Clientes.ClienteID, Clientes.NomeCliente, Pedidos.PedidoID;