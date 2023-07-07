from enum import Enum
from typing import Any, Dict, List


class StatusOption(str, Enum):
    to_do = 'To Do'
    doing = 'Doing'
    finished = 'Finished'
    canceled = 'Canceled'


class ToDo:
    todo: List[Dict[str, Any]] = [
        {
            'id': 1,
            'titulo': 'FastAPI :)',
            'descricao': ':)',
            'status': StatusOption.to_do,
        },
        {
            'id': 2,
            'titulo': 'Aprender python :)',
            'descricao': 'estudando!',
            'status': StatusOption.doing,
        },
    ]

    current_id = 2

    def list(self):
        return self.todo

    def add(self, item: Dict[str, Any]) -> Dict[str, Any]:
        self.current_id += 1
        item['id'] = self.current_id
        self.todo.append(item)
        return item

    def get(self, id: int) -> Dict[str, Any] | None:
        for item in self.todo:
            if item['id'] == id:
                return item
