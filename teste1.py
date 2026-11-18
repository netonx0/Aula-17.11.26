import sqlite3 ### import bliblioteca sqlite3

try:
    banco = sqlite3.connect('banco.db') #### conecta ao banco

    cursor = banco.cursor() ## cria o objeto Cursor reponsavel por criar  elementos no sql

    cursor.execute("CREATE TABLE aluno(id_aluno int, Nome text, idade int, email text)") ### cria a tabela aluno e e as colunas com seus respectivos nomes

    cursor.execute("INSERT INTO aluno VALUES (1, 'JOÃO',20,'joaozinholeroy@gmail.com') ") ### insere  os dados  na linha 1
    cursor.execute("INSERT INTO aluno VALUES (3, 'ricardo',26,'jheimesbrow@gmail.com') ") ### insere  os dados  na linha 2
    banco.commit()
    print("Os dados foram adicionados com sucesso!!")  ### print na tela caso tenha ocorrido tudo bem


    cursor.execute("Select *FROM aluno")  ### seleciona a tabela aluno
    print(cursor.fetchall())

    cursor.execute("DELETE from aluno WHERE idade = 20")  ### deleta a linha que cotenha idad= 20

    banco.commit() # confima as ateraçoes
    banco.close()  ### encerra a conecxao com banco de dados
    print("Os dados foram removidos com sucesso!!")  ### prnt a mensagem caso tenha ocorrido tudo bem

except sqlite3.Error as erro:
    print("Erro ao excluir: ", erro)  ### print caso ocorrer 
