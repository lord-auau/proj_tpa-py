import Pessoa
res = 0
def pergunta():
    res = int(input("Deseja cadastrar uma nova pessoa? 1 - SIM ou 0 - NÃO: "))
    return res

cadastro = []

res = pergunta()
while(res == 1):
   nome = str(input("Digite seu nome: "))
   idade = int(input("Digite sua idade: "))
   cargo = str(input("Digite seu cargo: "))
   salario = float(input("Digite seu salario: "))
   
   cadastro.append(Pessoa.Pessoa(nome, idade, cargo, salario))
   res = pergunta()

def mostrar():
    print("{:<4}{:<10}{:<7}{:<10}{:<7}"
          .format("N°", "nome", "idade", "cargo", "salario"))
    
    y = 1
    for x in cadastro:
        print("{:<4}{:<10}{:<7}{:<10}{:<7}"
              .format(y,
                      x.get_nome(),
                      x.get_idade(),
                      x.get_cargo(),
                      x.get_salario()
                      ))
        y += 1
        mostrar()
        
        
        def alterar(x, y,z):
            res = int(input("Deseja fazer alguma alteração? 1 - SIM ou 0 - NÃO: "))
            return res
        
            if (y==0): cadastro[x].set_name(z)
            if (y==1): cadastro[x].set_idade(z)
            if (y==2): cadastro[x].set_cargo(z)
            if (y==3): cadastro[x].set_salario(z)
            
        alterar(0,0,"bruna")
        mostrar()