from typing import Any
from datetime import datetime


def op_resolver(source: Any, target: Any, op: str):
    if op == "eq":
        return source == target
    elif op == "ne":
        return source != target
    elif op == "gt":
        return source > target
    elif op == "gte":
        return source >= target
    elif op == "lt":
        return source < target
    elif op == "lte":
        return source <= target
    else:
        raise ValueError("Unsupported Operation")


class Product:
    def __init__(
        self,
        title: str = None,
        description: str = None,
        price: float = None,
        available_date: datetime = None,
        stock_quantity: int = None,
        product_images: list[str] = None,
        category: str = None,
        is_promoted: bool = None,
    ):
        self.title = title
        self.description = description
        self.price = price
        self.available_date = available_date
        self.stock_quantity = stock_quantity
        self.product_images = product_images
        self.category = category
        self.is_promoted = is_promoted

    def __repr__(self) -> str:
        prepared_str = ",".join(
            ['{k}="{v}"'.format(k=k, v=v) for k, v in self.__dict__.items()]
        )
        return "{}({})".format(type(self).__name__, prepared_str)


class BaseWarehouse:
    def __init__(self, products: list[Product] = None):
        self.products = products

    def search(self, query: str) -> list:
        q = query.lower()
        search_with_title = lambda p: p.title.lower().startswith(q)
        search_with_description = lambda p: q in p.description.lower()
        return list(filter(search_with_title, self.products)) + list(
            filter(search_with_description, self.products)
        )

    def filter(self, field_name: str, op: str, value: Any) -> list:
        return list(
            filter(
                lambda p: op_resolver(getattr(p, field_name), value, op=op),
                self.products,
            )
        )

    def order_by(
        self,
        products: list[Product],
        field_name: str = "available_date",
        ascending: bool = True,
    ) -> list:
        return list(
            sorted(
                products,
                key=lambda p: getattr(p, field_name),
                reverse=not ascending,
            )
        )


class StoreFront(BaseWarehouse):
    def get_promotion_products(self) -> list:
        return self.filter("is_promoted", "eq", True)

    def get_catalogs(self) -> list:
        return list(set(each.category for each in self.products))

    def get_products_by_catalog(self, catalog: str) -> list:
        return self.filter("category", "eq", catalog)


class MicroStore(BaseWarehouse):
    def get_available_products(self) -> list:
        return self.filter("stock_quantity", "gt", 0)


if __name__ == "__main__":
    import random

    products = [
        Product(
            title=f"Product {i}",
            stock_quantity=random.randint(0, 10),
            available_date=datetime.now(),
            price=random.randint(100, 500),
            category=random.choice(
                ["life style", "technology", "sports", "travel", "home"]
            ),
            is_promoted=random.choice([True, False]),
        )
        for i in range(1, 21)
    ]
    sf1 = StoreFront(products=products[:10])
    ms1 = MicroStore(products=products[11:])

    print(f"Generated products: {len(products)}")
    print(products)

    print("STORE FRONT >>>")
    print(f"  All Products ({len(sf1.products)}) ...")
    print(sf1.products)

    promotion_products = sf1.get_promotion_products()
    print(f"  Promotions ({len(promotion_products)}) ...")
    print(promotion_products)

    available_catalogs = sf1.get_catalogs()
    print(f"  Catalogs ({available_catalogs}) ...")
    print(available_catalogs)

    current_catalog = available_catalogs[-1]
    items_by_catalog = sf1.get_products_by_catalog(current_catalog)
    print(
        f"  Products in Catalog: {current_catalog} ({len(items_by_catalog)}) ..."
    )
    print(items_by_catalog)

    print("")
    print("MICROSTORE ###")
    print(f"  All Products ({len(ms1.products)}) ...")
    print(ms1.products)

    available_products = ms1.get_available_products()
    print(f"  Available Products ({len(available_products)}) ...")
    print(available_products)
