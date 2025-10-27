from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import ProdutoForm, MarcaForm, CategoriaForm
from app.models import Produto, Marca, Categoria

# Rota da página inicial (que vai mostrar os produtos)
@app.route('/')
@app.route('/index')
def index():
    # Busca todas as marcas e categorias para popular os menus de filtro
    marcas = Marca.query.order_by(Marca.nome).all()
    categorias = Categoria.query.order_by(Categoria.nome).all()
    
    produtos_filtrados = []
    # Guarda os valores selecionados para enviar de volta ao template
    selected_marca = ""
    selected_categoria = ""

    # Checa se o formulário foi usado (se os campos de nome estão na URL)
    if 'marca_nome' in request.args or 'categoria_nome' in request.args:
        marca_nome = request.args.get('marca_nome', type=str)
        categoria_nome = request.args.get('categoria_nome', type=str)

        # Atualiza as variáveis com os valores selecionados para manter nos campos
        selected_marca = marca_nome
        selected_categoria = categoria_nome

        # Começa a busca juntando as tabelas para poder filtrar pelo nome
        query = Produto.query.join(Marca).join(Categoria)

        # Se um nome de marca foi passado no filtro, aplica o filtro
        if marca_nome:
            query = query.filter(Marca.nome == marca_nome)
        
        # Se um nome de categoria foi passado no filtro, aplica o filtro
        if categoria_nome:
            query = query.filter(Categoria.nome == categoria_nome)

        # Executa a busca e ordena por nome
        produtos_filtrados = query.order_by(Produto.nome).all()

    return render_template('index.html', title='Catálogo', 
                           produtos=produtos_filtrados,
                           marcas=marcas,
                           categorias=categorias,
                           selected_marca=selected_marca,
                           selected_categoria=selected_categoria)

# Rota para a página de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    # Instancia os três formulários que criamos
    marca_form = MarcaForm()
    categoria_form = CategoriaForm()
    produto_form = ProdutoForm()

    # --- Lógica para popular os menus de seleção (dropdowns) ---
    marcas = Marca.query.order_by(Marca.nome).all()
    categorias = Categoria.query.order_by(Categoria.nome).all()
    produto_form.marca.choices = [(m.id, m.nome) for m in marcas]
    produto_form.categoria.choices = [(c.id, c.nome) for c in categorias]

    # --- Lógica para salvar os dados ---

    # Checa se o formulário de MARCA foi enviado e é válido
    if marca_form.validate_on_submit() and 'submit_marca' in request.form:
        nova_marca = Marca(nome=marca_form.nome.data)
        db.session.add(nova_marca)
        db.session.commit()
        flash('Marca cadastrada com sucesso!')
        return redirect(url_for('cadastro'))

    # Checa se o formulário de CATEGORIA foi enviado e é válido
    if categoria_form.validate_on_submit() and 'submit_categoria' in request.form:
        nova_categoria = Categoria(nome=categoria_form.nome.data)
        db.session.add(nova_categoria)
        db.session.commit()
        flash('Categoria cadastrada com sucesso!')
        return redirect(url_for('cadastro'))

    # Checa se o formulário de PRODUTO foi enviado e é válido
    if produto_form.validate_on_submit() and 'submit_produto' in request.form:
        # Usa uma URL placeholder se o campo de imagem estiver vazio
        imagem = produto_form.imagem_url.data or "https://via.placeholder.com/200"
        novo_produto = Produto(
            codigo=produto_form.codigo.data,
            nome=produto_form.nome.data,
            imagem_url=imagem,
            marca_id=produto_form.marca.data,
            categoria_id=produto_form.categoria.data
        )
        db.session.add(novo_produto)
        db.session.commit()
        flash('Produto cadastrado com sucesso!')
        return redirect(url_for('cadastro'))

    # Se a página for apenas carregada (GET), renderiza o template com os formulários
    return render_template('cadastro.html', title='Cadastro',
                           marca_form=marca_form,
                           categoria_form=categoria_form,
                           produto_form=produto_form)