"""Porque testar nosso codigo?
São testes automatizados. 
motivos: 
- Reduzir bugs 
- Testes garantem que novos recursos da sua aplicação não quebrem 
recursos antigos
- Testes garantem que bugs (problemas) que foram corrigidos anteriormente
continuem corrigidos
- Testes garantem que a refatoração que costumamos a fazer não tragam
novos problemas

TDD - test driven delevopment (Desenvolvimento guiado por testes)
Com TDD é utilizado estágios de desenvolvimento, ou seja, vc escreve
seu teste primeiro, depois vc escreve seu codigo minimo suficiente
para fazer o teste passar (Ou seja, executar com sucesso)

- Então refatora o codigo para realizar a funcionalidade novamente. 
- Uma vez que o teste passa, o recurso é considerado completo. 

Estes estágios de desenvolvimento do TDD é quase como um mantra que
os desenvolvedores seguem, conhecidos como 
red: teste falhou
green: teste passa
refactor: reescrever o codigo para que ele funciona melhor
"""




class Gato:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando')
        

felix = Gato("Felix")
felix.miar()
print(felix.nome)

