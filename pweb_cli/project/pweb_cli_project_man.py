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

        Console.success("Creating source management descriptor")
        self.pweb_source_man.create_pwebsm_yml(project_root=project_root, name=name, ui_type=ui_type)

        Console.success("Creating project required files")
        self.pweb_source_man.process_pweb_files(project_root=project_root, name=name, port=port)

        self.pweb_source_man.process_react_files(project_root=project_root, name=name, ui_type=ui_type)

        Console.success("Creating virtual environment for the project")
        self.pweb_source_man.create_virtual_env(project_root=project_root)

        Console.success("Resolving project dependencies")
        self.pweb_source_man.run_pwebsm(project_root=project_root)

        print("\n")
        Console.success("----------------------------------------")
        Console.red("           Congratulations!!", bold=True)
        Console.yellow("      Project has been Initialized")
        Console.success("----------------------------------------")

        print("\n")
        Console.info("Go to project directory: " + directory)
        Console.info("First active the virtual environment")
        Console.info("Run Command: pweb_app.py")

    def setup(self, repo, directory, branch, env):
        Console.success(f"Starting setup...")
        self.pweb_source_man.setup(repo=repo, directory=directory, branch=branch, env=env)
        Console.success(f"Setup process has been completed")

    def update(self, env):
        Console.success(f"Starting update...")
        self.pweb_source_man.update(env=env)
        Console.success(f"Update process has been completed")
