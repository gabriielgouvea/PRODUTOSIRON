from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired

class ProdutoForm(FlaskForm):
    codigo = StringField('Código do Produto', validators=[DataRequired()])
    nome = StringField('Nome do Produto', validators=[DataRequired()])
    imagem_url = StringField('URL da Imagem')
    marca = SelectField('Marca', coerce=int, validators=[DataRequired()])
    categoria = SelectField('Categoria', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Cadastrar Produto')

class MarcaForm(FlaskForm):
    nome = StringField('Nome da Marca', validators=[DataRequired()])
    submit = SubmitField('Cadastrar Marca')

class CategoriaForm(FlaskForm):
    nome = StringField('Nome da Categoria', validators=[DataRequired()])
    submit = SubmitField('Cadastrar Categoria')

class UploadForm(FlaskForm):
    arquivo = FileField(
        'Selecione a planilha (.xlsx ou .csv)',
        validators=[
            FileRequired(),
            FileAllowed(['xlsx', 'csv'], 'Apenas arquivos .xlsx e .csv são permitidos!')
        ]
    )
    submit = SubmitField('Enviar Planilha')

class EditarProdutoForm(FlaskForm):
    codigo = StringField('Código do Produto', validators=[DataRequired()])
    nome = StringField('Nome do Produto', validators=[DataRequired()])
    imagem_url = StringField('URL da Imagem')
    marca = SelectField('Marca', coerce=int, validators=[DataRequired()])
    categoria = SelectField('Categoria', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Salvar Alterações')

class ExportarPlanilhaForm(FlaskForm):
    senha_admin = PasswordField('Senha de Administrador', validators=[DataRequired()])
    submit = SubmitField('Exportar Planilha')

# --- NOVO FORMULÁRIO DE BUSCA DE PRODUTO ---
class BuscarProdutoForm(FlaskForm):
    termo_busca = StringField('Buscar por Código ou Nome do Produto', validators=[DataRequired()])
    submit = SubmitField('Buscar Produto')