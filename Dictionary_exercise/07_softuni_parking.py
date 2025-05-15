registered_users = {}

def register(user: str, licence: str) -> str:
    global registered_users

    if user not in registered_users:
        registered_users[user] = licence
        return f'{user} registered {licence} successfully'
    else:
        used_licence_plate = registered_users[user]
        return f'ERROR: already registered with plate number {used_licence_plate}'

def unregister(user: str) -> str:
    if user not in registered_users:
        return f'ERROR: user {user} not found'
    registered_users.pop(user)
    return f'{user} unregistered successfully'




number_of_commands = int(input())
for _ in range(number_of_commands):
    command = input().split()
    if len(command) == 3:
        reg_or_unreg, username, licence_plate_number = command
    else:
        reg_or_unreg, username = command

    if reg_or_unreg == 'register':
        register_car = register(username, licence_plate_number)
        print(register_car)
    elif reg_or_unreg == 'unregister':
        unregister_car = unregister(username)
        print(unregister_car)
for users, licence_plate in registered_users.items():
    print(f'{users} => {licence_plate}')