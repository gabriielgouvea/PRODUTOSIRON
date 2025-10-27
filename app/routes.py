from flask import render_template, redirect, url_for, flash, request, jsonify, make_response, session
from app import app, db
from app.forms import LoginForm, ProdutoForm, MarcaForm, CategoriaForm, UploadForm, EditarProdutoForm, ExportarPlanilhaForm, BuscarProdutoForm
from app.models import Produto, Marca, Categoria
from sqlalchemy import or_
import pandas as pd
import io
from functools import wraps

# Credenciais do administrador
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"

# --- DECORADOR DE LOGIN ---
# Esta função "envelopa" outras rotas para protegê-las.
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash('Por favor, faça login para acessar esta página.', 'error')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# --- ROTAS DE LOGIN E LOGOUT ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'logged_in' in session:
        return redirect(url_for('cadastro')) # Se já está logado, vai direto para a gestão

    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == ADMIN_USERNAME and form.password.data == ADMIN_PASSWORD:
            session['logged_in'] = True
            flash('Login bem-sucedido!', 'success')
            # Redireciona para a página de gestão após o login
            return redirect(url_for('cadastro'))
        else:
            flash('Usuário ou senha inválidos.', 'error')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Você saiu do sistema.', 'success')
    return redirect(url_for('index'))

# --- ROTAS PÚBLICAS ---

@app.route('/')
@app.route('/index')
def index():
    marcas = Marca.query.order_by(Marca.nome).all()
    categorias = Categoria.query.order_by(Categoria.nome).all()
    
    produtos_filtrados = []
    selected_marca = ""
    selected_categoria = ""

    if 'marca_nome' in request.args or 'categoria_nome' in request.args:
        marca_nome = request.args.get('marca_nome', type=str)
        categoria_nome = request.args.get('categoria_nome', type=str)

        selected_marca = marca_nome
        selected_categoria = categoria_nome

        query = Produto.query.join(Marca).join(Categoria)

        if marca_nome:
            query = query.filter(Marca.nome == marca_nome)
        
        if categoria_nome:
            query = query.filter(Categoria.nome == categoria_nome)

        produtos_filtrados = query.order_by(Produto.nome).all()

    return render_template('index.html', title='Catálogo', 
                           produtos=produtos_filtrados,
                           marcas=marcas,
                           categorias=categorias,
                           selected_marca=selected_marca,
                           selected_categoria=selected_categoria)

@app.route('/search')
def search():
    query = request.args.get('q', '', type=str)
    produtos_encontrados = []
    
    if query:
        search_term = f"%{query}%"
        produtos = Produto.query.filter(Produto.nome.ilike(search_term)).order_by(Produto.nome).limit(50).all()
        produtos_encontrados = [
            {'codigo': p.codigo, 'nome': p.nome, 'imagem_url': p.imagem_url}
            for p in produtos
        ]
        
    return jsonify(produtos_encontrados)

# --- ROTAS PROTEGIDAS POR LOGIN ---

@app.route('/cadastro', methods=['GET', 'POST'])
@login_required
def cadastro():
    marca_form = MarcaForm()
    categoria_form = CategoriaForm()
    produto_form = ProdutoForm()
    upload_form = UploadForm()
    export_form = ExportarPlanilhaForm()
    buscar_form = BuscarProdutoForm()
    
    produtos_encontrados = None

    marcas = Marca.query.order_by(Marca.nome).all()
    categorias = Categoria.query.order_by(Categoria.nome).all()
    produto_form.marca.choices = [(m.id, m.nome) for m in marcas]
    produto_form.categoria.choices = [(c.id, c.nome) for c in categorias]

    if 'submit_buscar' in request.form and buscar_form.validate_on_submit():
        termo = buscar_form.termo_busca.data
        search_term = f"%{termo}%"
        produtos_encontrados = Produto.query.filter(
            or_(Produto.codigo.ilike(search_term), Produto.nome.ilike(search_term))
        ).order_by(Produto.nome).all()

    if 'submit_marca' in request.form and marca_form.validate_on_submit():
        nome_padronizado = marca_form.nome.data.strip().title()
        if not Marca.query.filter_by(nome=nome_padronizado).first():
            db.session.add(Marca(nome=nome_padronizado))
            db.session.commit()
            flash('Marca cadastrada com sucesso!', 'success')
        else:
            flash('Essa marca já existe.', 'error')
        return redirect(url_for('cadastro'))

    if 'submit_categoria' in request.form and categoria_form.validate_on_submit():
        nome_padronizado = categoria_form.nome.data.strip().title()
        if not Categoria.query.filter_by(nome=nome_padronizado).first():
            db.session.add(Categoria(nome=nome_padronizado))
            db.session.commit()
            flash('Categoria cadastrada com sucesso!', 'success')
        else:
            flash('Essa categoria já existe.', 'error')
        return redirect(url_for('cadastro'))

    if 'submit_produto' in request.form and produto_form.validate_on_submit():
        imagem = produto_form.imagem_url.data or "https://via.placeholder.com/200"
        novo_produto = Produto(codigo=produto_form.codigo.data, nome=produto_form.nome.data, imagem_url=imagem, marca_id=produto_form.marca.data, categoria_id=produto_form.categoria.data)
        db.session.add(novo_produto)
        db.session.commit()
        flash('Produto cadastrado com sucesso!', 'success')
        return redirect(url_for('cadastro'))

    return render_template('cadastro.html', title='Cadastro e Gestão',
                           marca_form=marca_form,
                           categoria_form=categoria_form,
                           produto_form=produto_form,
                           upload_form=upload_form,
                           export_form=export_form,
                           buscar_form=buscar_form,
                           produtos_encontrados=produtos_encontrados)

