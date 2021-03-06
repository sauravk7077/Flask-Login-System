from urllib.parse import urlparse, urljoin
from flask import request
from flask_login import current_user

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc


def isAdmin():
    for role in current_user.roles:
        if role.name == 'admin':
            return True
    return False
