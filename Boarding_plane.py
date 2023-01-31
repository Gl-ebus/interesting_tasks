"""
В самолете n рядов и по три кресла слева и справа в каждом ряду. Крайние кресла (A и F)
находятся у окна, центральные (C и D) – у прохода. На регистрацию приходят группы из одного,
двух или трех пассажиров. Они желают сидеть рядом, то есть на одном ряду и на одной стороне:
левой или правой. Например, группа из двух пассажиров может сесть на кресла B и C,
но не может сесть на кресла C и D, потому что они разделены проходом, а также не может сесть
на кресла A и C, потому что тогда они окажутся не рядом.
Кроме того, один из пассажиров каждой группы очень требовательный – он хочет сесть либо у окна,
либо у прохода. Конечно же, каждая группа из пассажиров хочет занять места в ряду
с как можно меньшим номером, ведь тогда они скорее выйдут из самолета после посадки.
Для каждой группы пассажиров определите, есть ли места в самолете, подходящие для них.
"""

# ----------------------Консольный ввод исходных данных-------------------------------------
n = int(input()) # число рядов
start_position = [[i for i in input().split('_')] for _ in range(n)]

m = int(input()) # количество групп пассажиров, далее m строк с описанием групп пассаж.
groups = []
for _ in range(m):
    num, side, pos = tuple(i for i in input().split())
    if pos == 'aisle':
        pos = 2 if side == 'left' else 0
    else:
        pos = 0 if side == 'left' else 2
    groups.append((int(num), 0 if side == 'left' else 1, pos)) # 0 - left, 1 - right


def take_seats(row:str, group:tuple) -> str:
    """Возращает строку левого или правого ряда с указанием занятых мест для группы символом X """

    position, side, quant_passenger  = group[2], group[1], group[0]
    if position:  # не 0
        upd_row = row[:3 - quant_passenger] + 'X' * quant_passenger
    else:  # 0
        upd_row = 'X' * quant_passenger + row[quant_passenger:]

    return upd_row


def print_save_position(new_row, side:int) -> None:
    """Вывод мест размещённых пассажиров и установка флага `занято`"""

    letters = {0: ('A', 'B', 'C'), 1: ('D', 'E', 'F')}
    index_position = start_position.index(new_row) # индекс(номер) ряда
    seat_numbers_group = tuple(filter(lambda i: new_row[side][i] == 'X', range(3)))
    seat_numbers_group = (f'{index_position + 1}{letters[side][i]}' for i in seat_numbers_group)
    print(f'Passengers can take seats:', *seat_numbers_group)

    for indx_pos in range(len(start_position)):
        print('_'.join(start_position[indx_pos]))

    start_position[index_position] = [i.replace('X', '#') for i in new_row]


for gr in groups:
    success = False
    for row in start_position:
        if (gr[0]*'.' in row[gr[1]]) and (row[gr[1]][gr[2]] == '.'):
            update_side_row = take_seats(row[gr[1]], gr)
            row.insert(gr[1], update_side_row) # вставка в ряд подходящих мест группы (gr)
            row.remove(row[gr[1]+1]) # удаление старой позиции ряда
            print_save_position(row,gr[1])
            success = True
            break
        else:
            continue
    if not success:
        print('Cannot fulfill passengers requirements')
