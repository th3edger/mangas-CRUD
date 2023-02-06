import click
from mangas import commands as mangas_commands

MANGA_TABLE = '.mangas.csv'

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = dict()
    ctx.obj['mangas_table'] = MANGA_TABLE


cli.add_command(mangas_commands.all)