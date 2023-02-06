import uuid

class Manga:

    def __init__(self, name, manga_volume, price, purchase_year, specials_or_repeat_books, uid=None) -> None:
        self.name = name
        self.manga_volume = manga_volume
        self.price = price
        self.purchase_year = purchase_year
        self.specials_or_repeat_books = specials_or_repeat_books
        self.uid = uid or uuid.uuid4()

    
    def to_dict(self):
        return vars(self)


    @staticmethod
    def schema():
        return ['name','manga_volume','price', 'purchase_year', 'specials_or_repeat_books', 'uid']