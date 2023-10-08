from ppy_common import Console
from ppy_file_text import StringUtil, FileUtil, TextFileMan
from pweb_cli.common.pweb_cli_named import AppRendering
from pweb_cli.common.pweb_cli_path import PWebCLIPath


class PWebCLIModuleMan:
    starting_message: str = "Starting"

    def create_pweb_module(self, name: str, version: str = None, rendering: str = AppRendering.api):
        display_name = StringUtil.human_readable(name)
        class_name = StringUtil.py_class_name(name)
        file_name = setup_package_name = StringUtil.py_hyphen_name(name)
        package_name = StringUtil.py_underscore_name(name)

        if not version:
            version = "1.0.0"

        PWebCLIPath.am_i_in_project_root()
        module_root = FileUtil.join_path(PWebCLIPath.get_application_dir(), file_name)
        module_package_root = FileUtil.join_path(module_root, package_name)
        PWebCLIPath.exception_on_exist_file(module_root, message=f"{setup_package_name} module already exist.")
        template_path = PWebCLIPath.get_template_pweb_module_dir()

        Console.success(f"{self.starting_message} {display_name} ({setup_package_name}) Module creation")

        find_replace = [
            {"find": "__MODULE_DISPLAY_NAME__", "replace": display_name},
            {"find": "___MODULE_SETUP_NAME__", "replace": setup_package_name},
            {"find": "___VERSION___", "replace": version},
            {"find": "__MODULE_CLASS_NAME__", "replace": class_name}
        ]

        Console.info("Creating Package Root")
        FileUtil.create_directories(module_package_root)
        init_file = FileUtil.join_path(template_path, "__init__.py")
        FileUtil.copy(init_file, FileUtil.join_path(module_package_root, "__init__.py"))

        Console.info("Creating Essential files")
        directory_structure = [".gitignore", "README.md", "setup.py"]
        for directory in directory_structure:
            source_path = FileUtil.join_path(template_path, directory)
            copy_to_path = FileUtil.join_path(module_root, directory)
            FileUtil.copy(source_path, copy_to_path)
            TextFileMan.find_replace_text_content(copy_to_path, find_replace)

        Console.info("Creating Component Register")
        module_descriptor = FileUtil.join_path(module_package_root, f"{package_name}_module.py")
        FileUtil.copy(FileUtil.join_path(template_path, "module_registry.py"), module_descriptor)
        TextFileMan.find_replace_text_content(module_descriptor, find_replace)

        Console.info("Creating Pacakge Structure")
        directory_structure = ["common", "controller", "data", "model", "service"]
        if rendering == AppRendering.api:
            directory_structure.append("dto")
        elif rendering == AppRendering.ssr:
            directory_structure.append("form")
        else:
            directory_structure.append("form")
            directory_structure.append("dto")

        for directory in directory_structure:
            path = FileUtil.join_path(module_package_root, directory)
            FileUtil.create_directories(path)
            FileUtil.copy(init_file, FileUtil.join_path(path, "__init__.py"))

    def _create_pweb_component(self, name, module_name, package_name, package_dir, file_extra_name, template_file):
        PWebCLIPath.am_i_in_project_root()

        if not package_name:
            package_name = StringUtil.py_underscore_name(module_name)

        dist_path = FileUtil.join_path(PWebCLIPath.get_application_dir(), module_name, package_name, package_dir)
        dist_file = f"{StringUtil.py_underscore_name(name)}{file_extra_name}.py"
        dist_path_and_file = FileUtil.join_path(dist_path, dist_file)
        PWebCLIPath.exception_on_not_exist_file(dist_path, f"Module and Package not exist. {dist_path}")
        PWebCLIPath.exception_on_exist_file(dist_path_and_file, f"File already exist. {dist_file}")

        Console.success(f"{self.starting_message} {dist_file}")
        source_template = FileUtil.join_path(PWebCLIPath.get_template_pweb_module_dir(), template_file)
        FileUtil.copy(source_template, dist_path_and_file)

        class_name = StringUtil.py_class_name(name)
        find_replace = [
            {"find": "___LOWER__UNDERSCORE_NAME___", "replace": StringUtil.py_underscore_name(name)},
            {"find": "___URL_NAME___", "replace": StringUtil.text_to_url_text(name)},
            {"find": "___DTO_NAME___", "replace": class_name},
            {"find": "___FORM_NAME___", "replace": class_name},
            {"find": "___MODEL_NAME___", "replace": class_name},
            {"find": "___SERVICE_NAME___", "replace": class_name},
        ]
        TextFileMan.find_replace_text_content(dist_path_and_file, find_replace)
        Console.info(f"Created {dist_file}")

    def create_pweb_controller(self, name, module_name, package_name=None):
        self._create_pweb_component(
            name=name,
            module_name=module_name,
            package_name=package_name,
            package_dir="controller",
            file_extra_name="_controller",
            template_file="controller.py"
        )

    def create_pweb_model(self, name, module_name, package_name=None):
        self._create_pweb_component(
            name=name,
            module_name=module_name,
            package_name=package_name,
            package_dir="model",
            file_extra_name="",
            template_file="model.py"
        )

    def create_pweb_dto(self, name, module_name, package_name=None):
        self._create_pweb_component(
            name=name,
            module_name=module_name,
            package_name=package_name,
            package_dir="dto",
            file_extra_name="_dto",
            template_file="dto.py"
        )

    def create_pweb_form(self, name, module_name, package_name=None):
        self._create_pweb_component(
            name=name,
            module_name=module_name,
            package_name=package_name,
            package_dir="form",
            file_extra_name="_form",
            template_file="form.py"
        )

    def create_pweb_service(self, name, module_name, package_name=None):
        self._create_pweb_component(
            name=name,
            module_name=module_name,
            package_name=package_name,
            package_dir="service",
            file_extra_name="_service",
            template_file="service.py"
        )

    def create_pweb_all(self, name, module_name, rendering, package_name=None):
        self.create_pweb_controller(name=name, module_name=module_name, package_name=package_name)
        self.create_pweb_model(name=name, module_name=module_name, package_name=package_name)
        self.create_pweb_service(name=name, module_name=module_name, package_name=package_name)

        if rendering == AppRendering.api:
            self.create_pweb_dto(name=name, module_name=module_name, package_name=package_name)
        elif rendering == AppRendering.ssr:
            self.create_pweb_form(name=name, module_name=module_name, package_name=package_name)
