from ppy_common import click


@click.group(name="prod", help="PWeb Deployment Management CLI")
def pweb_prod_cli():
    pass


@click.command(name="create-service", help="Create Linux Service file")
def create_service():
    pass


@click.command(name="create-nignx-conf", help="Create nginx server configuration file")
def create_nignx_conf():
    pass


@click.command(name="generate-config", help="Generate required configuration files (Nginx, Service)")
def generate_config():
    pass


pweb_prod_cli.add_command(create_service)
pweb_prod_cli.add_command(create_nignx_conf)
pweb_prod_cli.add_command(generate_config)
