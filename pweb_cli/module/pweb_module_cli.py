from ppy_common import click, Console
from pweb_cli.common.pweb_cli_named import AppRendering
from pweb_cli.module.pweb_cli_module_man import PWebCLIModuleMan

pweb_cli_module_man = PWebCLIModuleMan()


@click.group(name="module", help="PWeb Module Management CLI")
def pweb_module_cli():
    pass


@click.command(name="create", help="Create new module")
@click.option("--name", "-n", help="Module name", default=None, show_default=True, required=True)
@click.option("--version", "-v", help="Module Version", default="1.0.0", show_default=True)
@click.option("--rendering", "-r", help="Module Rendering", default=AppRendering.api, show_default=True, type=click.Choice([AppRendering.api, AppRendering.ssr, AppRendering.both], case_sensitive=False))
def create(name, version, rendering):
    try:
        pweb_cli_module_man.create_pweb_module(name=name, version=version, rendering=rendering)
    except Exception as e:
        Console.error(str(e))


pweb_module_cli.add_command(create)
