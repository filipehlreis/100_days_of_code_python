from __future__ import annotations
from random import choice
from turtle import position
# from art import logo
from replit import clear
from time import sleep
"""
Using what you have learnt about Python programming, you will build a
text-based version of the Tic Tac Toe game. The game should be playable in
the command line just like the Blackjack game we created on Day 11. It should
be a 2-player game, where one person is "X" and the other plays "O".

This is a simple demonstration of how the game works:
https://www.google.com/search?q=tic+tac+toe

You can choose how you want your game to look. The simplest is to create a
game board using "|" and "_" symbols. But the design is up to you.

If you have more time, you can challenge yourself to build an AI player to
play the game with you.
"""

"""



"""

# funcoes globais


clear()

# inicializacao de variaveis globais
players = ['X', 'O']
valid_position = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
# xy
# x é linha
# y é coluna
game_should_continue = True
invalid_position = False
table_tic_tac = ['e' for _ in range(9)]
sum_table_tic_tac = ['e' for _ in range(8)]


def current_table(table_tic_tac_toe):
    table = ''

    for y in range(3):
        for x in range(3):
            if table_tic_tac_toe[y*3 + x] == 'e':
                table += '   '
            else:
                table += f' {table_tic_tac_toe[y*3 + x]} '

            if not x == 2:
                table += '|'
        if not y == 2:
            table += '\n-----------\n'

    print(table)


def is_there_a_winner(table_tic_tac):
    """
    Combinacoes para se ganhar.
    123
    456
    789

    147
    258
    369

    159
    357
    """
    sum_table_tic_tac[0] = (
        table_tic_tac[0] + table_tic_tac[1] + table_tic_tac[2])
    sum_table_tic_tac[1] = (
        table_tic_tac[3] + table_tic_tac[4] + table_tic_tac[5])
    sum_table_tic_tac[2] = (
        table_tic_tac[6] + table_tic_tac[7] + table_tic_tac[8])

    sum_table_tic_tac[3] = (
        table_tic_tac[0] + table_tic_tac[3] + table_tic_tac[6])
    sum_table_tic_tac[4] = (
        table_tic_tac[1] + table_tic_tac[4] + table_tic_tac[7])
    sum_table_tic_tac[5] = (
        table_tic_tac[2] + table_tic_tac[5] + table_tic_tac[8])

    sum_table_tic_tac[6] = (
        table_tic_tac[0] + table_tic_tac[4] + table_tic_tac[8])
    sum_table_tic_tac[7] = (
        table_tic_tac[2] + table_tic_tac[4] + table_tic_tac[6])

    # print(sum_table_tic_tac)
    if 'ooo' in sum_table_tic_tac or 'xxx' in sum_table_tic_tac:
        return True
    else:
        return False


# sortear um iniciante, X ou O
player = choice(players)

while game_should_continue:
    # inverter a vez do jogador e nao inverter caso o jogador tenha colocado
    # uma posicao invalida.
    if not invalid_position:
        if player == "X":
            player = "O"
        else:
            player = "X"
    else:
        invalid_position = False

    clear()

    # printar tabuleiro
    current_table(table_tic_tac)

    # perguntar ao outro jogador a posicao a ser jogada ou se quer desistir
    input_position = input(
        f"\n\nQual posicao que voce deseja jogar, jogador {player}?"
        f"\nDigite 'n' caso queira desistir.\n")

    # verifica se o jogador deseja sair.
    if input_position.lower() == 'n':
        game_should_continue = False
        break

    # verifica se o jogador inseriu uma posicao invalida.
    if input_position not in valid_position:
        print("\nVocê deve inserir uma posição valida! Tente novamente.")
        invalid_position = True
        sleep(1)
        continue

    # transforma um numero de xx para y
    position = [int(number) for number in input_position]
    position_index_list = 3 * position[0] + position[1]
    # print(position_index_list)

    # verifica se o usuario inseriu uma posicao livre
    if table_tic_tac[position_index_list] == 'e':
        table_tic_tac[position_index_list] = player.lower()
    else:
        print("Posicao inserida nao está livre.\nTente novamente.")
        invalid_position = True
        sleep(1)
        continue

    # printar se o jogo está ganho
    if is_there_a_winner(table_tic_tac):
        clear()
        current_table(table_tic_tac)
        print(f"\n O jogador '{player.upper()}' venceu o jogo! Parabéns!!!\n")
        game_should_continue = False
        break

    # verifica se ainda ha posicoes livres para serem jogadas
    if 'e' not in table_tic_tac:
        game_should_continue = False
        print('\n\n')
        print("### ### ### FIM ### ### ###")
        current_table(table_tic_tac)
        print("\nNão há jogadas a serem realizadas. O jogo acabou empatado.")
        break


#
#
#
#
#
