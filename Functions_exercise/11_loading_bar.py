def loading_bar(number: int):
    loading_bar_percentage = number // 10
    return loading_bar_percentage

def result(loading_bar_number):
    loading_bar = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    if loading_bar_number != 10:
        for loading in range(loading_bar_number):
            loading_bar[loading] = '%'
        return ''.join(loading_bar), False
    else:
        for loading in range(loading_bar_number):
            loading_bar[loading] = '%'
        return ''.join(loading_bar), True



number = int(input())
loading_bar_amount = loading_bar(number)
loading_bar_percent, is_complete = result(loading_bar_amount)

if is_complete:
    print(f'{number}% Complete!\n[{loading_bar_percent}]')
else:
    print(f'{number}% [{loading_bar_percent}]\nStill loading...')