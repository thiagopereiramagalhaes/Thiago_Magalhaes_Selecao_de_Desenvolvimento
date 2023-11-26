SELECT Clientes.NomeCliente, Pedidos.PedidoID, Pedidos.DataPedido
FROM Clientes
JOIN Pedidos 
ON Clientes.ClienteID = Pedidos.ClienteID
ORDER BY Pedidos.DataPedido DESC;