"""
Exercício 02 – Analisador de Argumentos Numéricos  (tempo aproximado 15 a 20 min)

Objetivo:
Crie uma função chamada `analisar_argumentos` que receba um número arbitrário de argumentos utilizando *args e analise quais deles são números (int ou float). A função deve retornar um dicionário com as seguintes chaves:
    - 'maior': o maior número encontrado.
    - 'menor': o menor número encontrado.
    - 'media': a média de todos os números considerados.
    - 'quantidade': a quantidade de números válidos analisados.

Requisitos:
  - Argumentos que não sejam números devem ser ignorados.
  - Se nenhum número for passado, retorne um dicionário com 'maior', 'menor' e 'media' iguais a None e 'quantidade' igual a 0.
  - Utilize estruturas condicionais e funções built-in como isinstance() para verificar os tipos.

Exemplo de uso:
    resultado = analisar_argumentos(10, "texto", 5.5, 3, [1,2], 8)
    print(resultado)
    # Saída esperada (exemplo): {'maior': 10, 'menor': 3, 'media': 6.125, 'quantidade': 4}
    
Dica: Use isinstance(x, (int, float)) para testar se x é numérico.
"""
# Sua solução aqui

analisar_argumentos =    
verificar_tipo = filter(lambda x: x if isinstance(x,(int,float)) else None, analisar_argumentos)
media = sum(verificar_tipo) / len(verificar_tipo)
quant = len(verificar_tipo)
#result = analisar_argumentos(10, "texto", 5.5, 3, [1,2], 8)
resultado = {"Maior":{max(verificar_tipo)},"Menor": {min(verificar_tipo)}, "Média": {media}, "Quantidade":{media}}
print(resultado)