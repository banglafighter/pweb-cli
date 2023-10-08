from ppy_common import click, Console
from pweb_cli.common.pweb_cli_named import OperatingSystem, ProdAction
from pweb_cli.prod.pweb_cli_server_man import PWebCLIServerMan

pweb_cli_server_man = PWebCLIServerMan()


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
@click.option("--name", "-n", help="Enter app name", required=True, show_default=True)
@click.option("--domain", "-d", help="Enter domain or subdomain name", required=True, show_default=True)
@click.option("--os", "-os", help="Enter os name", required=True, show_default=True, default=OperatingSystem.centos, type=click.Choice([OperatingSystem.centos]))
@click.option("--action", "-a", help="Enter action", required=True, show_default=True, default=ProdAction.generate, type=click.Choice([ProdAction.generate]))
def generate_config(name, domain, os, action):
    try:
        pweb_cli_server_man.generate(name=name, domain=domain, operating_system=os, action=action)
    except Exception as e:
        Console.error(str(e))


pweb_prod_cli.add_command(create_service)
pweb_prod_cli.add_command(create_nignx_conf)
pweb_prod_cli.add_command(generate_config)
