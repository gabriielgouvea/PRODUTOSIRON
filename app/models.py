from app import db

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    produtos = db.relationship('Produto', backref='marca', lazy=True)

    def __repr__(self):
        return f"Marca('{self.nome}')"

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    produtos = db.relationship('Produto', backref='categoria', lazy=True)

    def __repr__(self):
        return f"Categoria('{self.nome}')"

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(20), unique=True, nullable=False)
    nome = db.Column(db.String(200), nullable=False)
    imagem_url = db.Column(db.String(300), nullable=False, default='url_da_imagem_padrao.jpg')
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)

    def __repr__(self):
        return f"Produto('{self.nome}', '{self.codigo}')"