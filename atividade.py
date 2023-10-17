from random import randint

Q = []

for numero in range(20):
  Q.append(randint(1, 100))


maior = -1
menor = 101
for i in Q:
    if maior < i:
        maior = i
    if menor > i:
        menor = i


print('Lista de números:')
print(Q)
print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')

