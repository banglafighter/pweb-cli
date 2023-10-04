from ppy_common import Console, click
from pweb_cli.source.pweb_source_cli import pweb_source_setup

Console.blue("--------------------------------", bold=True)
Console.green("      PWeb Source Manager      ", bold=True)
Console.blue("--------------------------------", bold=True)


@click.group()
def pweb_cli_bsw():
    pass


pweb_cli_bsw.add_command(pweb_source_setup)