@app.route('/editar-produto/<int:produto_id>', methods=['GET', 'POST'])
@login_required
def editar_produto(produto_id):
    produto = Produto.query.get_or_404(produto_id)
    form = EditarProdutoForm(obj=produto)

    marcas = Marca.query.order_by(Marca.nome).all()
    categorias = Categoria.query.order_by(Categoria.nome).all()
    form.marca.choices = [(m.id, m.nome) for m in marcas]
    form.categoria.choices = [(c.id, c.nome) for c in categorias]
    
    if form.validate_on_submit():
        produto.codigo = form.codigo.data
        produto.nome = form.nome.data
        produto.imagem_url = form.imagem_url.data or "https://via.placeholder.com/200"
        produto.marca_id = form.marca.data
        produto.categoria_id = form.categoria.data
        db.session.commit()
        flash('Produto atualizado com sucesso!', 'success')
        return redirect(url_for('cadastro'))

    if request.method == 'GET':
        form.marca.data = produto.marca_id
        form.categoria.data = produto.categoria_id

    return render_template('editar_produto.html', title='Editar Produto', form=form, produto=produto)


@app.route('/excluir-produto/<int:produto_id>', methods=['POST'])
@login_required
def excluir_produto(produto_id):
    produto = Produto.query.get_or_404(produto_id)
    db.session.delete(produto)
    db.session.commit()
    flash(f'Produto "{produto.nome}" excluído com sucesso!', 'success')
    return redirect(request.referrer or url_for('index'))


@app.route('/upload-planilha', methods=['POST'])
@login_required
def upload_planilha():
    form = UploadForm()
    if form.validate_on_submit():
        arquivo = form.arquivo.data
        try:
            df = pd.read_excel(arquivo) if arquivo.filename.endswith('.xlsx') else pd.read_csv(arquivo)
            colunas_necessarias = ['Codigo', 'Descricao', 'Marca', 'Categoria']
            if not all(col in df.columns for col in colunas_necessarias):
                flash(f'Erro! A planilha deve conter as colunas: {", ".join(colunas_necessarias)}', 'error')
                return redirect(url_for('cadastro'))

            marcas_cache = {m.nome: m for m in Marca.query.all()}
            categorias_cache = {c.nome: c for c in Categoria.query.all()}
            produtos_existentes = {p.codigo for p in Produto.query.all()}
            
            novos_produtos = 0
            produtos_ignorados = 0

            for index, row in df.iterrows():
                codigo = str(row['Codigo'])
                
                if codigo in produtos_existentes:
                    produtos_ignorados += 1
                    continue

                nome_marca = str(row['Marca']).strip().title() if pd.notna(row['Marca']) else "Não Especificada"
                marca = marcas_cache.get(nome_marca)
                if not marca:
                    marca = Marca(nome=nome_marca)
                    db.session.add(marca)
                    db.session.commit()
                    marcas_cache[nome_marca] = marca
                
                nome_categoria = str(row['Categoria']).strip().title() if pd.notna(row['Categoria']) else "Não Especificada"
                categoria = categorias_cache.get(nome_categoria)
                if not categoria:
                    categoria = Categoria(nome=nome_categoria)
                    db.session.add(categoria)
                    db.session.commit()
                    categorias_cache[nome_categoria] = categoria

                imagem_url = "https://via.placeholder.com/200"
                if 'URL_Imagem' in df.columns and pd.notna(row['URL_Imagem']):
                    imagem_url = str(row['URL_Imagem'])

                novo_produto = Produto(codigo=codigo, nome=str(row['Descricao']), imagem_url=imagem_url, marca_id=marca.id, categoria_id=categoria.id)
                db.session.add(novo_produto)
                novos_produtos += 1
            
            db.session.commit()
            flash(f'Upload concluído! {novos_produtos} produtos adicionados. {produtos_ignorados} produtos já existentes foram ignorados.', 'success')

        except Exception as e:
            db.session.rollback()
            flash(f'Ocorreu um erro ao processar o arquivo: {e}', 'error')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(error, 'error')
    return redirect(url_for('cadastro'))

@app.route('/exportar-planilha', methods=['POST'])
@login_required
def exportar_planilha():
    form = ExportarPlanilhaForm()
    if form.validate_on_submit():
        if form.senha_admin.data == ADMIN_PASSWORD:
            produtos = Produto.query.join(Marca).join(Categoria).all()
            dados = [{
                'Codigo': p.codigo,
                'Descricao': p.nome,
                'Marca': p.marca.nome,
                'Categoria': p.categoria.nome,
                'URL_Imagem': p.imagem_url
            } for p in produtos]
            
            df = pd.DataFrame(dados)
            output = io.BytesIO()
            writer = pd.ExcelWriter(output, engine='openpyxl')
            df.to_excel(writer, index=False, sheet_name='Produtos')
            writer.close()
            output.seek(0)
            
            flash('Exportação iniciada. O download começará em breve.', 'success')
            return make_response(output.getvalue(), {
                'Content-Disposition': 'attachment; filename=catalogo_produtos.xlsx',
                'Content-type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            })
        else:
            flash('Senha de administrador incorreta!', 'error')
    else:
        flash('O campo de senha é obrigatório.', 'error')
    return redirect(url_for('cadastro'))