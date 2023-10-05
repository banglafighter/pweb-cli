from ppy_common import Console, click
from pweb_cli.module.pweb_module_cli import pweb_module_cli
from pweb_cli.prod.pweb_prod_cli import pweb_prod_cli
from pweb_cli.project.pweb_project_cli import pweb_project_cli

Console.blue("--------------------------------", bold=True)
Console.green("      PWeb Source Manager      ", bold=True)
Console.blue("--------------------------------", bold=True)


@click.group()
def pweb_cli_bsw():
    pass


pweb_cli_bsw.add_command(pweb_project_cli)
pweb_cli_bsw.add_command(pweb_module_cli)
pweb_cli_bsw.add_command(pweb_prod_cli)
