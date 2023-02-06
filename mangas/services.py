import csv
import os

from mangas.models import Manga


class MangaService:

    def __init__(self, table_name) -> None:
        self.table_name = table_name
    

    def create_manga(self, manga: Manga):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Manga.schema())
            writer.writerow(manga.to_dict())


    def list_mangas(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Manga.schema())

            return list(reader)


    def update_manga(self, updated_manga: Manga):
        mangas = self.list_mangas()

        updated_mangas = list()
        for manga in mangas:
            if manga['uid'] == updated_manga.uid:
                updated_mangas.append(updated_manga.to_dict())
            else:
                updated_mangas.append(manga)

        self._save_to_disk(updated_mangas)


    def delete_manga(self, manga: Manga):
        mangas_list = self.list_mangas()
        mangas_list.remove(manga[0])

        self._save_to_disk(mangas_list)


    def _save_to_disk(self, mangas):
        tmp_table_name = self.table_name + '.tmp'

        with open(tmp_table_name, mode='a') as f:
            writter = csv.DictWriter(f, fieldnames=Manga.schema())
            writter.writerows(mangas)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)