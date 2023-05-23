def test_search_repo_positive(git_hub_api_client):
    """
    This test search for existing repo on Github
    """

    # prepare the existing repo name
    repo_name = 'python'

    # search for the repo from step #1
    repos_list = git_hub_api_client.search_repo(repo_name)

    # Validate the search returns results
    assert repo_name in repos_list

def test_search_repo_negative(git_hub_api_client):
    """
    This test search for existing repo on Github
    """

    # prepare the existing repo name
    repo_name = 'sfdslfslkdfnsldkfnsldfnsdklf'

    # search for the repo from step #1
    repos_list = git_hub_api_client.search_repo(repo_name)

    # Validate the search returns results
    assert repo_name not in repos_list

def test_search_repo_millions_result(git_hub_api_client):
    """
    This test search for existing repo on Github
    """

    # prepare the existing repo name
    repo_name = 'a'
    per_page = 100

    # search for the repo from step #1
    repos_list = git_hub_api_client.search_repo(repo_name, per_page)

    # Validate the search returns results
    assert len(repos_list) == per_page