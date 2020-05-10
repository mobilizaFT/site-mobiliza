# Tutorial de Postagem
Duas áreas do site podem sofrer edição por meio de markdown, são elas: FT Ensina e FT para Todos. Markdown é uma linguagem de marcação e é escrita em documentos com extensão do tipo ".md".

## Postagens no FT Ensina
Para gerenciar as postanges do FT Ensina precisamos seguir esse caminho: **ft_ensina > videos**.

Cada arquivo do tipo .md representa um curso em andamento, por exemplo: APC, CPE e PCALC.

1. Para **adicionar um novo curso** basta clicar em "Create new file".
2. Dê um nome para o arquivo (não se esqueça de escrever o .md no final).
3. Escreva o seguinte modelo:
```
# Nome do Curso
## Live 1
#### 
###### (link da live)
```

![imagem1](https://user-images.githubusercontent.com/54515091/81501244-bd3b5080-92ad-11ea-9a4a-c85aa98b55de.png)

4. Clique em "Commit changes" e siga:

![imagem2](https://user-images.githubusercontent.com/54515091/81501253-c62c2200-92ad-11ea-8c3b-182f46f52fc8.png)

Agora, espere a aprovação de outro colega. É importante lembrar que, por precisar de aprovação, _nenhuma alteração é feita imediatamente no site_.

Para **alterar os cursos** (adicionar live 2, live 3, etc) basta clicar no curso que quer alterar, quebrar algumas linhas e usar o seguinte modelo:
```
## Live 2
#### 
###### (link da live 2)
```
Então, se eu quiséssemos adicionar a live 2 do curso de CPE, por exemplo, nosso arquivo cpe.md ficaria da seguinte maneira:
```
# Computação para Engenharia (título do curso)
## Live 1
####
###### (link da live 1)

## Live 2
#### 
###### (link da live 2)
```
Novamente clicamos em "Commit changes" e esperamos a aprovação de outro colega.

## Postagens no FT para Todos
O FT para Todos tem uma estrutura mais simples que a do FT Ensina, para publicarmos devemos ir em: **ft_para_todos > blog**.

Todas as alterações são feitas no arquivo **posts.md**, clique nele e siga o seguinte modelo para adicionar novas postagens:
```
# Autor 
## Data 
### Título 
#### Descrição (máximo de 80 caracteres)
##### link
###### Assistir (botão escrito "Assistir")
```
Depois clique em "Commit changes" e espere pela aprovação.
