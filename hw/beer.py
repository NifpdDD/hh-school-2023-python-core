class Beer:
    _next_index = 1

    def __init__(self, title=None, production_date=None) -> None:
        self.title = f"НЛО Пиво {Beer._next_index}" if title is None else title
        self.production_date = production_date
        self.index = Beer._next_index
        if title is None:
            Beer._next_index += 1
        # TODO: добавить остальную инициализацию