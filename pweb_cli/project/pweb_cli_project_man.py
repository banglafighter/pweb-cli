from ppy_common import Console
from ppy_file_text import StringUtil


class PWebCLIProjectMan:

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

    def setup(self):
        pass

    def update(self):
        pass
