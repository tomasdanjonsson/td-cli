from sqlite3 import Error

from todo.commands.base import Command
from todo.renderers import RenderOutput
from todo.settings import config
from todo.utils import get_user_input


class EditDetails(Command):
    def run(self, id):
        try:
            todo = self._get_todo_or_raise(id)
            details = get_user_input(config["editor"], str.encode(todo[3]))
            self.service.todo.edit_details(todo[0], details)

            RenderOutput("Edited {bold}{todo_id}{reset}: {name}").render(todo_id=todo[0], name=todo[2])
        except Error as e:
            print(u'[*] Could not edit a todo due to "{}"'.format(e))