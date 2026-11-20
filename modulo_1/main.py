"""
# PROJETO 1 — PROMPT PACKER (BÁSICO)

## Criar um programa que recebe (via terminal):
- role
- tom de voz
- tarefa
- número máximo de palavras

## Regras obrigatórias:
- O programa deve montar um prompt final usando f-strings, no formato:
  - Role: ...
  - Tom de voz: ...
  - Tarefa: ...
  - Instruções: ...
- O programa deve estimar a quantidade de palavras do prompt final usando a heurística:
  - 1 palavra ≈ 6.11 caracteres
- O programa deve checar se a quantidade estimada de palavras ficou dentro de uma faixa aceitável:
  - entre (máximo de palavras - 10) e (máximo de palavras + 10)

## Esse programa deve retornar:
- prompt final (string)
- quantidade de palavras estimada (float ou int)
- está dentro do intervalo aceitável? (bool)
"""


#recebendo entradas do usuários

role = input("digite o cargo:")
tom_de_voz =  input("tom de voz")
tarefa = input("digite a tarefa")
numero_máximo_de_palavras = int(input("digite o numero maximo de palavras: "))


#montando o prompt


Final = f"""- {role}: 
  - {tom_de_voz}: 
  - {tarefa}: 
  - Instruções: """

maximo_c = len(Final)
maximo_p = maximo_c / 6.11



#ta dentro do intervalo confiavel?
 intervalo = (numero_máximo_de_palavras - 10 <= maximo_p <= numero_máximo_de_palavras + 10)




#exibição
print(Final)
print(intervalo)
print(maximo_c)







