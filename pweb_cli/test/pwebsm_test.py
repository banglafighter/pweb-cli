from ppy_jsonyml.converter.yaml_converter import YamlConverter
from pweb_cli.data.pweb_cli_pwebsm import PWebSM

pweb_sm_content = """
name: "This is the Project Name"

start_script:
  - script 1
  - script 2

dependencies:
  - name: "app-base-dependencies"
    dir: "dependencies"
    status: "active"

    module:
      status: "inactive"
      script:
        - python setup.py develop
      dir:
        - name: "example-module"
          script:
            - python setup.py develop

    clone:
      branch: "dev"
      status: "active"
      script:
        - python setup.py develop
      repo:
        - url: "https://example.com/example.git"
          name: "project-name"
          branch: "pre-release"
          script:
            - python --version


end_script:
  - script 1
  - script 2
"""

yaml_converter = YamlConverter()
pweb_sm = PWebSM()
response = yaml_converter.yaml_to_object(pweb_sm_content, pweb_sm)
print(response)
