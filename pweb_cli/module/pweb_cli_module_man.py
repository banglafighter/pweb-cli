from ppy_common import Console
from ppy_file_text import StringUtil, FileUtil, TextFileMan
from pweb_cli.common.pweb_cli_named import AppRendering
from pweb_cli.common.pweb_cli_path import PWebCLIPath


class PWebCLIModuleMan:
    starting_message: str = "Starting"

    def create_pweb_module(self, name: str, version: str = None, rendering: str = AppRendering.api):
        Console.success(f"{self.starting_message} Module creation")
        display_name = StringUtil.human_readable(name)
        class_name = StringUtil.py_class_name(name)
        file_name = setup_package_name = StringUtil.py_hyphen_name(name)
        package_name = StringUtil.py_underscore_name(name)

        if not version:
            version = "1.0.0"

        PWebCLIPath.am_i_in_project_root()
        module_root = FileUtil.join_path(PWebCLIPath.get_application_dir(), file_name)
        module_package_root = FileUtil.join_path(module_root, package_name)
        PWebCLIPath.exception_on_exist_file(module_root, message="Module already exist.")
        template_path = PWebCLIPath.get_template_pweb_module_dir()

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

    def create_pweb_controller(self):
        pass

    def create_pweb_model(self):
        pass

    def create_pweb_dto(self):
        pass

    def create_pweb_form(self):
        pass

    def create_pweb_service(self):
        pass

    def create_pweb_all(self):
        pass

    def create_react_module(self):
        pass
