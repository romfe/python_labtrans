def reps(lista):
  print("[+] A lista original é: ")
  print(lista)
  resposta = []
  contadorIgual = 0
  for item in lista:
    for item2 in lista:
      if item == item2:
        contadorIgual = contadorIgual + 1
        if contadorIgual == 2:
          if not (item2 in resposta):
            resposta.append(item2)
            contadorIgual = 0
            break
    contadorIgual = 0


  print(resposta)

reps([1, 2, 2, 3, 5, 6, 3])