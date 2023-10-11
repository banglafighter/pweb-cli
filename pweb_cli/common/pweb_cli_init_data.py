from pweb_cli.common.pweb_cli_named import UIType, ActionStatus
from pweb_cli.data.pweb_cli_pwebsm import PWebSM, PWebSMClone, PWebSMRepo, PWebSMDependency, PWebSMModule, \
    PWebSMDirectory


class PWebCLIInitData:

    @staticmethod
    def get_default_pwebsm(name, ui_type):
        pweb_sm = PWebSM(name=name)

        pweb_sm.start_script = [
            "python --version",
        ]

        pweb_sm.end_script = [
            "python setup.py develop --uninstall",
            "python setup.py develop"
        ]

        if ui_type == UIType.react:
            pweb_sm.end_script.append("npm install -g yarn")
            pweb_sm.end_script.append("yarn install")

        clone: PWebSMClone = PWebSMClone(status=ActionStatus.inactive, branch="dev")
        clone.add_repo(PWebSMRepo(url="https://github.com/problemfighter/pweb.git", script=["python setup.py develop --uninstall", "python setup.py develop"]))

        source_dependency: PWebSMDependency = PWebSMDependency(name="Source Development", status=ActionStatus.inactive, dir="dependencies")
        source_dependency.clone = clone
        pweb_sm.add_dependency(source_dependency)

        module: PWebSMModule = PWebSMModule(status=ActionStatus.inactive, script=["python setup.py develop --uninstall", "python setup.py develop"])
        module.add_subdir(PWebSMDirectory(name="example-app"))

        app_dependency: PWebSMDependency = PWebSMDependency(name="Application", status=ActionStatus.inactive, dir="application")
        app_dependency.module = module
        pweb_sm.add_dependency(app_dependency)

        return pweb_sm
