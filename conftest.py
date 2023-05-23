import pytest
from src.user import User
from src.applications.api.github_api_client import GitHubAPIClient
from src.config.config import Config


@pytest.fixture(scope = 'session')
def user_fixture():
    # create a user -> precondition
    user_name = User.username
    user = dict(name = user_name)  # user.create()
    print(f"User {user_name} created")
    
    # execute test -> test steps
    yield user

    # remove a user -> postcondition
    user = None  # user.remove()
    print(f"User {user_name} removed")

def pytest_html_report_title(report):
    report.title = "My special report!"


@pytest.fixture(scope='module')
def git_hub_api_client():
    api = GitHubAPIClient()
    api.login(Config.get_property('USERNAME'), Config.get_property('PASSWORD'))

    yield api

    api.logout()