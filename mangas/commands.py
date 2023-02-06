import click
from tabulate import tabulate


from mangas.services import MangaService
from mangas.models import Manga


@click.group()
def mangas():
    """Manages the mangas lifecycle"""
    pass


@mangas.command()
@click.pass_context
@click.option('-n', '--name', type=str, prompt=True, help='The Manga name')
@click.option('-v', '--manga_volume', type=int, prompt=True, help='The Manga Volume')
@click.option('-p', '--price', type=float, prompt=True, help='The Manga price')
@click.option('-pd', '--purchase_year', type=int, prompt=True, help='the year of manga"s purchase')
@click.option('-s', '--specials_or_repeat_books', type=bool, prompt=True, help='is a specials or repeat book')
def create(ctx, name, manga_volume, price, purchase_year, specials_or_repeat_books):
    """Create a new manga"""
    manga = Manga(name, manga_volume, price, purchase_year, specials_or_repeat_books)
    manga_service = MangaService(ctx.obj['mangas_table'])

    manga_service.create_manga(manga)


@mangas.command()
@click.pass_context
def list(ctx):
    """List all mangas"""
    manga_service = MangaService(ctx.obj['mangas_table'])

    mangas_list = manga_service.list_mangas()

    click.echo(tabulate(mangas_list, headers='keys', tablefmt='fancy_grid'))


@mangas.command()
@click.argument('manga_uid', type=str)
@click.pass_context
def update(ctx, manga_uid):
    """Updates a Manga Volume"""
    manga_service = MangaService(ctx.obj['mangas_table'])
    manga_list = manga_service.list_mangas()

    manga = [manga for manga in manga_list if manga['uid']==manga_uid]

    if manga:
        manga = _update_manga_flow(Manga(**manga[0]))
        manga_service.update_manga(manga)

        click.echo("Manga Updated")
    else:
        click.echo("Manga Not Found")


def _update_manga_flow(manga: Manga):
    click.echo('Leave empty if you dont want to modify the value')
    manga.name = click.prompt('New Name', type=str, default=manga.name)
    manga.manga_volume = click.prompt('New Manga Volme', type=int, default=manga.manga_volume)
    manga.price = click.prompt('New Price', type=float, default=manga.price)
    manga.purchase_year = click.prompt('New Purchase year', type=str, default=manga.purchase_year)
    manga.specials_or_repeat_books = click.prompt('True or False', type=bool, default=manga.specials_or_repeat_books)
    
    return manga



@mangas.command()
@click.argument('manga_uid', type=str)
@click.pass_context
def delete(ctx, manga_uid):
    """Deletes a Manga Volume"""
    manga_service = MangaService(ctx.obj['mangas_table'])
    mangas_list = manga_service.list_mangas()

    manga = [manga for manga in mangas_list if manga['uid'] == manga_uid]

    if manga:
        manga_service.delete_manga(manga)
        click.echo('Manga deleted')
    else:
        click.echo('Manga Not Found')


all = mangas
