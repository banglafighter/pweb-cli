from ppy_jsonyml.converter.od_base import ODBase
from pweb_cli.common.pweb_cli_named import ActionStatus


class PWebSMRepo(ODBase):
    url: str
    source: str
    name: str = None
    branch: str
    script: list[str]

    def __init__(self, url: str = None, branch: str = None, script: list = None):
        self.url = url
        self.branch = branch
        self.script = script


class PWebSMClone(ODBase):
    branch: str
    status: str
    source: str
    script: list[str]
    repo: list[PWebSMRepo] = None

    def __init__(self, status: str = ActionStatus.active, script: list = None, branch: str = None):
        self.status = status
        self.script = script
        self.branch = branch

    def add_repo(self, repo: PWebSMRepo):
        if not self.repo:
            self.repo = []
        self.repo.append(repo)


class PWebSMDirectory(ODBase):
    name: str
    script: list[str]

    def __init__(self, name: str = None, script: list = None):
        self.name = name
        self.script = script


class PWebSMModule(ODBase):
    status: str
    script: list[str]
    subdir: list[PWebSMDirectory] = None

    def __init__(self, status: str = ActionStatus.active, script: list = None):
        self.status = status
        self.script = script

    def add_subdir(self, subdir: PWebSMDirectory):
        if not self.subdir:
            self.subdir = []
        self.subdir.append(subdir)


class PWebSMDependency(ODBase):
    name: str
    dir: str
    status: str
    module: PWebSMModule
    clone: PWebSMClone

    def __init__(self, name: str = None, dir: str = None, status: str = ActionStatus.active):
        self.name = name
        self.dir = dir
        self.status = status


class PWebSM(ODBase):
    name: str
    start_script: list[str]
    dependencies: list[PWebSMDependency] = None
    end_script: list[str]

    def __init__(self, name: str = None):
        self.name = name

    def add_end_script(self, command):
        if not self.end_script:
            self.end_script = []
        self.end_script.append(command)

    def add_dependency(self, dependency: PWebSMDependency):
        if not self.dependencies:
            self.dependencies = []
        self.dependencies.append(dependency)
