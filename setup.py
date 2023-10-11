from setuptools import setup, find_packages
import os
import pathlib

CURRENT_DIR = pathlib.Path(__file__).parent
README = (CURRENT_DIR / "README.md").read_text()

env = os.environ.get('source')


def get_dependencies():
    dependency = ["virtualenv", "GitPython==3.1.37"]

    if env and env == "code":
        return dependency

    return dependency + ["ppy-common", "ppy-file-text", "ppy-jsonyml"]


setup(
    name='pweb-cli',
    version='0.0.2',
    url='https://github.com/problemfighter/pweb-cli',
    license='Apache 2.0',
    author='Problem Fighter',
    author_email='problemfighter.com@gmail.com',
    description='Command line interface for PWeb application, which allow to make PWeb work easy.',
    long_description=README,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=get_dependencies(),
    entry_points={
        'console_scripts': [
            'pwebcli=pweb_cli.pweb_cli_bsw:pweb_cli_bsw'
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ]
)
