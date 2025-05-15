def search(how_namy_searches):
    names_to_search = []
    for _ in range(how_namy_searches):
        name = input()
        names_to_search.append(name)
    for is_name_in_book in names_to_search:
        if is_name_in_book in phone_book:
            yield f'{is_name_in_book} -> {phone_book[is_name_in_book]}'
        else:
            yield f'Contact {is_name_in_book} does not exist.'


name_phone = input().split('-')
phone_book = {}

while True:
    if len(name_phone) > 1:
        phone_book[name_phone[0]] = name_phone[1]
        name_phone = input().split('-')
    else:
        search_for_names = int(''.join(name_phone))
        name_search = list(search(search_for_names))
        break
for output in name_search:
    print(output)