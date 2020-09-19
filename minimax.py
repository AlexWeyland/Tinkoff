import random


def empty(board):
    mas = list()
    for i in range(9):
        if (board[i] == ' '):
            mas.append(i)
    return(mas)


def printBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

def winning(board, player):
    if (
            (board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player)
    ):
        return True
    else:
        return False


def minimax(newBoard, player):
    availSpots = empty(newBoard)
    moves = []
    if player == 'X':
        plant = 'O'
    else:
        plant = 'X'
    if (winning(newBoard, 'X')):
        return ([10])
    if (winning(newBoard, 'O')):
        return ([-10])
    if len(availSpots) == 0:
        return ([0])
    for i in availSpots:
        move = []
        newBoard[i] = player
        if (player == aiPl):
            result = minimax(newBoard, huPl)
            move.append(result[0])
        else:
            result = minimax(newBoard, aiPl)
            move.append(result[0])
        move.append(i)
        newBoard[i] = ' '
        moves.append(move)
    if (player == aiPl):
        bestScore = -10000
        for i in moves:
            if (i[0] > bestScore):
                bestScore = i[0]
                bestMove = i
    else:
        bestScore = 10000
        for i in moves:
            if (i[0] < bestScore):
                bestScore = i[0]
                bestMove = i
    return bestMove


def AIplay(field):
    move = minimax(field, 'X')
    field[move[1]] = 'X'
    printBoard(field)
    a = random.choice(Tails1)
    print(a)
    return(field)


def AIplay2(field):
    massiv = empty(field)
    move = random.choice(massiv)
    field[move] = 'X'
    a = random.choice(Tails1)
    print(a)
    printBoard(field)
    return(field)


def AIplay3(field):
    massiv = empty(field)
    move = random.choice(massiv)
    field[move] = 'O'
    a = random.choice(Tails1)
    print(a)
    printBoard(field)
    return(field)


def Huplay(field):
    a = random.choice(Tails2)
    print(a)
    move = int(input())
    open = empty(field)
    flag = 0
    for x in open:
        if move == x:
            flag = 1
    if flag == 1:
        field[move] = 'O'
        printBoard(field)
        return(field)
    if flag == 0:
        print('Не хочу обидеть тебя, но ты явно что-то перепутал или перепутала. Подумай еще!')
        return(Huplay(field))


def HP2(field, player, simb):
    a = random.choice(Tails3)
    print(player, a, sep='')
    move = int(input())
    open = empty(field)
    flag = 0
    for x in open:
        if move == x:
            flag = 1
    if flag == 1:
        field[move] = simb
        printBoard(field)
        return (field)
    if flag == 0:
        print('Не хочу обидеть тебя, но ты явно что-то перепутал или перепутала. Подумай еще!')
        return (HP2(field))


def game0(field):
    count = 0
    winner = 0
    if count == 0:
        count += 1
        field[4] = 'X'
        printBoard(field)
        a = random.choice(Tails1)
        print(a)
    while(count < 9):
        field = Huplay(field)
        count += 1
        if winning(field, 'O'):
            winner = 2
            break
        field = AIplay(field)
        count += 1
        if (winning(field, 'X')):
            winner = 1
            break
    return(winner)


def game1(field, pl1, pl2):
    count = 0
    winner = 0
    while (count < 9):
        field = HP2(field, pl1, "X")
        count += 1
        if ((winning(field, 'X')) or (count == 9)):
            winner = pl1
            break
        field = HP2(field, pl2, "O")
        count += 1
        if winning(field, 'O'):
            winner = 2
            break
    return (winner)


def game2(field):
    count = 0
    winner = 0
    while (count < 9):
        field = AIplay2(field)
        count += 1
        if ((winning(field, 'X')) or (count == 9)):
            if winning(field, 'X'):
                winner = 1
            break
        field = AIplay3(field)
        count += 1
        if (winning(field, 'O')):
            winner = 2
            break
    return (winner)


theBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
Tails1 = ['Я учился играть у лучших мастеров.', 'Твои шансы лежат в малой окрестности 0.', 'Я бы пожелал удачи, но она не поможет.',
         'Хотел бы я хоть иногда ошибаться', 'Сыграем на биткоин?', 'Давай закончим это быстро', 'Моя очередь.']
Tails2 = ['Твой ход, Дружище!', 'Выбирай клетку, бро!', 'Шансов у тебя нет, но ты держись и выбирай клетку!', 'Напиши, пожалуйста, номер клетки',
          'Твоя очередь!']
Tails3 = [', твой ход!', ', выбирай клетку)', ', подумай хорошенько', ', тебе предстоит нелегкий выбор.', ', введи номер свободной клетки!',
          ', твоя очередь.', ', ходи скорее!', ', какую клетку выбираешь?']
huPl = 'O'
aiPl = 'X'
print('Привет, ты хочешь сыграть со мной или с другом?'
      '(Введи 0 или 1)')
print('Теперь доступен режим симуляции! Для выбора его введи 2.')
answer = int(input())
if answer == 0:
    print('ОК, бро. Давай попробуем! Я хожу первый)')
    win = game0(theBoard)
    if win == 0:
        print('Хорошая партия, но жаль, что безрезултативная!')
        print('НИЧЬЯ')
    if win == 1:
        print('Предсказуемый итог!')
        print('ТЫ ПРОИГРАЛ')
    if win == 2:
        print('Реальность полна разочарований даже для меня!')
        print('ТЫ ПОБЕДИЛ')
if answer == 1:
    print('Хорошо, введи пожалуста имя первого игрока!')
    player1 = input()
    print('Теперь имя второго)')
    player2 = input()
    print('Мы начинаем.')
    printBoard(theBoard)
    win = game1(theBoard, player1, player2)
    if win == 0:
        print(player1, ' ', player2, ', поздравляю вас с ничьей!', sep='')
    else:
        print(win, 'ПОБЕДИЛ!')
if answer == 2:
    print('Сейчас ты увидишь битву настоящих титанов!')
    print('Леди и джентельмены, боец в синем углы ринга, непобедимый чеспион - крестик!')
    print('Его соперник, боец в красном углу ринга, дерзкий претендент - нолик!')
    printBoard(theBoard)
    print('Мы начинаем.')
    win = game2(theBoard)
    if win == 0:
        print('Хорошая партия, но жаль, что безрезултативная!')
        print('НИЧЬЯ')
    if win == 1:
        print('Предсказуемый итог!')
        print('ЧЕМПИОН ПОБЕДИЛ!')
    if win == 2:
        print('Жизнь порой удивляет!')
        print('ПРЕТЕНДЕНТ ПОБЕДИЛ')