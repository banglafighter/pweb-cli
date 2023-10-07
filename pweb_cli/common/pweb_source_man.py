import os
import sys
from ppy_common import Console
from ppy_file_text import FileUtil
from ppy_jsonyml import YamlConverter
from pweb_cli.common.pweb_cli_init_data import PWebCLIInitData
from pweb_cli.common.pweb_cli_named import PWebCLINamed


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

