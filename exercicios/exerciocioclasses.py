class Musica:
    def __init__(self, nome, estilo):
        self.nome = nome
        self.estilo = estilo
    
    def apresentar(self):
        print(f"Olá, me chamo {self.nome} e gosto de escutar {self.estilo}")
    
pessoa = Musica("Tony", "Rock")
pessoa.apresentar()
print()

class Musica1(Musica):
    def __init__(self, nome, estilo, artista):
        super().__init__(nome, estilo)
        self.artista = artista
    
    def escutar(self):
        print(f"{self.nome} escuta {self.artista}")
    
    def escutar1(self):
        print(f"Estilo favorito de {self.nome}: {self.estilo}")

pessoa1 = Musica1("Luiz", "RAP", "Kanye West")
pessoa1.apresentar()
pessoa1.escutar()
pessoa1.escutar1()
print()

class Musica2(Musica1):
    def __init__(self, nome, estilo, artista, musica):
        super().__init__(nome, estilo, artista)
        self.musica = musica
    
    def musica_fav(self):
        print(f"A musica favorita de {self.nome} é {self.musica}")
    
    def musica_artista(self):
        print(f"A musica {self.musica} é do artista {self.artista}")
    
    def artista_estilo(self):
        print(f"{self.artista} canta no estilo {self.estilo}")

pessoa2 = Musica2("Luiz", "RAP", "Kanye West", "Runaway")
pessoa2.apresentar()
pessoa2.musica_fav()
pessoa2.musica_artista()
pessoa2.artista_estilo()
print()
pessoa3 = Musica2("Tony", "Rock", "Eagles", "Hotel California")
pessoa3.apresentar()
pessoa3.musica_fav()
pessoa3.musica_artista()
pessoa3.artista_estilo()