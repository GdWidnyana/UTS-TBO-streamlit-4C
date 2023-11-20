class dfa():
    def __init__(self):
        self.current_state = "q0"
        self.final_state = []
        
    def addFinalState(self, states):
        for state in states:
            self.final_state.append(state)

    def addCurrentState(self, state):
        self.current_state = state

def automata(dfa, input):
    current_penjurusan = ""
    for letter in input:   
        if dfa.current_state == "q0": 
            if letter == '1':
                dfa.current_state = 'J1'
            if letter == '2':
                dfa.current_state = 'J2'
            if letter == '3':
                dfa.current_state = 'J3'
            if letter ==  '4':
                dfa.current_state = 'J4'
            if letter == '5':
                dfa.current_state = 'J5'

        elif dfa.current_state == "J1": 
            current_penjurusan = 'J1'
            if letter == '1':
                dfa.current_state = 'ALP'

        elif dfa.current_state == 'ALP': 
               if current_penjurusan in {'J1', 'J2', 'J3', 'J4', 'J5'}: 
                   if letter in {'1', '2', '3'}: 
                       if current_penjurusan == 'J1':
                           dfa.current_state = 'TBO'
                       elif current_penjurusan == 'J2':
                           dfa.current_state = 'RPL'
                       elif current_penjurusan == 'J3':
                           dfa.current_state = 'MI'
                       elif current_penjurusan == 'J4':
                           dfa.current_state = 'SDG'
                       elif current_penjurusan == 'J5':
                           dfa.current_state = 'KDJK'
                   else:
                       dfa.current_state = 'TDK'
                     

        elif dfa.current_state == 'TBO':
            if letter == '1':
                dfa.current_state = 'BD'
            else:
                dfa.current_state = 'P/S'
              

        elif dfa.current_state == 'BD': 
            if current_penjurusan == 'J1':
                if letter in {'1', '2'}:
                    dfa.current_state = 'MI'
                else:
                    dfa.current_state = 'TDK'

            elif current_penjurusan == 'J2':
                if letter in {'1', '2'}:
                    dfa.current_state = 'MI'
                else:
                    dfa.current_state = 'TDK'

            elif current_penjurusan == 'J3':
                if letter in {'1', '2'}:
                    dfa.current_state = 'SDG'
                else:
                    dfa.current_state = 'TDK'

            elif current_penjurusan == 'J4':
                if letter in {'1', '2'}:
                    dfa.current_state = 'MI'
                else:
                    dfa.current_state = 'TDK'
        
        elif dfa.current_state == 'MI':
            if current_penjurusan == 'J1':
                if letter in {'1', '2'}:
                    dfa.current_state = 'SD'
                else:
                    dfa.current_state = 'TDK'

            elif current_penjurusan == 'J2':
                if letter in {'1', '2'}:
                    dfa.current_state = 'SD'
                else:
                    dfa.current_state = 'TDK'
                    
            elif current_penjurusan == 'J3':
                if letter == '1':
                    dfa.current_state = 'BD'
                else:
                    dfa.current_state = 'P/S'
                
            elif current_penjurusan == 'J4':
                if letter in {'1', '2'}:
                    dfa.current_state = 'SD'
                else:
                    dfa.current_state = 'TDK'

            elif current_penjurusan == 'J5':
                if letter in {'1', '2'}:
                    dfa.current_state = 'MD2'
                else:
                    dfa.current_state = 'TDK'
        
        elif dfa.current_state == 'SD':
            if current_penjurusan == 'J1':
                if letter in {'1', '2'}:
                    dfa.current_state = 'MD1'
                else:
                    dfa.current_state = 'TDK'
            
            elif current_penjurusan == 'J2':
                if letter in {'1', '2'}:
                    dfa.current_state = 'DAA'
                else:
                    dfa.current_state = 'TDK'

            elif current_penjurusan == 'J4':
                if letter in {'1', '2'}:
                    dfa.current_state = 'SO'
                else:
                    dfa.current_state = 'TDK'

        elif dfa.current_state == 'MD1':
            if current_penjurusan == 'J1':
                if letter in {'1', '2'}:
                    dfa.current_state = 'ACC'
                else:
                    dfa.current_state = 'TDK'
            if current_penjurusan == 'J3':
                if letter in {'1', '2'}:
                    dfa.current_state = 'ACC'
                else:
                    dfa.current_state = 'TDK'

        elif dfa.current_state == 'P/S':
            if letter == 'T':
                dfa.current_state = 'TDK'
            if current_penjurusan in {'J1', 'J2', 'J3', 'J4'}:
                if letter == 'Y':
                    dfa.current_state = 'BD'
            else:
                if letter == 'Y':
                    dfa.current_state = 'RPL'

