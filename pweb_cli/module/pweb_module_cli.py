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


@click.command(name="controller", help="Create new controller")
@click.option("--name", "-n", help="Controller name", default=None, show_default=True, required=True)
@click.option("--mname", "-m", help="Module name", default=None, show_default=True, required=True)
@click.option("--pname", "-p", help="Module package name", default=None, show_default=True)
def controller(name, mname, pname):
    try:
        pweb_cli_module_man.create_pweb_controller(name=name, module_name=mname, package_name=pname)
    except Exception as e:
        Console.error(str(e))


@click.command(name="all", help="Create new all")
@click.option("--name", "-n", help="Controller name", default=None, show_default=True, required=True)
@click.option("--mname", "-m", help="Module name", default=None, show_default=True, required=True)
@click.option("--pname", "-p", help="Module package name", default=None, show_default=True)
@click.option("--rendering", "-r", help="Module Rendering", required=True, show_default=True, type=click.Choice([AppRendering.api, AppRendering.ssr], case_sensitive=False))
def all(name, mname, pname, rendering):
    try:
        pweb_cli_module_man.create_pweb_all(name=name, module_name=mname, package_name=pname, rendering=rendering)
    except Exception as e:
        Console.error(str(e))


@click.command(name="service", help="Create new service")
@click.option("--name", "-n", help="Controller name", default=None, show_default=True, required=True)
@click.option("--mname", "-m", help="Module name", default=None, show_default=True, required=True)
@click.option("--pname", "-p", help="Module package name", default=None, show_default=True)
def service(name, mname, pname):
    try:
        pweb_cli_module_man.create_pweb_service(name=name, module_name=mname, package_name=pname)
    except Exception as e:
        Console.error(str(e))


@click.command(name="model", help="Create new model")
@click.option("--name", "-n", help="Controller name", default=None, show_default=True, required=True)
@click.option("--mname", "-m", help="Module name", default=None, show_default=True, required=True)
@click.option("--pname", "-p", help="Module package name", default=None, show_default=True)
def model(name, mname, pname):
    try:
        pweb_cli_module_man.create_pweb_model(name=name, module_name=mname, package_name=pname)
    except Exception as e:
        Console.error(str(e))


@click.command(name="form", help="Create new form")
@click.option("--name", "-n", help="Controller name", default=None, show_default=True, required=True)
@click.option("--mname", "-m", help="Module name", default=None, show_default=True, required=True)
@click.option("--pname", "-p", help="Module package name", default=None, show_default=True)
def form(name, mname, pname):
    try:
        pweb_cli_module_man.create_pweb_form(name=name, module_name=mname, package_name=pname)
    except Exception as e:
        Console.error(str(e))


@click.command(name="dto", help="Create new dto")
@click.option("--name", "-n", help="Controller name", default=None, show_default=True, required=True)
@click.option("--mname", "-m", help="Module name", default=None, show_default=True, required=True)
@click.option("--pname", "-p", help="Module package name", default=None, show_default=True)
def dto(name, mname, pname):
    try:
        pweb_cli_module_man.create_pweb_dto(name=name, module_name=mname, package_name=pname)
    except Exception as e:
        Console.error(str(e))


pweb_module_cli.add_command(create)
pweb_module_cli.add_command(controller)
pweb_module_cli.add_command(dto)
pweb_module_cli.add_command(form)
pweb_module_cli.add_command(model)
pweb_module_cli.add_command(all)
