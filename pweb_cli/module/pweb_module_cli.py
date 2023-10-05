from ppy_common import click


@click.group(name="module", help="PWeb Module Management CLI")
def pweb_module_cli():
    pass


@click.command(name="init", help="Initialize new module")
def init():
    pass


pweb_module_cli.add_command(init)
