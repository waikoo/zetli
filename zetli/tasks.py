from .storage import Storage
from .task import Task
from .tips import Tips


class Tasks:
    def __init__(self):
        self.storage = Storage()
        self.storage.setup()
        self.tips = Tips()


    def add(self, message):
        if not message:
            self.tips.no_message_after_add()
            return

        last_id = self.storage.get_last_id()
        new_id = last_id + 1
        self.storage.add(
            Task(new_id, message).to_dict()
        )


    def done(self, id_to_delete):
        if not id_to_delete:
            self.tips.no_id_after_done()
            return

        self.storage.delete_by_id(id_to_delete)
        length = self.storage.get_length_of_tasks_list()
        self.tips.deletion_successful(length)

    def show(self):
        self.storage.print()


    def delete_all(self):
        self.storage.delete_all()
        self.tips.all_tasks_deleted()
