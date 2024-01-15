class Wine:
    _next_index = 1

    def __init__(self, title=None, production_date=None) -> None:
        self.title = f"НЛО Вино {Wine._next_index}" if title is None else title
        self.production_date = production_date
        self.index = Wine._next_index
        if title is None:
            Wine._next_index += 1

        # TODO: добавить инициализацию

