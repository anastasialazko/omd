def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. ️\n '
        ' Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

def step2_umbrella():
    print(
        'Утка-маляр 🦆 решила взять зонтик. ️\n '
        ' Утку-маляра 🦆 пугал солнечный удар. ️\n  '
        'Утка-маляр 🦆 идет одна в бар? ️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return \
            print(
                'Хотя за окном льет весь день дождик. ️\n '
                'Утка-маляр 🦆 идет одна в бар, ️\n '
                'Хотя солнечный удар ее все же тревожит'
    )
    return print(

        'А от ливня на крыльце спасался мокрый котик. ️\n '
        'Утка и кот решили вместе идти в бар - \n '
        'На брудершафт выпить компотик!'
    )
def step2_no_umbrella():
    print(
        'Утка-маляр 🦆 решила не брать с собой зонтик. ️\n '
        'Утку-маляра 🦆 не испугал солнечный удар. ️\n '
        'Потому что за окном шел проливной дождик. ️\n '
        'Дойдет ли утка-маляр 🦆 в бар? ️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return \
           print ('Мокрая утка-маляр 🦆 пришла в любимый бар. ️️\n '
                  'Утка жалеет, что забыла дома зонтик.')
    return print ('На утку-маляра 🦆 опустился туман, ️️\n '
                  'Утка-маляр 🦆 не видит бар на горизонте.')


if __name__ == '__main__':
    step1()
