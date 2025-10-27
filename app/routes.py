from flask import render_template, redirect, url_for, flash, request, jsonify, make_response
from app import app, db
from app.forms import ProdutoForm, MarcaForm, CategoriaForm, UploadForm, EditarProdutoForm, ExportarPlanilhaForm, BuscarProdutoForm
from app.models import Produto, Marca, Categoria
from sqlalchemy import or_
import pandas as pd
import io

ADMIN_PASSWORD = "admin"

@app.route('/')
@app.route('/index')
def index():
    marcas = Marca.query.order_by(Marca.nome).all()
    categorias = Categoria.query.order_by(Categoria.nome).all()
    produtos_filtrados = []
    selected_marca, selected_categoria = "", ""
    if 'marca_nome' in request.args or 'categoria_nome' in request.args:
        marca_nome = request.args.get('marca_nome', '')
        categoria_nome = request.args.get('categoria_nome', '')
        selected_marca, selected_categoria = marca_nome, categoria_nome
        query = Produto.query.join(Marca).join(Categoria)
        if marca_nome: query = query.filter(Marca.nome == marca_nome)
        if categoria_nome: query = query.filter(Categoria.nome == categoria_nome)
        produtos_filtrados = query.order_by(Produto.nome).all()
    return render_template('index.html', title='Catálogo', produtos=produtos_filtrados, marcas=marcas, categorias=categorias, selected_marca=selected_marca, selected_categoria=selected_categoria)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    marca_form = MarcaForm()
    categoria_form = CategoriaForm()
    produto_form = ProdutoForm()
    upload_form = UploadForm()
    export_form = ExportarPlanilhaForm()
    buscar_form = BuscarProdutoForm() # Novo formulário de busca
    
    produtos_encontrados = None # Para guardar os resultados da busca

    marcas = Marca.query.order_by(Marca.nome).all()
    categorias = Categoria.query.order_by(Categoria.nome).all()
    produto_form.marca.choices = [(m.id, m.nome) for m in marcas]
    produto_form.categoria.choices = [(c.id, c.nome) for c in categorias]

    # --- LÓGICA DE BUSCA PARA EDITAR ---
    if 'submit_buscar' in request.form and buscar_form.validate_on_submit():
        termo = buscar_form.termo_busca.data
        search_term = f"%{termo}%"
        # Busca por código ou nome (case-insensitive)
        produtos_encontrados = Produto.query.filter(
            or_(Produto.codigo.ilike(search_term), Produto.nome.ilike(search_term))
        ).order_by(Produto.nome).all()

    # --- LÓGICA DE CADASTROS MANUAIS ---
    if 'submit_marca' in request.form and marca_form.validate_on_submit():
        # Lógica de cadastro de marca...
        return redirect(url_for('cadastro'))

    if 'submit_categoria' in request.form and categoria_form.validate_on_submit():
        # Lógica de cadastro de categoria...
        return redirect(url_for('cadastro'))

    if 'submit_produto' in request.form and produto_form.validate_on_submit():
        # Lógica de cadastro de produto...
        return redirect(url_for('cadastro'))

    return render_template('cadastro.html', title='Cadastro e Gestão',
                           marca_form=marca_form,
                           categoria_form=categoria_form,
                           produto_form=produto_form,
                           upload_form=upload_form,
                           export_form=export_form,
                           buscar_form=buscar_form, # Envia o form de busca
                           produtos_encontrados=produtos_encontrados) # Envia os resultados

@app.route('/upload-planilha', methods=['POST'])
def upload_planilha():
    form = UploadForm()
    if form.validate_on_submit():
        if request.form.get('senha_admin') != ADMIN_PASSWORD:
            flash('Senha de administrador incorreta!', 'error')
            return redirect(url_for('cadastro'))
            
        arquivo = form.arquivo.data
        try:
            df = pd.read_excel(arquivo) if arquivo.filename.endswith('.xlsx') else pd.read_csv(arquivo)
            colunas_necessarias = ['Codigo', 'Descricao', 'Marca', 'Categoria']
            if not all(col in df.columns for col in colunas_necessarias):
                flash(f'Erro! A planilha deve conter as colunas: {", ".join(colunas_necessarias)}', 'error')
                return redirect(url_for('cadastro'))

            # ... (Lógica de cache e processamento da planilha) ...
            
            novos_produtos = 0
            for index, row in df.iterrows():
                # ...
                # --- LÓGICA ATUALIZADA PARA INCLUIR IMAGEM ---
                imagem_url = "https://via.placeholder.com/200" # Padrão
                if 'URL_Imagem' in df.columns and pd.notna(row['URL_Imagem']):
                    imagem_url = str(row['URL_Imagem'])
                
                novo_produto = Produto(
                    # ...,
                    imagem_url=imagem_url,
                    # ...
                )
                db.session.add(novo_produto)
                novos_produtos += 1
            
            db.session.commit()
            flash(f'Upload concluído! {novos_produtos} produtos adicionados.', 'success')

        except Exception as e:
            db.session.rollback()
            flash(f'Ocorreu um erro ao processar o arquivo: {e}', 'error')

    return redirect(url_for('cadastro'))


# --- AS OUTRAS ROTAS (editar, excluir, exportar, search) CONTINUAM AQUI ---
@app.route('/editar-produto/<int:produto_id>', methods=['GET', 'POST'])
def editar_produto(produto_id):
    # ... código da rota de edição ...
    pass

@app.route('/excluir-produto/<int:produto_id>', methods=['POST'])
def excluir_produto(produto_id):
    # ... código da rota de exclusão ...
    pass

@app.route('/exportar-planilha', methods=['POST'])
def exportar_planilha():
    # ... código da rota de exportação ...
    pass

@app.route('/search')
def search():
    # ... código da rota de busca dinâmica ...
    pass