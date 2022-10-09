#Função sem argumentos
def saudacao():
    print("Boa noite")

#Função sem argumentos
def elogiar_usuario():
    nome = input("Digite o seu nome: ")
    print(f"{nome}, você é muito firmeza!")
    
#Função com argumentos
def elogiar_usuario(nome):
    print(f"{nome}, você é muito firmeza!")

#Função com return (entra para o retorno e se faz  que quizer com o dado retornado)
def elogiar_usuario_com_retorno(nome):
   return f"{nome}, você é muito firmeza!" 

nomes = ["Rafael", "Mouse", "Teclado"]
saudacao()
for nome in nomes:
    elogiar_usuario(nome)
    
print(elogiar_usuario_com_retorno("Batman"))