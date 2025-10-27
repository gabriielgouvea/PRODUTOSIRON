from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from app.models import Marca, Categoria

class ProdutoForm(FlaskForm):
    codigo = StringField('Código do Produto', validators=[DataRequired()])
    nome = StringField('Nome do Produto', validators=[DataRequired()])
    imagem_url = StringField('URL da Imagem')

    # Os campos 'choices' serão preenchidos depois, na nossa rota.
    marca = SelectField('Marca', coerce=int, validators=[DataRequired()])
    categoria = SelectField('Categoria', coerce=int, validators=[DataRequired()])

    submit = SubmitField('Cadastrar Produto')

    # (coloque isso depois da classe ProdutoForm)

class MarcaForm(FlaskForm):
    nome = StringField('Nome da Marca', validators=[DataRequired()])
    submit = SubmitField('Cadastrar Marca')

class CategoriaForm(FlaskForm):
    nome = StringField('Nome da Categoria', validators=[DataRequired()])
    submit = SubmitField('Cadastrar Categoria')