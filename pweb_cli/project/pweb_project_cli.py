from ppy_common import click, Console
from pweb_cli.common.pweb_cli_named import UIType
from pweb_cli.project.pweb_cli_project_man import PWebCLIProjectMan

pweb_cli_project_man = PWebCLIProjectMan()


@click.group(name="project", help="PWeb Project Management CLI")
def pweb_project_cli():
    pass


@click.command(name="setup", help="Setup PWeb Project from git repo")
def setup():
    pass


@click.command(name="update", help="Download new changes and update the project")
def update():
    pass


@click.command(name="init", help="Initialize project from scratch")
@click.option("--name", "-n", help="Project name", default=None, show_default=True, required=True)
@click.option("--port", "-p", help="Project run on the port", default=1212, show_default=True, type=int)
@click.option("--directory", "-d", help="Project directory name", default=None, show_default=True)
@click.option("--ui-type", "-ui", help="Enter Project UI Type", default=UIType.ssr, show_default=True, type=click.Choice([UIType.react, UIType.ssr, UIType.api], case_sensitive=False))
def init(name, port, directory, ui_type):
    try:
        pweb_cli_project_man.init(name=name, port=port, directory=directory, ui_type=ui_type)
    except Exception as e:
        print("\n\n")
        Console.error(str(e))


pweb_project_cli.add_command(setup)
pweb_project_cli.add_command(update)
pweb_project_cli.add_command(init)
