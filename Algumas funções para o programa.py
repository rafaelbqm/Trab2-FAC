def dec_to_bin(x):
    return int(bin(x)[2:])#Função que retorna o valor binário de um numero decimal.

def expoentebin(entrada):#Função que retorna o expoente em binário já com o excesso de 127.
    nbin=entrada.split(',')
    r=(len(nbin[0])-1)+127
    return dec_to_bin(r)

def virgula(entrada): #Função move a virgula para a primeira casa e retorna a string.
    r=entrada.split(',')
    r=r[0]+r[1]
    r=r[0]+','+r[1:]
    return r

def verifica_sinal(entrada):
    if entrada[0]=='-':
        return 1;
    else:
        return 0;

def casos_especiais(entrada): #Imprime no formato IEEE754 e Retorna True se for um caso especial.
    if entrada=='0' or entrada=='+0':
        print('SINAL: 0 EXPOENTE: 00000000 MANTISSA: 00000000000000000000000')
        return True
    elif entrada=='-0':
        print('SINAL: 1 EXPOENTE: 00000000 MANTISSA: 00000000000000000000000')
        return True
    elif entrada=='+inf':
        print('SINAL: 0 EXPOENTE: 11111111 MANTISSA: 00000000000000000000000')
        return True
    elif entrada=='-inf':
        print('SINAL: 1 EXPOENTE: 11111111 MANTISSA: 00000000000000000000000')
        return True
    else:
        return False
