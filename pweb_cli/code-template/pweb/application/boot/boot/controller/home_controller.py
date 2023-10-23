from pweb import Blueprint
from pweb_form_rest import ssr_ui_render

url_prefix = "/"
home_controller = Blueprint(
    "home_controller",
    __name__,
    url_prefix=url_prefix
)


@home_controller.route("/", methods=['GET'])
def index():
    return ssr_ui_render(view_name="home/index")
