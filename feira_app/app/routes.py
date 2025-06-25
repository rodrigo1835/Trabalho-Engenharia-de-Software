from flask import Blueprint, request, jsonify, render_template, session, flash, redirect
from datetime import datetime
from .models import db, Feira, Expositor, Produto, Ingresso, Usuario

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html', usuario_id=session.get('usuario_id'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        usuario = Usuario.query.filter_by(email=email, senha=senha).first()
        if usuario:
            session['usuario_id'] = usuario.id
            flash('Login realizado com sucesso!', 'success')
            return redirect('/')
        else:
            flash('Email ou senha inválidos', 'error')
            return redirect('/login')

    return render_template('login.html')


@bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        # Evita registro com e-mail duplicado
        if Usuario.query.filter_by(email=email).first():
            flash('Email já está em uso', 'error')
            return redirect('/registro')

        novo_usuario = Usuario(nome=nome, email=email, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Conta criada com sucesso! Faça login.', 'success')
        return redirect('/login')

    return render_template('registrar.html')

@bp.route('/logout')
def logout():
    session.pop('usuario_id', None)
    flash('Logout realizado com sucesso.', 'success')
    return redirect('/')

@bp.route('/criar-feira', methods=['GET','POST'])
def criar_feira():
    if request.method == 'POST':
        dados = request.form
        feira = Feira(
            nome=dados['nome'],
            descricao=dados.get('descricao'),
            data_inicio=datetime.strptime(dados['data_inicio'], "%Y-%m-%d").date(),
            data_fim=datetime.strptime(dados['data_fim'], "%Y-%m-%d").date(),
            local=dados['local'],
            cidade=dados['cidade'],
            estado=dados['estado'],
            criador_id= session.get('usuario_id')
        )
        db.session.add(feira)
        db.session.commit()
        flash('Feira Criada com sucesso', 'sucess')
        return redirect('/minhas-feiras')
    
    return render_template('criar-feira.html')

@bp.route('/feiras', methods=['GET'])
def listar_feiras():
    feiras = Feira.query.all()
    return render_template('feiras.html', feiras=feiras)

@bp.route('/feiras/<int:id>', methods=['GET'])
def listar_feira(id):
    feira = Feira.query.get(id)
    expositores = Expositor.query.filter_by(feira_id = id).all()
    if not feira:
        return "Feira não encontrada", 404
    return render_template('feira.html', feira=feira, expositores = expositores)

@bp.route('/minhas-feiras')
def minhas_feiras():
    if 'usuario_id' not in session:
        flash('Você precisa estar logado para ver suas feiras', 'error')
        return redirect('/login')
    
    usuario_id = session['usuario_id']
    feiras = Feira.query.filter_by(criador_id=usuario_id).all()
    
    return render_template('minhas_feiras.html', feiras=feiras)

@bp.route('/feiras/<int:id>/excluir', methods = ['POST'])
def excluir_feira(id):
    if 'usuario_id' not in session:
        flash('Você precisa estar logado.', 'error')
        return redirect('/login')

    feira = Feira.query.get_or_404(id)

    if feira.criador_id != session['usuario_id']:
        flash('Você não tem permissão para excluir esta feira.', 'error')
        return redirect('/minhas-feiras')

    # Verifica se existem expositores vinculados
    if feira.expositores:
        flash('Você não pode excluir uma feira que possui expositores cadastrados.', 'error')
        return redirect('/minhas-feiras')

    db.session.delete(feira)
    db.session.commit()
    flash('Feira excluída com sucesso.', 'success')
    return redirect('/minhas-feiras')

@bp.route('/criar-expositor', methods=['GET', 'POST'])
def criar_expositor():
    if 'usuario_id' not in session:
        flash('Você precisa estar logado.', 'error')
        return redirect('/login')

    usuario_id = session['usuario_id']
    feiras = Feira.query.filter_by(criador_id=usuario_id).all()

    if request.method == 'POST':
        dados = request.form
        feira_id = dados['feira_id']
        expositor = Expositor(
            nome=dados['nome'],
            descricao=dados['descricao'],
            contato=dados['contato'],
            feira_id=feira_id,
            criador_id=usuario_id
        )
        db.session.add(expositor)
        db.session.commit()
        flash('Expositor criado com sucesso!', 'success')
        return redirect('/meus-expositores')

    return render_template('criar_expositor.html', feiras=feiras)

@bp.route('/expositores/<int:feira_id>', methods=['GET'])
def listar_expositores(feira_id):
    expositores = Expositor.query.filter_by(feira_id=feira_id).all()
    return jsonify([{'id': e.id, 'nome': e.nome} for e in expositores])

@bp.route('/expositor/<int:id>')
def visualizar_expositor(id):
    expositor = Expositor.query.get_or_404(id)
    feira = Feira.query.get(expositor.feira_id)
    produtos = Produto.query.filter_by(expositor_id=id).all()
    return render_template('expositor.html', expositor=expositor, feira=feira, produtos = produtos)

@bp.route('/meus-expositores', methods = ['GET'])
def meus_expositores():
    if 'usuario_id' not in session:
        flash('Você precisa estar logado para ver seus expositores', 'error')
        return redirect('/login')
    
    usuario_id = session['usuario_id']
    expositores = Expositor.query.filter_by(criador_id=usuario_id).all()
    return render_template('meus_expositores.html', expositores = expositores)

@bp.route('/expositores/<int:id>/excluir', methods=['POST'])
def excluir_expositor(id):
    if 'usuario_id' not in session:
        flash('Você precisa estar logado.', 'error')
        return redirect('/login')

    expositor = Expositor.query.get_or_404(id)

    if expositor.criador_id != session['usuario_id']:
        flash('Você não tem permissão para excluir este expositor.', 'error')
        return redirect('/meus-expositores')

    # Verifica se existem produtos vinculados
    if expositor.produtos:
        flash('Você não pode excluir um expositor com produtos cadastrados.', 'error')
        return redirect('/meus-expositores')

    db.session.delete(expositor)
    db.session.commit()
    flash('Expositor excluído com sucesso!', 'success')
    return redirect('/meus-expositores')

@bp.route('/criar-produto', methods=['GET', 'POST'])
def criar_produto():
    if 'usuario_id' not in session:
        flash('Você precisa estar logado.', 'error')
        return redirect('/login')

    usuario_id = session['usuario_id']
    expositores = Expositor.query.filter_by(criador_id=usuario_id).all()

    if request.method == 'POST':
        dados = request.form
        produto = Produto(
            nome=dados['nome'],
            descricao=dados.get('descricao'),
            preco=float(dados['preco']),
            expositor_id=dados['expositor_id'], 
            criador_id=usuario_id
        )
        db.session.add(produto)
        db.session.commit()
        flash('Produto criado com sucesso!', 'success')
        return redirect('/meus-produtos')

    return render_template('criar_produto.html', expositores=expositores)

@bp.route('/produtos/<int:id>/excluir', methods=['POST'])
def excluir_produto(id):
    if 'usuario_id' not in session:
        flash('Você precisa estar logado.', 'error')
        return redirect('/login')

    produto = Produto.query.get_or_404(id)

    if produto.criador_id != session['usuario_id']:
        flash('Você não tem permissão para excluir este produto.', 'error')
        return redirect('/meus-produtos')

    db.session.delete(produto)
    db.session.commit()
    flash('Produto excluído com sucesso!', 'success')
    return redirect('/meus-produtos')


@bp.route('/meus-produtos', methods=['GET'])
def meus_produtos():
    usuario_id = session.get('usuario_id')
    if not usuario_id:
        flash('Você precisa estar logado.', 'error')
        return redirect('/login')

    produtos = Produto.query.filter_by(criador_id=usuario_id).all()
    return render_template('meus_produtos.html', produtos=produtos)


@bp.route('/feiras/<int:feira_id>/adquirir-ingresso', methods=['POST'])
def adquirir_ingresso(feira_id):
    if 'usuario_id' not in session:
        flash('Você precisa estar logado para adquirir um ingresso.', 'error')
        return redirect('/login')

    usuario_id = session['usuario_id']

    import random
    numero = f"{feira_id}-{usuario_id}-{random.randint(1000, 9999)}"

    ingresso = Ingresso(
        numero=numero,
        feira_id=feira_id,
        criador_id=usuario_id
    )
    db.session.add(ingresso)
    db.session.commit()
    flash('Ingresso adquirido com sucesso!', 'success')
    return redirect(f'/feiras/{feira_id}')

@bp.route('/meus-ingressos')
def meus_ingressos():
    if 'usuario_id' not in session:
        flash('Você precisa estar logado.', 'error')
        return redirect('/login')

    usuario_id = session['usuario_id']
    ingressos = Ingresso.query.filter_by(criador_id=usuario_id).all()

    # Montar lista com feira associada manualmente
    ingressos_info = []
    for ingresso in ingressos:
        feira = Feira.query.get(ingresso.feira_id)
        ingressos_info.append({
            'id': ingresso.id,
            'numero': ingresso.numero,
            'data_emissao': ingresso.data_emissao.strftime('%d/%m/%Y'),
            'feira_nome': feira.nome,
            'feira_local': feira.local,
            'feira_cidade': feira.cidade,
            'feira_estado': feira.estado,
            'feira_data_inicio': feira.data_inicio.strftime('%d/%m/%Y'),
            'feira_data_fim': feira.data_fim.strftime('%d/%m/%Y')
        })

    return render_template('meus_ingressos.html', ingressos=ingressos_info)

@bp.route('/ingressos/<int:id>/excluir', methods=['POST'])
def excluir_ingresso(id):
    if 'usuario_id' not in session:
        flash('Você precisa estar logado.', 'error')
        return redirect('/login')

    ingresso = Ingresso.query.get_or_404(id)

    if ingresso.criador_id != session['usuario_id']:
        flash('Você não tem permissão para excluir este ingresso.', 'error')
        return redirect('/meus-ingressos')

    db.session.delete(ingresso)
    db.session.commit()
    flash('Ingresso excluído com sucesso!', 'success')
    return redirect('/meus-ingressos')

@bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')