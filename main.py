from pyproj import Transformer

x = 'n'
while x == 'n' :
    def dms_para_decimal(graus, minutos, segundos, direcao):
        direcao = direcao.strip().upper()
        if direcao not in ['N', 'S', 'E', 'W']:
            raise ValueError(f"Direção inválida: {direcao}")
        decimal = graus + minutos / 60 + segundos / 3600
        if direcao in ['S', 'W']:
            decimal *= -1
        return decimal

    def le_dms(eixo):
        print(f'Insira {eixo} (graus, minutos, segundos, direção):')
        g = float(input('  Graus: '))
        m = float(input('  Minutos: '))
        s = float(input('  Segundos: '))
        d = input('  Direção (N/S/E/W): ')
        return dms_para_decimal(g, m, s, d)

    def main():
        try:
            lon_dec = le_dms('Longitude')
            lat_dec = le_dms('Latitude')

            # DEBUG: confirme valores antes de projetar
            print(f'[DEBUG] longitude_decimal = {lon_dec}')
            print(f'[DEBUG] latitude_decimal  = {lat_dec}')

            transformer = Transformer.from_crs('EPSG:4326', 'EPSG:31980', always_xy=True)
            # chamada posicional: primeiro longitude, depois latitude
            x, y = transformer.transform(lon_dec, lat_dec)

            print('\n' + '='*30)
            print(f'Coordenadas EPSG:31980 → X = {x:.3f}, Y = {y:.3f}')
            print('='*30)

            # salva em arquivo
            with open("resultado.txt", "w") as f:
                f.write(f"X: {x:.3f}\nY: {y:.3f}\n")
            print('[OK] Resultado salvo em resultado.txt')

        except Exception as e:
            print('[ERRO]', e)


    if __name__ == '__main__':
        main()
    x = input('Deseja sair? (s/n) \n')
    