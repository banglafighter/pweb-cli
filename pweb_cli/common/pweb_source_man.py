import os
import sys
from ppy_common import Console
from ppy_file_text import FileUtil, StringUtil, TextFileMan
from ppy_jsonyml import YamlConverter
from pweb_cli.common.pweb_cli_init_data import PWebCLIInitData
from pweb_cli.common.pweb_cli_named import PWebCLINamed
from pweb_cli.common.pweb_cli_path import PWebCLIPath


class PWebSourceMan:
    yaml_converter = YamlConverter()
    pwebsm_file_name = "pwebsm.yml"

    def project_root_dir(self, directory=None):
        root_path = FileUtil.getcwd()
        if directory:
            root_path = FileUtil.join_path(root_path, directory)
        return root_path

    def get_project_root_dir(self, directory=None):
        project_root = self.project_root_dir(directory=directory)
        if FileUtil.is_exist(project_root):
            raise Exception("{} Path already exist.".format(str(project_root)))
        FileUtil.create_directories(project_root)
        return project_root

    def run_command_with_venv(self, command_root, project_root, command, mode):
        active = "source " + FileUtil.join_path(project_root, PWebCLINamed.VENV_DIR_NAME, "bin", "activate")
        if sys.platform == "win32":
            active = FileUtil.join_path(project_root, PWebCLINamed.VENV_DIR_NAME, "Scripts", "activate")
        command = active + " && " + command
        Console.run(command, command_root, env=dict(os.environ, **{"source": mode}))

    def create_pwebsm_yml(self, project_root, name, ui_type):
        pwebsm = PWebCLIInitData.get_default_pwebsm(name=name, ui_type=ui_type)
        pwebsm_yaml_text = self.yaml_converter.object_to_yaml(od_object=pwebsm, is_ignore_none=True)
        self.yaml_converter.write_yaml_content_to_file(FileUtil.join_path(project_root, self.pwebsm_file_name), yaml_content=pwebsm_yaml_text)

    def copy_file(self, source, destination, file_dir_name, dst_file_name=None):
        source_file_dir = FileUtil.join_path(source, file_dir_name)
        _dst_file_name = file_dir_name
        if dst_file_name:
            _dst_file_name = dst_file_name
        destination_file_dir = FileUtil.join_path(destination, _dst_file_name)
        FileUtil.delete(destination_file_dir)
        FileUtil.copy(source_file_dir, destination_file_dir)
        return destination_file_dir

    def process_pweb_files(self, project_root, name, port):
        system_name = StringUtil.system_readable(name)
        system_hyphen_name = StringUtil.find_and_replace_with(system_name, "_", "-")

        for file_name in [".gitignore", "README.md"]:
            self.copy_file(PWebCLIPath.get_template_common_dir(), project_root, file_name)

        destination_file = self.copy_file(PWebCLIPath.get_template_pweb_dir(), project_root, "pweb_app.py")
        TextFileMan.find_replace_text_content(destination_file, [
            {"find": "___APP_NAME__", "replace": system_name}
        ])

        destination_file = self.copy_file(PWebCLIPath.get_template_pweb_dir(), project_root, "setup.py")
        TextFileMan.find_replace_text_content(destination_file, [
            {"find": "___APP_NAME__", "replace": system_hyphen_name}
        ])

        for file_name in [PWebCLIPath.application_dir_name, "env.yml"]:
            self.copy_file(PWebCLIPath.get_template_pweb_dir(), project_root, file_name)

        app_config_file = FileUtil.join_path(project_root, PWebCLIPath.application_dir_name, "config", "app_config.py")
        TextFileMan.find_replace_text_content(app_config_file, [
            {"find": "___APP_NAME___", "replace": name},
            {"find": "___APP_PORT___", "replace": str(port)},
        ])

