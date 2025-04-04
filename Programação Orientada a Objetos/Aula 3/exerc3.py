class Livro:
    def __init__(self, title, autor, ano, disp):
        self.title = title
        self.autor = autor
        self.ano = ano
        self.disp = disp

    def emprestar(self, disp):
        self.disp = disp
        
    def devoler(self, disp):
        self.disp = disp

livro = Livro("como subir na vida", "My", 2025, "sim")
print(livro.title)
print(livro.autor)
print(livro.ano)
print(livro.disp)
