

def crawl(url):
    """Take in a url, return a dictionary of url with links."""

    # call get_links on input url
    # get_links returns a set of links
    # build dictionary with url as key and returned links as value
    # call the get links on each in value

    # create a list to store each link we need to visit
    to_visit = [url]


    # initialize a dictionary to store the url with their links
    output = {}


    # iterate over the list
    # create a key value pair with the url as the key and the links as a set of values
    # add other urls to to visit

    for url in to_visit:
        if url in output:
            continue
        else:
            output[url] = get_links(url)
            to_visit.extend(output[url])


    return output


def get_links(url):

    if url == "foo.com":
        return ["bar.com", "baz.com"]
    elif url == "bar.com":
        return ["baz.com", "bar.com"]
    elif url == "baz.com":
        return ["foo.com"]


print crawl("foo.com")
