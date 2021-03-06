from fabric.api import local 
from fabric.decorators import task

@task
def runserver():
    """RUN SERVER"""
    local("./manage.py runserver")

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