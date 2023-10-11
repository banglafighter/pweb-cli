import os
import sys
from ppy_common import Console
from ppy_file_text import FileUtil, StringUtil, TextFileMan
from ppy_jsonyml import YamlConverter
from pweb_cli.common.pweb_cli_init_data import PWebCLIInitData
from pweb_cli.common.pweb_cli_named import PWebCLINamed, UIType, ActionStatus, SourceMode
from pweb_cli.common.pweb_cli_path import PWebCLIPath
from pweb_cli.common.pweb_git_repo import PWebGitRepo
from pweb_cli.data.pweb_cli_pwebsm import PWebSM, PWebSMModule, PWebSMClone


class PWebSourceMan:
    yaml_converter = YamlConverter()
    pweb_git_repo = PWebGitRepo()
    pwebsm_file_name = "pwebsm"
    pwebsm_file_extension = ".yml"

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

    def get_pwebsm_file_name(self, env=None):
        env_postfix = ""
        if env:
            env_postfix = "-" + env
        return self.pwebsm_file_name + env_postfix + self.pwebsm_file_extension

    def run_command_with_venv(self, command_root, project_root, command, env_variable: dict = {}):
        active = "source " + FileUtil.join_path(project_root, PWebCLINamed.VENV_DIR_NAME, "bin", "activate")
        if sys.platform == "win32":
            active = FileUtil.join_path(project_root, PWebCLINamed.VENV_DIR_NAME, "Scripts", "activate")
        command = active + " && " + command
        Console.run(command, command_root, env=dict(os.environ, **env_variable))

    def create_pwebsm_yml(self, project_root, name, ui_type):
        pwebsm = PWebCLIInitData.get_default_pwebsm(name=name, ui_type=ui_type)
        pwebsm_yaml_text = self.yaml_converter.object_to_yaml(od_object=pwebsm, is_ignore_none=True)
        self.yaml_converter.write_yaml_content_to_file(FileUtil.join_path(project_root, self.get_pwebsm_file_name()), yaml_content=pwebsm_yaml_text)

    def copy_file(self, source, destination, file_dir_name, dst_file_name=None):
        source_file_dir = FileUtil.join_path(source, file_dir_name)
        _dst_file_name = file_dir_name
        if dst_file_name:
            _dst_file_name = dst_file_name
        destination_file_dir = FileUtil.join_path(destination, _dst_file_name)
        FileUtil.delete(destination_file_dir)
        FileUtil.copy(source_file_dir, destination_file_dir)
        return destination_file_dir

    @staticmethod
    def get_system_readable_name(name: str, replace: str = "_"):
        if not name:
            return name
        name = name.lower()
        name = name.strip()
        name = StringUtil.find_and_replace_with(name, " ", replace)
        return StringUtil.remove_special_character(name)

    def process_pweb_files(self, project_root, name, port):
        system_hyphen_name = PWebSourceMan.get_system_readable_name(name, "-")

        for file_name in [".gitignore", "README.md"]:
            self.copy_file(PWebCLIPath.get_template_common_dir(), project_root, file_name)

        pweb_app_name = StringUtil.find_and_replace_with(name, " ", "")
        pweb_app_name = StringUtil.remove_special_character(pweb_app_name)
        destination_file = self.copy_file(PWebCLIPath.get_template_pweb_dir(), project_root, "pweb_app.py")
        TextFileMan.find_replace_text_content(destination_file, [
            {"find": "___APP_NAME__", "replace": pweb_app_name}
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

    def process_react_files(self, project_root, name, ui_type):
        if ui_type != UIType.react:
            return

        system_hyphen_name = PWebSourceMan.get_system_readable_name(name, "-")

        Console.success("Processing React Config")
        for file_name in ["lerna.json", "package.json"]:
            self.copy_file(PWebCLIPath.get_template_react_dir(), project_root, file_name)

        package_json = os.path.join(project_root, "package.json")
        if FileUtil.is_exist(package_json):
            TextFileMan.find_replace_text_content(package_json, [
                {"find": "___APP_NAME___", "replace": system_hyphen_name},
                {"find": "___PROJECT_APP_NAME___", "replace": system_hyphen_name + "-app"}
            ])

    def get_python(self):
        return sys.executable

    def create_virtual_env(self, project_root):
        if not FileUtil.is_exist(FileUtil.join_path(project_root, PWebCLINamed.VENV_DIR_NAME)):
            Console.run(self.get_python() + " -m venv " + PWebCLINamed.VENV_DIR_NAME, project_root)

    def run_pwebsm(self, project_root=None, env=None, directory=None):
        if not project_root:
            project_root = self.project_root_dir(directory=directory)

        pwebsm_file = self.get_pwebsm_file_name(env=env)
        pwesm_file_path = FileUtil.join_path(project_root, pwebsm_file)
        if not FileUtil.is_exist(pwesm_file_path):
            raise Exception("PWeb source management file not found")
        self.process_pwebsm_file(project_root=project_root, file_path=pwesm_file_path)

    def _run_script(self, project_root, command_root, scrips: list, source_mode: str = SourceMode.binary):
        if not scrips or not project_root or not command_root:
            return False
        for command in scrips:
            if not command:
                continue
            self.run_command_with_venv(command_root=command_root, project_root=project_root, command=command, env_variable={"source": source_mode})

    def _run_start_script(self, project_root, pweb_sm: PWebSM):
        if pweb_sm and pweb_sm.start_script:
            Console.info("Running start script")
            self._run_script(project_root=project_root, command_root=project_root, scrips=pweb_sm.start_script)

    def _run_end_script(self, project_root, pweb_sm: PWebSM):
        pweb_sm.add_end_script(f"{self.get_python()} pweb_app.py develop")
        if pweb_sm and pweb_sm.end_script:
            Console.info("Running end script")
            self._run_script(project_root=project_root, command_root=project_root, scrips=pweb_sm.end_script)

    def _process_clone(self, project_root, clone: PWebSMClone, base_dir: str):
        if not clone.status or clone.status != ActionStatus.active or not clone.repo:
            return

        Console.info(f"Starting clone work")
        parent_script = clone.script
        parent_branch = clone.branch
        source_mode = SourceMode.binary
        if clone.source:
            source_mode = clone.source

        for repo in clone.repo:
            if not repo.url:
                continue

            scripts = parent_script
            if repo.script:
                scripts = repo.script

            name = repo.name
            if not name:
                name = self.pweb_git_repo.get_repo_name_from_url(repo.url)

            branch = None
            if repo.branch:
                branch = repo.branch
            elif parent_branch:
                branch = parent_branch

            if repo.source:
                source_mode = repo.source

            clone_dir = FileUtil.join_path(project_root, base_dir)
            FileUtil.create_directories(clone_dir)
            clone_project_dir = FileUtil.join_path(clone_dir, name)

            Console.info(f"Cloning Project : {repo.url}")
            Console.cyan(f"Cloning at : {clone_dir}", enable_staring=True)
            self.pweb_git_repo.clone_or_pull_project(path=clone_project_dir, url=repo.url, branch=branch)
            command_root = FileUtil.join_path(clone_dir, name)
            if not FileUtil.is_exist(command_root) or not scripts:
                continue

            Console.info(f"Running script for {name}")
            self._run_script(project_root=project_root, command_root=command_root, scrips=scripts, source_mode=source_mode)

    def _process_module(self, project_root, module: PWebSMModule, base_dir: str):
        if not module.status or module.status != ActionStatus.active or not module.subdir:
            return

        Console.info(f"Starting model work")
        parent_script = module.script
        for child_module in module.subdir:
            command_root = FileUtil.join_path(project_root, base_dir, child_module.name)
            scripts = parent_script
            if child_module.script:
                scripts = child_module.script
            if not scripts:
                continue

            Console.info(f"Running script for {child_module.name}")
            self._run_script(project_root=project_root, command_root=command_root, scrips=scripts)

    def _process_dependencies(self, project_root, pweb_sm: PWebSM):
        if not pweb_sm or not project_root or not pweb_sm.dependencies:
            return

        for dependency in pweb_sm.dependencies:
            try:
                if not dependency.status or dependency.status != ActionStatus.active:
                    continue

                if dependency.clone:
                    self._process_clone(project_root=project_root, clone=dependency.clone, base_dir=dependency.dir)

                if dependency.module:
                    self._process_module(project_root=project_root, module=dependency.module, base_dir=dependency.dir)
            except Exception as e:
                print("\n\n")
                Console.error(str(e))

    def process_pwebsm_file(self, project_root, file_path: str):
        pweb_sm: PWebSM = self.yaml_converter.read_yaml_object_from_file(file_path_with_name=file_path, od_object=PWebSM())
        if not pweb_sm:
            raise Exception("Invalid descriptor file for PWeb Source Management")
        self._run_start_script(project_root=project_root, pweb_sm=pweb_sm)
        self._process_dependencies(project_root=project_root, pweb_sm=pweb_sm)
        self._run_end_script(project_root=project_root, pweb_sm=pweb_sm)

    def _setup_or_update(self, project_root, url=None, branch=None, env=None, directory=None):
        if url and branch:
            self.pweb_git_repo.clone_or_pull_project(project_root, url, branch)
        self.create_virtual_env(project_root=project_root)
        self.run_pwebsm(project_root=project_root, env=env, directory=directory)

    def update(self, env):
        project_root = os.getcwd()
        self._setup_or_update(project_root=project_root, env=env)

    def setup(self, repo, directory, branch, env):
        if not directory:
            directory = self.pweb_git_repo.get_repo_name_from_url(repo)
        project_root = self.project_root_dir(directory=directory)
        if FileUtil.is_exist(project_root):
            raise Exception("{} Path already exist.".format(str(project_root)))
        self._setup_or_update(project_root=project_root, url=repo, branch=branch, env=env)

