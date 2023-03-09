while True:	# Programa roda num loop eternamente até ser quebrado. (Linha 110)
	import numpy as np
	import random
	import os
	os.system("cls") # Limpa console

	tabuleiro = [[" " for i in range(3)] for j in range(3)] # Define o tabuleiro como um Array de 3 colunas e 3 linhas
	jogo = 1 # Declarando variáveis
	jogoAI = 1

	def preenchido(col, row): # Função para detectar se uma célula foi preenchida
		if tabuleiro[col][row] == "X" or tabuleiro[col][row] == "O":
			return True
		else:
			return False

	def turnoPlayer(jogo): # Turno do Jogador
		printTabuleiro()
		
		if checkVitoria() == 1:
			return False
		try:
			jogo = int(input("Jogue com um número de 1 a 9: "))
		except ValueError:
			print("Você deve jogar com um número de 1 a 9.")
			turnoPlayer(jogo)

		if jogo < 1 or jogo > 9:
			try:
				jogo = int(input("Jogue com um número de 1 a 9: "))
			except ValueError:
				print("Você deve jogar com um número de 1 a 9.")
				turnoPlayer(jogo)
		elif jogo <= 3:
			if preenchido(0, jogo - 1):
				print("Esse espaço já foi preenchido.")
			else:
				tabuleiro[0][jogo - 1] = "X"
				turnoAI(jogoAI)
		elif jogo <= 6:
			if preenchido(1, jogo - 3 - 1):
				print("Esse espaço já foi preenchido.")
			else:
				tabuleiro[1][jogo - 3 - 1] = "X"
				turnoAI(jogoAI)
		elif jogo <= 9:
			if preenchido(2, jogo - 6 - 1):
				print("Esse espaço já foi preenchido.")
			else:
				tabuleiro[2][jogo - 6 - 1] = "X"
				turnoAI(jogoAI)

		turnoPlayer(jogo) # Caso as condições falhem, roda o turno do jogador novamente

	def turnoAI(jogoAI): # Turno do Computador
		jogoAI = random.randint(1,9)
		if checkVitoria() == 1:
			return False

		if jogoAI <= 3:
			if not preenchido(0, jogoAI - 1):
				tabuleiro[0][jogoAI - 1] = "O"
				return False # Sai da função, e troca para o turno do Jogador (Linha 106)
		elif jogoAI <= 6:
			if not preenchido(1, jogoAI - 3 - 1):
				tabuleiro[1][jogoAI - 3 - 1] = "O"
				return False
		elif jogoAI <= 9:
			if not preenchido(2, jogoAI - 6 - 1):
				tabuleiro[2][jogoAI - 6 - 1] = "O"
				return False

		turnoAI(jogoAI) # Se as condições falharem, roda o turno do Computador novamente

	def printTabuleiro():  # Mostra o tabuleiro de forma legal
		print("")
		print("=========")
		print(tabuleiro[0][0],"|",tabuleiro[0][1],"|",tabuleiro[0][2])
		print("=========")
		print(tabuleiro[1][0],"|",tabuleiro[1][1],"|",tabuleiro[1][2])
		print("=========")
		print(tabuleiro[2][0],"|",tabuleiro[2][1],"|",tabuleiro[2][2])
		print("=========")

	def checkRows(tabuleiro): # Função para detectar se a linha foi preenchida (Cr: Efferalgan)
		for row in tabuleiro:
			if len(set(row)) == 1:
				return row[0]
		return 0 

	def checkDiagonals(tabuleiro): # Função para detectar se a diagonal/coluna foi preenchida (Cr: Efferalgan)
		if len(set([tabuleiro[i][i] for i in range(len(tabuleiro))])) == 1:
			return tabuleiro[0][0]
		if len(set([tabuleiro[i][len(tabuleiro)-i-1] for i in range(len(tabuleiro))])) == 1:
			return tabuleiro[0][len(tabuleiro)-1]
		return 0 

	def checkWin(tabuleiro):  # Função para detectar se houve vencedor (Cr: Efferalgan)
		#transposition to check rows, then columns
		for newtabuleiro in [tabuleiro, np.transpose(tabuleiro)]:
			result = checkRows(newtabuleiro)
			if result:
				return result
		return checkDiagonals(tabuleiro)

	def checkVitoria(): # Função para detectar quem venceu
		if checkWin(tabuleiro) == "X":
			print("")
			print("Você venceu! :D")
			return True
		elif checkWin(tabuleiro) == "O":
			print("")
			print("Você perdeu. :(")
			return True
		elif all([cell != " " for row in tabuleiro for cell in row]):
			print("Velha!!!") # Demorei muito pra conseguir fazer isso aqui kkkkk
			return True
		else:
			return False
	
	turnoPlayer(jogo) # Roda o turno do jogador pela primeira vez

	jogonovo = input("Deseja jogar novamente? [S/N]: ") # Pergunta ao usuário se quer jogar novamente. Se não, quebra o loop eterno e fecha o programa
	if jogonovo.upper() != "S":
		break