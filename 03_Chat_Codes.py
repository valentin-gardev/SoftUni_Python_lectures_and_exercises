num_messages = int(input())

for i in range(num_messages):
    message = int(input())
    if message == 88:
        print("Hello")
    elif message == 86:
        print("How are you?")
    elif message != 88 and message != 86 and message < 88:
        print("GREAT!")
    elif message > 88:
        print("Bye.")