# =================================================================
        #Penjaluran 2
        elif dfa.current_state == "J2": 
            current_penjurusan = 'J2'
            if letter == '2':
                dfa.current_state = 'ALP'

        elif dfa.current_state == 'RPL': 
            if current_penjurusan == 'J2':
                if letter == '1':
                    dfa.current_state = 'BD'
                else:
                    dfa.current_state = 'P/S'
            if current_penjurusan == 'J5':
                if letter in {'1', '2'}:
                    dfa.current_state = 'MI'
                else:
                    dfa.current_state = 'TDK'

        elif dfa.current_state == 'DAA':
            if current_penjurusan == 'J2':
                if letter in {'1', '2'}:
                    dfa.current_state = 'ACC'
                else:
                    dfa.current_state = 'TDK'
            if current_penjurusan == 'J3':
                if letter in {'1', '2'}:
                    dfa.current_state = 'MD1'
                else:
                    dfa.current_state = 'TDK'
                    
# =================================================================
        #Penjaluran 3

        elif dfa.current_state == 'J3': # State sekarang adalah j3
            current_penjurusan = 'J3'
            if letter == '3':
                dfa.current_state = 'ALP'

        elif dfa.current_state == 'SDG':
            
            if current_penjurusan == 'J3':
                if letter in {'1', '2'}:
                    dfa.current_state = 'DAA'
                else:
                    dfa.current_state = 'TDK'
            if current_penjurusan == 'J4':
                if letter in {'1'}:
                    dfa.current_state = 'BD'
                else:
                    dfa.current_state = 'TDK'    
    
# =================================================================
        #Penjaluran 4

        elif dfa.current_state == "J4": 
            current_penjurusan = 'J4'
            if letter == '4':
                dfa.current_state = 'ALP'

        elif dfa.current_state == 'SDG': # State sekarang adalah TBO
            if letter == '1':
                dfa.current_state = 'BD'
            else:
                dfa.current_state = 'P/S'

        elif dfa.current_state == 'SO':
            if current_penjurusan == 'J4':
                if letter in {'1', '2'}:
                    dfa.current_state = 'ACC'
                else:
                    dfa.current_state = 'TDK'
            if current_penjurusan == 'J5':
                if letter in {'1', '2'}:
                    dfa.current_state = 'ACC'
                else:
                    dfa.current_state = 'TDK'

# =================================================================
        #Penjaluran 5
        elif dfa.current_state == "J5": # State sekarang adalah j1
            current_penjurusan = 'J5'
            if letter == '5':
                dfa.current_state = 'ALP'

        elif dfa.current_state == 'KDJK': # State sekarang adalah KDJK
            if letter == '1':
                dfa.current_state = 'RPL'
            else:
                dfa.current_state = 'P/S'

        elif dfa.current_state == 'RPL': # State sekarang adalah RPL
            if current_penjurusan == 'J5':
                if letter in {'1', '2'}:
                    dfa.current_state = 'MI'
                else:
                    dfa.current_state = 'TDK'
        
        elif dfa.current_state == 'MD2':
            if current_penjurusan == 'J5':
                if letter in {'1', '2'}:
                    dfa.current_state = 'SO'
                else:
                    dfa.current_state = 'TDK'
                    
        elif dfa.current_state == 'P/S':
            if letter == 'T':
                dfa.current_state = 'TDK'
            if current_penjurusan in {'J1', 'J2', 'J3', 'J4'}:
                if letter == 'Y':
                    dfa.current_state = 'BD'
            else:
                if letter == 'Y':
                    dfa.current_state = 'RPL'
  
        
    if dfa.current_state == 'ACC':
        return True
    elif dfa.current_state == 'TDK':
        return False
    else:
        return None
    
if __name__ == '__main__':
    a = dfa()
    a.addFinalState("ACC")
    input_string = input("Masukkan string nilai mata kuliah dan sertifikat (contoh: 3322Y21111): ")
    result = automata(a, input_string)
    if result == True:
        print("Terima")
    elif result == False:
        print("Tolak")
    else:
        print("Input Illegal")