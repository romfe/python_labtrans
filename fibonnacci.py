def fibonnacci(position):
  n1 = 0
  n2 = 1
  if(position) <= 0:
    print("[-] Por favor digite um número inteiro maior do que 0")
    quit()
  for i in range(position - 1):
    fn = n1 + n2
    n1 = n2
    n2 = fn
  # Observação: o programa foi construído de acordo com as especificações do enunciado
  # no entanto, o resultado foi diferente de outras fontes consultadas. Uma delas segue:
  # https://www.omnicalculator.com/math/fibonacci
  
  print(n1)

pos = input("[+] Por favor, entre com o número para a sequência > ")
pos = int(pos)
fibonnacci(pos)
