def countries_and_capitals(country: list, capital: list):
    combined = {}
    for country, capital in zip(country, capital):
        combined[country] = capital
    return combined


def result(dictionary_of_countries_capitals):
    for country, capital in dictionary_of_countries_capitals.items():
        yield f'{country} -> {capital}'


country_names = input().split(', ')
capital_names = input().split(', ')
country_capital = countries_and_capitals(country_names, capital_names)
for answer in result(country_capital):
    print(answer)