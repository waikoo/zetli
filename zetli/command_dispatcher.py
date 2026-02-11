from zetli.tips import Tips
from .tasks import Tasks

class CommandDispatcher:
    def __init__(self, argv):
        self.argv = argv

    def run(self):
        tasks = Tasks()

        if len(self.argv) < 2:
            tasks.show()
            return

        _, command, *rest = self.argv
        all_the_rest = ' '.join(rest)

        match command:
            case 'add':
                tasks.add(all_the_rest)
            case 'done':
                tasks.done(all_the_rest)
            case 'show':
                tasks.show()
            case 'boom':
                tasks.delete_all()
            case _:
                Tips().show_all_usage()




