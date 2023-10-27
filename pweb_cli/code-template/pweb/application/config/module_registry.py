from pweb import PWebModuleRegister
from boot.boot_module import BootModule


class Register(PWebModuleRegister):

    def get_module_list(self) -> list:
        return [BootModule]
