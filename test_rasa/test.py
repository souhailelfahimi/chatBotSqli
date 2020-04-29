from stackapi import StackAPI


def search(message):
    SITE = StackAPI('stackoverflow')
    SITE.page_size = 3
    SITE.max_pages = 1
    comments = SITE.fetch('similar', sort='relevance', title=message)
    result = []
    for i in comments['items']:
        result.append(i['link'])
    return result
