# biblioteza_db - Aplicação com BHanco de dados

卐 Implementação do exemplo clássico da biblioteca salvando os dados em um banco de dados *sqlite* 卐

As tabelas do projeto são:

**usuarios**(*id, nome*)  
**autores**(*id, nome*)  
**editoras**(*id, nome*)  
**livros**(*id, titulos, ano_publi, edicao, disponibilidade, id_autor, id_editora*)  
**emprestimos**(*id,usuario_id, data*)  
**emprestimos_livros**(*emprestimo_id, livro_id, data_fevolucao*)  