import os

from ppy_file_text import FileUtil


class PWebCLIPath:

    application_dir_name = "application"

    @staticmethod
    def get_root_dir():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @staticmethod
    def current_directory():
        return os.getcwd()

    @staticmethod
    def get_application_dir():
        return os.path.join(PWebCLIPath.current_directory(), PWebCLIPath.application_dir_name)

    @staticmethod
    def get_module_config_dir():
        return os.path.join(PWebCLIPath.get_application_dir(), "config")

    @staticmethod
    def am_i_in_project_root():
        if not FileUtil.is_exist(PWebCLIPath.get_module_config_dir()):
            raise Exception("Please run the command inside the project root")

    @staticmethod
    def exception_on_exist_file(path: str, message: str = "Already exist"):
        PWebCLIPath.exception_on_file_state(path, message=message, is_exist=True)

    @staticmethod
    def exception_on_not_exist_file(path: str, message: str = "Not exist"):
        PWebCLIPath.exception_on_file_state(path, message=message, is_exist=False)

    @staticmethod
    def exception_on_file_state(path: str, message: str, is_exist: bool = True):
        if FileUtil.is_exist(path) == is_exist:
            raise Exception(message)

    @staticmethod
    def get_template_dir():
        return os.path.join(PWebCLIPath.get_root_dir(), "code-template")

    @staticmethod
    def get_template_pweb_dir():
        return os.path.join(PWebCLIPath.get_template_dir(), "pweb")

    @staticmethod
    def get_template_pweb_module_dir():
        return os.path.join(PWebCLIPath.get_template_pweb_dir(), "module")

    @staticmethod
    def get_template_common_dir():
        return os.path.join(PWebCLIPath.get_template_dir(), "common")

    @staticmethod
    def get_template_react_dir():
        return os.path.join(PWebCLIPath.get_template_dir(), "react")

    @staticmethod
    def get_template_server_dir():
        return os.path.join(PWebCLIPath.get_template_dir(), "server")

    @staticmethod
    def get_template_server_centos_dir():
        return os.path.join(PWebCLIPath.get_template_server_dir(), "centos")
