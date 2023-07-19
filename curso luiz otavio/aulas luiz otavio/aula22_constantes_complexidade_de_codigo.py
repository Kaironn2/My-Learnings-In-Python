# CONSTANTE = "Variáveis" que não vão mudar são escritas em maiúsculo
# Muitas condições no mesmo if (ruim)
#   <- contagem de complexidade (ruim), quanto mais afastado da margem, mais complexo
# abs() -> retorna o valor absoluto do número, sem o sinal
# \ -> quebra a linha de código e continua na próxima linha

velocidade_carro = 62 # Velocidade atual do carro
local_carro = 49 # local em que o carro está na estrada

RADAR_POSICAO_INICIAL = 50
RADAR_POSICAO_FINAL = 150
RADAR_VELOCIDADE_PERMITIDA = 60
diferenca_da_velocidade_radar_carro = abs(RADAR_VELOCIDADE_PERMITIDA - velocidade_carro)

if RADAR_POSICAO_FINAL >= local_carro >= RADAR_POSICAO_INICIAL:
    if velocidade_carro > RADAR_VELOCIDADE_PERMITIDA:

        print(
            f'Você está a {velocidade_carro}km/h, acima do limite de velocidade permitido. ' 
        f'\nVocê está {diferenca_da_velocidade_radar_carro}km/h acima do permitido e será multado.'
        )
    else:
        print(f'Você está a {velocidade_carro}km/h, dentro da velocidade permitida. Boa viagem!')
else:

    if local_carro > RADAR_POSICAO_FINAL:
        print('Fique tranquilo, você já passou do alcance do radar.')
    
    elif local_carro < RADAR_POSICAO_INICIAL:
        if velocidade_carro > RADAR_VELOCIDADE_PERMITIDA:
            print(
                f'Você está a {velocidade_carro}km/h, acima do permitido.' 
                f'\nPor favor reduza a velocidade para {RADAR_VELOCIDADE_PERMITIDA}km/h para passar no radar'
                )
        else:
            print(f'Você está a {velocidade_carro}km/h, dentro da velocidade permitida'
                  f'do radar que é {RADAR_VELOCIDADE_PERMITIDA}km/h. \nMantenha a velocidade e prossiga.'
                  )
