class PWebCLINamed:
    VENV_DIR_NAME = "venv"


class ActionStatus:
    active = "active"
    inactive = "inactive"


class SourceMode:
    code = "code"
    binary = "binary"


class UIType:
    react = "react"
    ssr = "ssr"
    api = "api"


class ProdAction:
    generate = "generate"


class OperatingSystem:
    centos = "centos"


class AppRendering:
    ssr = "ssr"
    api = "api"
    both = "both"


class AppFileName:
    APP_CONFIG: str = "app_config.py"
    MODULE_REGISTRY: str = "module_registry.py"
    PWEBSM: str = "pwebsm.yml"


class AppDirectoryName:
    application = "application"
    config = "config"
