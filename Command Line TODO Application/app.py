from commands import commands_dict

# Take command as input and return the command name and arguments
def parse(command):
    cmd_list = command.split()
    cmd_type = cmd_list[0]
    if (cmd_type == 'help' or cmd_type == 'quit'):
        return cmd_type, []
    
    elif (cmd_type == 'list'):
        cmd_name = cmd_list[1]
        if (cmd_name in ['show', 'use', 'create']):
            return cmd_name, cmd_list[2:]
        else:
            return 'invalid', []
    
    elif (cmd_type == 'todo'):
        cmd_name = cmd_list[1]
        if (cmd_name in ['add', 'all', 'edit', 'remove', 'complete', 'incomplete']):
            return cmd_name, cmd_list[2:]
        else:
            return 'invalid', []
    else:
        return 'invalid', []

def main():
    print('TASKER application started sir.....')
    current_list = ''
    while (1):
        command = input() # Take the command as input from the user
        command_name, command_args = parse(command)
        # print(command_name, command_args)
        if (command_name == 'quit'):
            break

        elif (command_name == 'help'):
            with open('help.txt', 'r') as f:
                print(f.read())

        elif (command_name == 'invalid'):
            print('Please enter a valid command.\nFor help please type help.')

        elif (command_name == 'use'):
            file_name = commands_dict[command_name](command_args)
            if (file_name == -1):
                print('Please enter a valid list name.')
                current_list = ''
            else:
                print('List selection successfull.')
                current_list = file_name

        elif (command.split()[0] == 'todo'):
            command_args.insert(0, current_list)
            commands_dict[command_name](command_args)
            
        else:
            commands_dict[command_name](command_args)

if __name__ == "__main__":
    main()