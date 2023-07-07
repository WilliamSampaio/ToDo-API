from typing import List, Dict, Any



class ToDo:
    todo: List[Dict[str, Any]] = [
        {
            'id': 1,
            'titulo': 'FastAPI :)',
            'descricao': ':)',
            'status': 'Aprendendo...',
        },
        {
            'id': 2,
            'titulo': 'Aprender python :)',
            'descricao': 'estudando!',
            'status': 'em espera...',
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
