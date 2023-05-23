def test_search_topics_positive(git_hub_api_client):
    """
    This is search for existing topics
    """

    # prepare topic name what we want to search
    topic_name = 'python'

    # prepare search for topic from #1
    topics_list = git_hub_api_client.search_topic(topic_name)

    # validate the search return results
    assert topic_name in topics_list

def test_search_topics_negative(git_hub_api_client):
    """
    This is search for existing topics
    """

    # prepare topic name what we want to search
    topic_name = 'blsdkafsdfsdfsdtoptoptop'

    # prepare search for topic from #1
    topics_list = git_hub_api_client.search_topic(topic_name)

    # validate the search return results
    assert topic_name not in topics_list

