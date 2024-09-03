# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, 
# informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


def a_fibonacci(n):
    # Função para verificar se um número pertence à sequência de Fibonacci
    
    # Sequência inicial
    fib_sequencia = [0, 1]
    
    # Gerar a sequência de Fibonacci até que o último número seja maior ou igual a n
    while fib_sequencia[-1] < n:
        next_fib = fib_sequencia[-1] + fib_sequencia[-2]
        fib_sequencia.append(next_fib)
    
    # Verificar se o número informado está na sequência
    if n in fib_sequencia:
        return f"O número {n} pertence à sequência de Fibonacci!"
    else:
        return f"O número {n} ~~não~~ pertence à sequência de Fibonacci."

# Solicitar um número ao usuário
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Chamar a função e exibir o resultado
resultado = a_fibonacci(numero)
print(resultado)