from sqlite3 import Error

from todo.commands.base import Command
from todo.renderers import RenderOutput


class Uncomplete(Command):
    def run(self, id):
        try:
            todo = self._get_todo_or_raise(id)
            self.service.todo.uncomplete(todo[0])
            RenderOutput("{bold}{red}x {reset}{todo_id}{normal}: {name}").render(todo_id=todo[0], name=todo[2])
        except Error as e:
            print(u'[*] Could not uncomplete a todo due to "{}"'.format(e))
