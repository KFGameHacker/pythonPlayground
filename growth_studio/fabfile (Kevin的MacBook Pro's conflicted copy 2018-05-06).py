from fabric.api import local 
from fabric.decorators import task
import webbrowser

@task
def r():
    """RUN SERVER"""
    local("./manage.py runserver")
    webbrowser.open_new_tab('http://127.0.0.1:8000/')

@task
def install(requirements_env="dev"):
    """INTSALL THE REQUIREMENTS"""
    local("pip install -r requirements/%s.txt" % requirements_env)

@task
def hello():
    """SAY HELLO!"""
    print("Hello World!")

@task
def pep8():
    """CHECK THE CODE STYLE FOR PEP8"""
    local('pep8 .')

@task
def tag_version(version):
    """Tag NEW VERSION"""
    local("git tag %s" % version)
    local("git push origin %s" % version)

@task
def fetch_version(version):
    "Fetch Git Version"
    local('wget https://github.com/KFGameHacker/pythonPlayground/archive/%s.zip'%version)

@task
def test():
    """ RUN TEST """
    local("./manage.py test")