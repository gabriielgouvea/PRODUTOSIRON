from app import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(64), index=True, unique=True)
    nome = db.Column(db.String(128), index=True)
    imagem_url = db.Column(db.String(256))
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))

    marca = db.relationship('Marca')
    categoria = db.relationship('Categoria')

    def __repr__(self):
        return f'<Produto {self.nome} - {self.codigo}>'

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), index=True, unique=True)
    produtos = db.relationship('Produto', backref='marca_obj', lazy='dynamic') # Adicionado backref para facilitar

    def __repr__(self):
        return f'<Marca {self.nome}>'

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), index=True, unique=True)
    produtos = db.relationship('Produto', backref='categoria_obj', lazy='dynamic') # Adicionado backref para facilitar

    def __repr__(self):
        return f'<Categoria {self.nome}>'