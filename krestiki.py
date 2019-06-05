# крестики-нолики бро

# Объявление констант

# обозначение для крестика
X="X";
# обозначение для ноля
O="O";
# обозначение не занятой, пустой клетки
EMPTY=" ";
# представление ничьей
TIE="Ничья";
# кол-во клеток дя игры
NUM_SQUARES=9;

def display_instruct():
    """ Выводит инструкцию для игры """
    print("""
    Добро пожаловать в игру крестики-нолики.
    Чтобы сделать ход. введи число от 0 до 8. Числа однозначно соответствуют полям доски. как показано ниже:
    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8
    
    Приготовься к бою :)
    """);
    
def ask_yes_no(question):
    """ Задает вопрос с ответом 'Да' или 'Нет'. """
    response=None;
    while response not in ("y","n"):
        response=input(question).lower();
    return response;
    
def ask_number(question, low,high):
    """ просит ввести число из диапазона. """
    response=None;
    while response not in range(low,high):
        response=int(input(question))
    return response;
    
def pieces():
    """ определяет принадлежность первого хода """
    go_first=ask_yes_no("Хочешь оставить за собой первый ход? (y/n): ");
    if go_first=="y":
        print("\n Даю тебе фору, играй крестиками.");
        human=X;
        computer=O;
    else:
        print("Тогда начну Я");
        computer=X;
        human=O;
        
    return computer,human;
    
def new_board():
    """ Создает новую игровую доску """
    board=[];
    for square in range(NUM_SQUARES):
        board.append(EMPTY);
    return board;
    
def display_board(board):
    """ Отображает игровую ситуацию на доске """
    print("\n\t",board[0],"|",board[1],"|",board[2]);
    print("\t","-----------");
    print("\t",board[3],"|",board[4],"|",board[5]);
    print("\t","-----------");
    print("\t",board[6],"|",board[7],"|",board[8],"\n");
    
def legal_moves(board):
    """ создает список доступных ходов """
    moves=[]
    for square in range(NUM_SQUARES):
        if board[square]==EMPTY:
            moves.append(square);
    return moves;
    
def winner(board):
    """ определяет победилея в игре """
    WAYS_TO_WIN=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6));
    
    for row in WAYS_TO_WIN:
        if board[row[0]]==board[row[1]]==board[row[2]]!=EMPTY:
            winner=board[row[0]];
            return winner;
            
        if EMPTY not in board:
            return TIE;
    
    return None;
    
def human_move(board,human):
    """ получает ход человека """
    legal=legal_moves(board);
    move=None;
    
    while move not in legal:
        move=ask_number("Твой ход человек. Выбери одно из полей (0-8): ",0,NUM_SQUARES);
        if move not in legal:
            print("\n Поле занято человек! выбери другое. \n");
    print("Принято..");
    return move;
    
def computer_move(board,computer,human):
    """ делает ход за компьютер """
    #создаем копию доски, потому что ф-я будет менять значение в списке
    board=board[:]
    # поля доски по приоритетам
    BEST_MOVES=(4,0,2,6,8,1,3,5,7);
    print("Я выберу поле номер",end=" ");
    
    # проверяем в цикле свободные клетки в доске на возможность выигрыша от компьютера
    
    for move in legal_moves(board):
        board[move]=computer;
        # если следующим ходом может победить компьютер. то выберем его
        if winner(board)==computer:
            print(move);
            return move;
        # выполнив проверку. отменим внесенные изменения
        board[move]=EMPTY;
        
    # проверяем возможные ходы человека. чтобы он не выиграл следующим ходом
    for move in legal_moves(board):
        board[move]=human;
        # если следующим ходом выиграть может человек. то надо его опередить
        if winner(board)==human:
            print(move);
            return move;
        board[move]=EMPTY;
        
    # раз не нашли оптимальный ход для компьтера для немедленного выигрыша и не нашли контр-ход против человека
    # то выбираем приоритетный ход из BEST_MOVES
    
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print (move);
            return move;
            
def next_turn(turn):
    """ осуществляет перевод хода к следующему игроку """
    if turn==X:
        return O;
    else:
        return X;
        
def congrat_winner(the_winner, computer,human):
    """ поздравляем победителя """
    if the_winner!=TIE:
        print("Три", the_winner, "в ряд! \n");
    else:
        print("Ничья!\n");
    
    if the_winner==computer:
        print("КОМПЬЮТЕР победил!!! бгггга");
    elif the_winner==human:
        print("О Нет! как же ты смог меня победить, белковый\n я еще смогу победить тебя!");
    elif the_winner==TIE:
        print("Ничья! тебе повезло. ты смог ввести игру к ничье");


def main():
    """ Сборка всех функций в одну и основную логику игры """
    
    display_instruct();
    computer,human=pieces();
    turn=X
    board=new_board();
    display_board(board);
    while not winner(board):
        if turn==human:
            move=human_move(board,human);
            board[move]=human;
        else:
            move=computer_move(board,computer,human)
            board[move]=computer;
            
        display_board(board);
        turn=next_turn(turn);
        
    the_winner=winner(board);
    congrat_winner(the_winner,computer,human);

# запуск программы!

main();
input("нажмите  Enter, чтобы выйти!");
        
