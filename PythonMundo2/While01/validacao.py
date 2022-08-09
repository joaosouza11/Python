#Programa básico de validação

s = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0] 
#[0] para caso o usuário digitar, por exemplo, "feminino" o programa vai pegar apenas a letra "f"

while s not in "MF":
  s = str(input("Informação inválida. \nInforme seu sexo [M/F]: ")).strip().upper()[0]
print("Obrigado pela resposta!")