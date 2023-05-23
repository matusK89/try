def test_search_repo_positive(git_hub_api_client):
    """
    This test search for existing repo on Github
    """

    # prepare the existing repo name
    repo_name = 'python'

    # search for the repo from step #1
    repos_list = git_hub_api_client.search_repo(repo_name)

    # Validate the search returns results
    assert len(repos_list) != 0

def test_search_repo_negative(git_hub_api_client):
    """
    This test search for existing repo on Github
    """

    # prepare the existing repo name
    repo_name = 'sfdslfslkdfnsldkfnsldfnsdklf'

    # search for the repo from step #1
    repos_list = git_hub_api_client.search_repo(repo_name)

    # Validate the search returns results
    assert len(repos_list) == 0