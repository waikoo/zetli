import json
import os
from pathlib import Path

from zetli.tips import Tips


class Storage:
    def __init__(self):
        self.app_folder = Path(user_data_dir("zetli"))
        self.app_folder = self.appdata_path / 'zetli'
        self.tasks_file = self.app_folder / 'tasks.json'
        self.app_folder.mkdir(parents=True, exist_ok=True)
        self.tips = Tips()

    @staticmethod
    def get_starter_content():
        return {
            "last_id": 0,
            "tasks": []
        }

    def setup(self):
        if not self.app_folder.exists():
            self.app_folder.mkdir(parents=True, exist_ok=True)
            if not self.tasks_file.exists():
                import json
                with self.tasks_file.open('w', encoding='utf-8') as file:
                    json.dump(self.get_starter_content(), file, indent=2)


    def print(self):
        with self.tasks_file.open('r') as file:
            contents = json.load(file)
            if len(contents['tasks']) == 0:
                self.tips.no_tasks()
                return
            for task in contents['tasks']:
                print(f'{task['id']} {task['message']}')


    def add(self, message_with_id):
        if not self.is_new_message_a_duplicate(message_with_id):
            tasks_contents = None
            with self.tasks_file.open('r') as file:
                tasks_contents = json.load(file)
            tasks_contents['last_id'] += 1
            tasks_contents['tasks'].append(message_with_id)
            with self.tasks_file.open('w') as file:
                json.dump(tasks_contents, file, indent=2)
            self.tips.task_add_successful()



    def is_new_message_a_duplicate(self, message_with_id):
        message = message_with_id['message']
        duplicate_id = self.message_exists(message)

        if duplicate_id is not None:
            self.tips.duplicate_message(duplicate_id, message)
            return True

        return False


    def message_exists(self, message):
        with self.tasks_file.open('r') as file:
            contents = json.load(file)
            tasks = contents['tasks']

            duplicate = next(
                (task for task in tasks if task["message"] == message),
                None
            )

            if duplicate:
                return duplicate["id"]

            return None


    def get_last_id(self):
        with self.tasks_file.open('r') as file:
            return json.load(file)['last_id']


    def delete_by_id(self, id_to_delete):
        contents = None
        with self.tasks_file.open('r') as file:
            contents = json.load(file)
        for task in contents['tasks']:
            if task['id'] == int(id_to_delete):
                contents['tasks'].remove(task)
                break
        with self.tasks_file.open('w') as file:
            json.dump(contents, file, indent=2)


    def delete_all(self):
        with self.tasks_file.open('w') as file:
            json.dump(self.get_starter_content(), file, indent=2)


    def get_length_of_tasks_list(self):
        with self.tasks_file.open('r') as file:
            return len(json.load(file)['tasks'])
