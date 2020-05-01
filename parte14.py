from datetime import date, time, datetime, timedelta


def com_dateora():
    data_atual = datetime.now()
    print(data_atual.strftime('%d/%m/%Y, as %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    tupla = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta','Sabado','Domingo']
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2023, 3, 21, 6, 30, 56)
    print(data_criada)
    print(data_atual.strftime('%c'))
    data_string = '01/11/2090 15:13:09'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida + timedelta(days=36500, hours=201920)
    print(nova_data)
def so_as_data():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual_str)
    print(type(data_atual))

def so_as_ora():
    horario = time(hour=15, minute=30, second=45)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario))

if __name__ == '__main__':
    so_as_data()
    so_as_ora()
    com_dateora()
