times = (
    "Botafogo",
    "Palmeiras",
    "Flamengo",
    "Fortaleza",
    "Internacional",
    "São Paulo",
    "Corinthians",
    "Bahia",
    "Cruzeiro",
    "Vasco da Gama",
    "Vitória",
    "Atlético Mineiro",
    "Fluminense",
    "Grêmio",
    "Juventude",
    "Red Bull Bragantino",
    "Athletico Paranaense",
    "Criciúma",
    "Atlético Goianiense",
    "Cuiabá",
)

print(f"Lista dos times do Brasileirão 2025: {times}")

print('-='*10)

print(f'Os cinco primeiros são: {times[:5]}')

print('-='*10)

print(f'Os cinco ultimos são: {times[-5 : ]}')

print('-='*10)

print(f'Os times em ordem alfabetica é: {sorted(times)}')

print('-='*10)

print(f'O Grêmio está na {times.index("Grêmio")+1} posição')