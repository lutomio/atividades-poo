class Livro:
    def __init__(self, titulo, autores, ano, editora, edicao, volume):
        self.titulo = titulo
        self.autores = autores
        self.ano = ano
        self.editora = editora
        self.edicao = edicao
        self.volume = volume

    def get_titulo(self):
        return self.titulo

    def get_autores(self):
        return self.autores

    def get_ano(self):
        return self.ano

    def get_editora(self):
        return self.editora

    def get_edicao(self):
        return self.edicao

    def get_volume(self):
        return self.volume


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def pesquisar_titulo(self, titulo):
        resultados = []
        for livro in self.livros:
            if livro.get_titulo() == titulo:
                resultados.append(livro)
        return resultados

    def pesquisar_autor(self, autor):
        resultados = []
        for livro in self.livros:
            if autor in livro.get_autores():
                resultados.append(livro)
        return resultados

    def pesquisar_ano(self, ano):
        resultados = []
        for livro in self.livros:
            if livro.get_ano() == ano:
                resultados.append(livro)
        return resultados

    def pesquisar_editora(self, editora):
        resultados = []
        for livro in self.livros:
            if livro.get_editora() == editora:
                resultados.append(livro)
        return resultados

    def pesquisar_edicao(self, edicao):
        resultados = []
        for livro in self.livros:
            if livro.get_edicao() == edicao:
                resultados.append(livro)
        return resultados

    def pesquisar_volume(self, volume):
        resultados = []
        for livro in self.livros:
            if livro.get_volume() == volume:
                resultados.append(livro)
        return resultados


livro1 = Livro("Ciencias da Computaçao", ["Jorge Amado"], 2009, "Livramento", "Ediçao 1", "Volume 1")
biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)

livros_pesquisados = biblioteca.pesquisar_titulo("Ciencias da Computaçao")
for livro in livros_pesquisados:
    print(livro.get_titulo())


