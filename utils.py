from models import Pessoa

def insere_pessoa():
    pessoa = Pessoa(nome='Teste2', idade=52)
    print(pessoa)
    pessoa.save()


def consulta_pessoa():
    pessoa = Pessoa.query.all()
    print(pessoa)
    pessoa = Pessoa.query.filter_by(nome = 'Teste').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoa.query.filter_by(nome='Teste').first()
    pessoa.idade = 40
    pessoa.nome = 'Sucesso'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoa.query.filter_by(nome='Teste1').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoa()
    # altera_pessoa()
    exclui_pessoa()
    consulta_pessoa()

