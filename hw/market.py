from decorators import log_and_time

class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = wines
        self.beers = beers
        self.title = set(map(lambda drink: drink.title, self.wines + self.beers))

    @log_and_time
    def has_drink_with_title(self, title=None) -> bool:
        """
        Метод проверки наличия напитка с указанным title

        :return: bool
        """
        return title in self.title

    @log_and_time
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка названий напитков (вина и пива) отсортированных по title

        :return: list
        """
        sorted_drinks = sorted(self.wines + self.beers, key=lambda drink: drink.title)
        return [f"{drink.title} - {drink.production_date}" for drink in sorted_drinks]

    @staticmethod
    def _is_within_date_range(drink_date, from_date, to_date):
        return (
                (from_date is None or (drink_date is not None and drink_date >= from_date)) and
                (to_date is None or (drink_date is not None and drink_date <= to_date))
        )

    @log_and_time
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        filtered_drinks = filter(
            lambda drink: (
                self._is_within_date_range(drink.production_date, from_date, to_date)
            ),
            self.wines + self.beers
        )

        return list(map(lambda drink: f"{drink.title} - {drink.production_date}", filtered_drinks))
