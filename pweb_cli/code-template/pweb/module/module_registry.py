from pweb import PWebComponentRegister, PWebModuleDetails


class __MODULE_CLASS_NAME__Module(PWebComponentRegister):

    def app_details(self) -> PWebModuleDetails:
        return PWebModuleDetails(system_name="___MODULE_SETUP_NAME__", display_name="__MODULE_DISPLAY_NAME__")

    def run_on_cli_init(self, pweb_app, config):
        pass

    def run_on_start(self, pweb_app, config):
        pass

    def register_model(self, pweb_db):
        pass

    def register_controller(self, pweb_app):
        # pweb_app.register_blueprint(example_controller)
        pass
