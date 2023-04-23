a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(  # Ponto ao termino do string mostram todas as ações deste objeto. Neste caso é um formato.
    nome1=a, nome2=b, nome3=c # A, B, C são argumentos e o nome1 é parametro.
)
   
print(formato)