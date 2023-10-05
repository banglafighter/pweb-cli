from ppy_common import click


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
def init():
    pass


pweb_project_cli.add_command(setup)
pweb_project_cli.add_command(update)
pweb_project_cli.add_command(init)
