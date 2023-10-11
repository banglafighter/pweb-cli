from ppy_common import Console
from ppy_file_text import FileUtil, TextFileMan
from pweb_cli.common.pweb_cli_named import ProdAction, OperatingSystem
from pweb_cli.common.pweb_cli_path import PWebCLIPath


class PWebCLIServerMan:

    def create_file(self, src_file, dst_file, find_replace: list):
        FileUtil.copy(src_file, dst_file)
        TextFileMan.find_replace_text_content(dst_file, find_replace)
        return dst_file

    def create_centos_prod(self, name, application_root, domain):
        Console.success("Creating Production Files")
        unix_socket_path = "unix:" + FileUtil.join_path(application_root, "PWeb.sock")
        fd_dict = [
            {"find": "___DOMAIN_NAME___", "replace": domain},
            {"find": "___UNIX_SOCK___", "replace": unix_socket_path},
            {"find": "___APP_NAME___", "replace": name},
            {"find": "___PROJECT_ROOT___", "replace": application_root},
        ]
        dsc_root = FileUtil.join_path(application_root, "prod")
        FileUtil.create_directories(dsc_root)
        service_src = FileUtil.join_path(PWebCLIPath.get_template_server_centos_dir(), "application.service")
        service_dst = FileUtil.join_path(dsc_root, domain + ".service")

        nginx_src = FileUtil.join_path(PWebCLIPath.get_template_server_centos_dir(), "nginx.conf")
        nginx_dst = FileUtil.join_path(dsc_root, domain + ".conf")

        self.create_file(service_src, service_dst, fd_dict)
        self.create_file(nginx_src, nginx_dst, fd_dict)
        Console.info(f"Created Nginx and service file on {dsc_root}")

    def generate_on_os(self, name, domain, operating_system):
        application_root = PWebCLIPath.current_directory()
        if operating_system == OperatingSystem.centos:
            self.create_centos_prod(name, application_root, domain)
        else:
            Console.error("Invalid OS Selected")

    def generate(self, name, domain, operating_system, action):
        PWebCLIPath.am_i_in_project_root()
        if action == ProdAction.generate:
            self.generate_on_os(name, domain, operating_system=operating_system)
        else:
            Console.error("Invalid Action")
