from ppy_common import click, Console
from pweb_cli.common.pweb_cli_named import UIType
from pweb_cli.common.pweb_cli_path import PWebCLIPath
from pweb_cli.project.pweb_cli_project_man import PWebCLIProjectMan

pweb_cli_project_man = PWebCLIProjectMan()


@click.group(name="project", help="PWeb Project Management CLI")
def pweb_project_cli():
    pass


@click.command(name="setup", help="Setup PWeb Project from git repo")
@click.option("--repo", "-r", help="Give Project Git Repository", required=True)
@click.option("--directory", "-d", help="Project directory name", default=None, show_default=True)
@click.option("--branch", "-b", help="Enter project branch", default="dev", show_default=True)
@click.option("--environment", "-e", help="Enter project environment name", default=None, show_default=True)
def setup(repo, directory, branch, environment):
    try:
        PWebCLIPath.am_i_in_project_root()
        pweb_cli_project_man.setup(repo=repo, branch=branch, directory=directory, env=environment)
    except Exception as e:
        print("\n\n")
        Console.error(str(e))


@click.command(name="update", help="Download new changes and update the project")
@click.option("--environment", "-e", help="Enter project environment name", default=None, show_default=True)
def update(environment):
    try:
        PWebCLIPath.am_i_in_project_root()
        pweb_cli_project_man.update(env=environment)
    except Exception as e:
        print("\n\n")
        Console.error(str(e))


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
