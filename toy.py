import random
import string

from requests_futures.sessions import FuturesSession


def random_chars(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


if __name__ == '__main__':

    # Make a session with a number of workers
    session = FuturesSession(max_workers=10)

    # Generate some fake urls
    urls = []
    for i in range(100):
        urls.append('http://httpbin.org/get?foo={}'.format(random_chars(6)))

    # Start a bunch of GET requests
    responses = [session.get(url) for url in urls]

    response44 = responses[44].result()
    print(response44.status_code)
    print(response44.content)

    response99 = responses[99].result()
    print(response99.status_code)
    print(response99.content)
