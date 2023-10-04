from ppy_common import click


@click.command(name="setup", help="Setup PWeb Project from git repo")
@click.option("--repo", "-r", help="Give Project Git Repository", required=True)
@click.option("--directory", "-d", help="Project directory name", default=None, show_default=True)
@click.option("--branch", "-b", help="Enter project branch", default="dev", show_default=True)
@click.option("--environment", "-e", help="Enter project environment name", default=None, show_default=True)
def pweb_source_setup(repo, directory, branch, environment, mode):
    print("Hi")
