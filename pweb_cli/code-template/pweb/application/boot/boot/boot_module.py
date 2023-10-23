from boot.controller.boot_static_controller import boot_static_controller
from pweb import PWebComponentRegister, PWebModuleDetails
from boot.controller.home_controller import home_controller


class BootModule(PWebComponentRegister):

    def app_details(self) -> PWebModuleDetails:
        return PWebModuleDetails(system_name="boot", display_name="Python Web Boot")

    def run_on_cli_init(self, pweb_app, config):
        pass

    def run_on_start(self, pweb_app, config):
        pass

    def register_model(self, pweb_db):
        pass

    def register_controller(self, pweb_app):
        pweb_app.register_blueprint(home_controller)
        pweb_app.register_blueprint(boot_static_controller)
