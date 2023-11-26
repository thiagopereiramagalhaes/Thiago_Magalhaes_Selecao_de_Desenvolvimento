SELECT Alunos.NomeAluno, AVG(Notas.nota)
FROM Alunos
JOIN Notas
ON Alunos.AlunoID = Notas.AlunoID
GROUP BY Alunos.AlunoID, Alunos.NomeAluno;