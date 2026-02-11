from colorama import Back, Fore, Style, init

init()


class Tips:
    @staticmethod
    def show_all_usage():
        print(
            f'{Back.RED + Fore.BLACK}Incorrect usage: missing arguments{Style.RESET_ALL}\n'
            f'Try writing {Fore.GREEN}"zetli add drink water"{Style.RESET_ALL} to add a new task\n'
            f'{Fore.GREEN}"zetli done 1"{Style.RESET_ALL} to delete an existing task\n'
            f'{Fore.GREEN}"zetli boom"{Style.RESET_ALL} to delete all tasks\n'
            f'{Fore.GREEN}"zetli"{Style.RESET_ALL} or {Fore.GREEN}"zetli show"{Style.RESET_ALL} to show all your added tasks'
        )

    @staticmethod
    def no_tasks():
        print(
            f'{Back.RED + Fore.BLACK}No tasks added yet!{Style.RESET_ALL}\nUse{Fore.GREEN} "zetli add new task" {Style.RESET_ALL}to add a new task.'
        )

    @staticmethod
    def no_message_after_add():
        print(f'Please enter a task after {Fore.GREEN}"zetli add"{Style.RESET_ALL}')

    @staticmethod
    def duplicate_message(id, message):
        print(f'This task: {message} already exists under id: {id}')

    @staticmethod
    def task_add_successful():
        print(f'{Fore.GREEN} Task added successfully!{Style.RESET_ALL}')

    @staticmethod
    def no_id_after_done():
        print(f'Please enter an id after {Fore.GREEN}"zetli done"{Style.RESET_ALL}')

    @staticmethod
    def all_tasks_deleted():
        print(f'{Fore.GREEN}Annihilation successful.{Style.RESET_ALL}')

    @staticmethod
    def deletion_successful(length):
        text = ''
        if length == 0:
            text = 'No more'
        elif length == 1:
            text = '1 task'
        else:
            text = f'{length} tasks'
        text += ' left.'
        print(f'Deletion successful.\n {text} ')
