from pweb import Blueprint

boot_static_controller = Blueprint(
    "boot-static",
    __name__,
    url_prefix="/",
    template_folder="../template-assets/templates",
    static_folder="../template-assets/assets",
    static_url_path="boot-assets"
)
