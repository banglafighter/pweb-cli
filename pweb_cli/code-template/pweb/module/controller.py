from pweb import Blueprint

url_prefix = "/___URL_NAME___"
___LOWER__UNDERSCORE_NAME____controller = Blueprint(
    "___LOWER__UNDERSCORE_NAME____controller",
    __name__,
    url_prefix=url_prefix
)


@___LOWER__UNDERSCORE_NAME____controller.route("/", methods=['GET', 'POST'])
def index():
    return "Index Page"
