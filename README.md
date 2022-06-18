# Categorização de projetos de leis municipais utilizando agrupamento de dados

Trabalho de Conclusão de Curso UFMS - Ciência da Computação 

Este trabalho tem como objetivo realizar a categorização de projetos de lei municipais extraídos da interface web das camaras municipais das cidades selecionadas. Dessa maneira, iremos realizar uma análise dessas base de dados e extrair conhecimentos utéis para o apoio a gestão de conhecimento.

# Extrai_Dados
* Dividida por cidades, cada cidade possui:
  * Projeto de Extração de coleção de documentos de cada cidade baseada em seu site municipal(onde estão localizadas os projetos de leis) .
* Ferramentas Utilizadas: scrapy, selenium, python, pdf2text.

# Projetos_txt
* Todos projetos retirados dos websites estão agrupados por cidade.
* Cada documento é um projeto de lei legislativo em formato .txt

# Analise_Dados
* Arquivos e scripts que realizam o pré-processamento e aplicam os algoritmos de extração de conhecimento(K-Means, Hierarquização).

# Saida_Centroids&LDA
* Retorno das palavras e tópicos mais relevantes para cada base de dados selecionados.

[Link Artigo Completo - TCC ](https://drive.google.com/file/d/1WPOQ35GuQeacTvth0_t9ogh3xzspK4XG/view?usp=sharing)



