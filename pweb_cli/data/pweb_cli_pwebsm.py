from ppy_jsonyml.converter.od_base import ODBase


class PWebSMRepo(ODBase):
    url: str
    name: str
    branch: str
    script: list[str]


class PWebSMClone(ODBase):
    branch: str
    status: str
    script: list[str]
    repo: PWebSMRepo


class PWebSMDirectory(ODBase):
    name: str
    script: list[str]


class PWebSMModule(ODBase):
    status: str
    script: list[str]
    dir: PWebSMDirectory


class PWebSMDependency(ODBase):
    name: str
    dir: str
    status: str
    module: PWebSMModule
    clone: PWebSMClone


class PWebSM(ODBase):
    name: str
    start_script: list[str]
    dependencies: list[str]
    end_script: list[str]
