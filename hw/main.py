from wine import Wine
from beer import Beer
from market import Market

"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""
wines = [Wine(), Wine("Вино2", ), Wine(None, "2020-05-01")]
beers = [Beer(), Beer("Пиво2", ), Beer(None, "2020-03-01")]
market = Market(wines, beers)
print(market.has_drink_with_title("Вино2"))#есть такое название
print("-------")
print(market.has_drink_with_title(None)) #нет такого названия
print("-------")
print(market.get_drinks_sorted_by_title()) #сортировка по названию
print("-------")
print(market.get_drinks_by_production_date()) #нет выбранного диапазона, поэтому выводится все
print("-------")
print(market.get_drinks_by_production_date("2020-03-01", "2020-03-02")) # по диапазону
print("-------")
print(market.get_drinks_by_production_date("2020-03-01")) #нет правой границы
print("-------")
print(market.get_drinks_by_production_date(None,"2020-03-01")) #нет левой границы

