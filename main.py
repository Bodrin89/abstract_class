
from classes.all_classes import Storage, Shop, Store, Request




shop = Shop({'печеньки': 3,
             'собачки': 2}, 0)
store = Store({'печеньки': 30,
             'собачки': 40}, 0)

def main():
    while True:
        user_input = input('ввести строку формата "Доставить 3 печеньки из склад в магазин"\n')
        if user_input in ('stop', 'стоп'):
            break
        request = Request(user_input)

        def work_store(product, amount):
            if request.from_ == 'склад':
                return store.remove(product, amount), shop.add(product, amount)
            return store.add(product, amount), shop.remove(product, amount)
        print(work_store(request.product, request.amount))


if __name__ == "__main__":
    main()