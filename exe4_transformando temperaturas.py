while True:
    print('Qual temperatura deseja ver:\n'
          '[1] ºC para ºF\n'
          '[2] ºF para ºC')
    resp = int(input('Resposta: '))
    if resp == 1:
        tc = float(input('Digite a temperatura em ºC: '))
        tf = tc * 9 / 5 +32
        print(f'A temperatura de {tc}ºC, são {tf:.1f}ºF.')
        break
    else:
        tf = float(input('Digite a temperatura em ºF: '))
        tc = (tf - 32) / 1.8
        print(f'A temperatura de {tf}ºF, são {tc:.1f}ºC.')
        break
