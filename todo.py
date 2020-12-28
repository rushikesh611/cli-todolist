# import Python.python.commands
from commands import commands_dict

def parse(command):
    cmd_list = command.split()
    cmd_type = cmd_list[0]
    if (cmd_type == 'help' or cmd_type == 'quit'):
        return cmd_type, []
    elif (cmd_type == 'todo'):
        cmd_name = cmd_list[1]
        if (cmd_name in ['add', 'ls', 'edit', 'del', 'done', 'report']):
            return cmd_name, cmd_list[2:]
        else:
            return 'invalid', []
    else:
        return 'invalid', []

def main():
    print('Application Started...')
    while(1):
        command = input('')
        command_type = command.split()[0]
        command_name, command_args = parse(command)
        if command_name == 'quit':
            break
        elif command_name == 'invalid':
            print('Please enter a valid command.')
        elif (command_name == 'help'):
            with open('help.txt', 'r') as help_file:
                print(help_file.read())
        elif command_type == 'todo':
            commands_dict[command_name](command_args)
        else:
            commands_dict[command_name](command_args)

if __name__ == "__main__":
    main()