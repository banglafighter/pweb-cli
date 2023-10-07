import os


class PWebCLIPath:

    application_dir_name = "application"

    @staticmethod
    def get_root_dir():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @staticmethod
    def get_template_dir():
        return os.path.join(PWebCLIPath.get_root_dir(), "code-template")

    @staticmethod
    def get_template_pweb_dir():
        return os.path.join(PWebCLIPath.get_template_dir(), "pweb")

    @staticmethod
    def get_template_common_dir():
        return os.path.join(PWebCLIPath.get_template_dir(), "common")
