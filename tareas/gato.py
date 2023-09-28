class Gato:
    def __init__(self):
        self.A=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        
    def print_state(self):
        ''' Muestra el estado del juego
        '''
        print("    A   B   C  ")
        print("  ┏━━━┯━━━┯━━━┓")
        print("1 ┃ {} │ {} │ {} ┃".format(self.A[0][0],self.A[0][1],self.A[0][2]))
        print("  ┠───┼───┼───┨")
        print("2 ┃ {} │ {} │ {} ┃".format(self.A[1][0],self.A[1][1],self.A[1][2]))
        print("  ┠───┼───┼───┨")
        print("3 ┃ {} │ {} │ {} ┃".format(self.A[2][0],self.A[2][1],self.A[2][2]))
        print("  ┗━━━┷━━━┷━━━┛")

    def casillas_disponibles(self):
        ''' Regresa un conjunto con las casillas disponibles
        '''
        disponibles = set()
        for i in range(3):
            for (j,letra) in zip(range(3),'ABC'):
                if self.A[i][j] == ' ':
                    disponibles.add(str(i+1)+letra)
        return disponibles
        
    def casilla_vacia(self, a):
        '''Revisa si la posición a se puede seleccionar, regresa un booleano
        '''
        return len(a) == 2 and a[0] in ['1', '2', '3'] and a[1] in ['A','B','C'] and a in self.casillas_disponibles()
        
    def movimiento_jugador1(self,a):
        ''' cambia el estado de la posicion a a x
        '''
        posicion = a.strip()
        y = -1
        x = -1
        if posicion[1] == 'A':
            y = 0
        elif posicion[1] == 'B':
            y = 1
        elif posicion[1] == 'C':
            y = 2
        x = int(posicion[0]) - 1
        self.A[x][y] = 'x'

    def movimiento_jugador2(self,a):
        '''cambia el estado de la posicion a a o
        '''
        posicion = a.strip()
        y = -1
        x = -1
        if posicion[1] == 'A':
            y = 0
        elif posicion[1] == 'B':
            y = 1
        elif posicion[1] == 'C':
            y = 2
        x = int(posicion[0]) - 1
        self.A[x][y] = 'o'
            
    def continua(self):
        '''revisa si el juego continua o no, regresa un booleano
        '''
        
        for i in range(3):
            renglon = str(self.A[i][0]) + str(self.A[i][1]) + str(self.A[i][2])
            columna = str(self.A[0][i]) + str(self.A[1][i]) + str(self.A[2][i])           
            if renglon in ['xxx','ooo'] or columna in ['xxx','ooo']:
                return False
                
        diagonal1 = str(self.A[0][0]) + str(self.A[1][1]) + str(self.A[2][2])
        diagonal2 = str(self.A[0][2]) + str(self.A[1][1]) + str(self.A[2][0])
        
        if diagonal1 in ['xxx','ooo'] or diagonal2 in ['xxx','ooo']:
            return False
            
        if not ' ' in self.A[0] + self.A[1] + self.A[2]:
            return False
            
        return True
        
    def quien_gano(self):
        '''Regresa un string indicando quien gano
        '''
        for i in range(3):
            renglon = str(self.A[i][0]) + str(self.A[i][1]) + str(self.A[i][2])
            columna = str(self.A[0][i]) + str(self.A[1][i]) + str(self.A[2][i])           
            if renglon == 'xxx' or columna == 'xxx':
                return 'Jugador'
            if renglon == 'ooo' or columna == 'ooo':
                return 'Maquina'
                
        diagonal1 = str(self.A[0][0]) + str(self.A[1][1]) + str(self.A[2][2])
        diagonal2 = str(self.A[0][2]) + str(self.A[1][1]) + str(self.A[2][0])
        
        if diagonal1 == 'xxx' or diagonal2 == 'xxx':
            return 'Jugador'
        if diagonal1 == 'ooo' or diagonal2 == 'ooo':
            return 'Maquina'
            
        return 'Nadie'
        
    def restart(self):
        '''Reinicia todas las casillas
        '''
        self.A = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

            