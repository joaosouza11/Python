times = ("Santos", "Atlético-MG", "Corinthians", "Cuiabá", "Internacional", "Avaí", "Red Bull Bragantino", "Palmeiras", "Flamengo", "Coritiba", "São Paulo", "Botafogo", "Fluminense", "América-MG", "Ceará", "Athletico", "Atlético-GO", "Goiás", "Juventude", "Fortaleza")

primeiros = times[0:5]
print(f"\nOs 5 primeiros times da tabela são:\n{primeiros}\n")

ultimos = times[-4:]
print(f"Os 4 últimos colocados são:\n{ultimos}\n")

ordem = sorted(times)
print(f"Os times em ordem alfabética são:\n{ordem}\n")

user_escolha = str(input("Você quer saber a posição de qual time? ")).capitalize()
escolha = times.index(f"{user_escolha}")+1 #Utiliza +1 pois a primeira posição é 0
print(f"O {user_escolha} está na {escolha}° posição")