from os import system
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#Criando banco de dados.
BANCO_ALUNO = create_engine("sqlite:///bancoaluno.db")

#Criando conexão com banco de dados.
Session = sessionmaker(bind=BANCO_ALUNO)
session = Session()

#Criando tabela.
Base = declarative_base()

class Aluno(Base):
    __tablename__ = "alunos"

    #Definindo atributos da tabela.
    ra = Column("ra",Integer,primary_key=True,autoincrement=True)
    nome = Column("nome",String)
    sobrenome = Column("sobrenome",String)
    email = Column("email",String)
    senha = Column("senha",String)

    def __init__(self,nome:str,sobrenome:str,email:str,senha:str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

#Criando tabela no banco de dados.
Base.metadata.create_all(bind=BANCO_ALUNO)

system("cls || clear")

#Create - Insert - Salvar.
def salvar_aluno():
    print("Solicitando dados para o aluno.")

    inserir_nome = input("Digite seu nome: ")
    inserir_sobrenome = input("Digite seu sobrenome: ")
    inserir_email = input("Digite seu e-mail: ")
    inserir_senha = input("Digite sua senha: ")

    aluno = Aluno(nome = inserir_nome,sobrenome = inserir_sobrenome,email = inserir_email,senha = inserir_senha)
    session.add(aluno)
    session.commit()

#Read - Select - Consultar.
def consultar_aluno():
    print("\nExibindo dados de todos os alunos.")
    lista_alunos = session.query(Aluno).all()

    for aluno in lista_alunos:
        print(
            f"\n{aluno.ra}"
            f"\n{aluno.nome}"
            f"\n{aluno.sobrenome}"
            f"\n{aluno.email}"
            f"\n{aluno.senha}"
            )

#Update - Update - Atualizar
def atualizar_aluno():
    print("\nAtualizando dados do aluno.")
    email_aluno = input("Digite o e-mail do aluno que será atualizado: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        aluno.nome = input("Digite seu nome: ")
        aluno.sobrenome = input("Digite seu sobrenome: ")
        aluno.email = input("Digite seu e-mail: ")
        aluno.senha = input("Digite sua senha: ")

        session.commit()
    else:
        print("Aluno não encontrado.")

    print("\nExibindo dados de todos os alunos.")
    lista_alunos = session.query(Aluno).all()

    for aluno in lista_alunos:
        print(
            f"\n{aluno.ra}"
            f"\n{aluno.nome}"
            f"\n{aluno.sobrenome}"
            f"\n{aluno.email}"
            f"\n{aluno.senha}"
            )
    
#Delete - DELETE - Excluir
def excluir_aluno():
    print("\nExcluindo os dados de um aluno.")
    email_aluno = input("Digite o e-mail do aluno que será excluído: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        session.delete(aluno)
        session.commit()
        print(f"Aluno {aluno.nome} excluído com sucesso!")

    else:
        print("Aluno não encontrado.")

    print("\nExibindo dados de todos os alunos.")
    lista_alunos = session.query(Aluno).all()

    for aluno in lista_alunos:
        print(
            f"\n{aluno.ra}"
            f"\n{aluno.nome}"
            f"\n{aluno.sobrenome}"
            f"\n{aluno.email}"
            f"\n{aluno.senha}"
            )
def consultar_unico_aluno():    
    print("\nConsultando dados de apenas um aluno.")
    email_aluno = input("Digite o e-mail do aluno: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        print(
        f"\n{aluno.ra}"
        f"\n{aluno.nome}"
        f"\n{aluno.sobrenome}"
        f"\n{aluno.email}"
        f"\n{aluno.senha}"
            )

    else:
        print("Aluno não encontrado.")


#Encerrando sessão.
session.close()