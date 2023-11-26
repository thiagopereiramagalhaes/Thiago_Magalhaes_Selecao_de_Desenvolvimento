SELECT Categorias.NomeCategoria, COUNT(Produtos.ProdutoID)
FROM Categorias
LEFT JOIN Produtos
ON Categorias.CategoriaID = Produtos.CategoriaID
GROUP BY Categorias.CategoriaID, Categorias.NomeCategoria;