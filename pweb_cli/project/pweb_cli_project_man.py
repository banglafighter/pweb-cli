from ppy_common import Console
from ppy_file_text import StringUtil
from pweb_cli.common.pweb_source_man import PWebSourceMan


class PWebCLIProjectMan:
    pweb_source_man = PWebSourceMan()

    def get_directory_name(self, name: str):
        name = name.lower()
        name = StringUtil.system_readable(name)
        name = StringUtil.find_and_replace_with(name, "_", "-")
        return name

    def init(self, name, port, directory, ui_type):
        Console.success(f"Initializing Project, Name: {name}")
        if not directory:
            directory = name.lower()
        directory = self.get_directory_name(name=directory)
        project_root = self.pweb_source_man.get_project_root_dir(directory=directory)

    def setup(self):
        pass

    def update(self):
        pass
