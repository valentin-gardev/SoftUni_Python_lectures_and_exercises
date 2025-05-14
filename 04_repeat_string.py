# def getting_string():
#     string = input()
#     return string
#
# def repeat_string():
#     repeat = int(input())
#     return repeat
#
#
# print(getting_string() * repeat_string())


repeat_string = lambda string, how_many_repeats: string * how_many_repeats

string = input()
how_many_repeats = int(input())
print(repeat_string(string, how_many_repeats))