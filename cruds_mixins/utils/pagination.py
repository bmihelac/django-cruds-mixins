from urllib.parse import urlencode, parse_qs


def pagination_getvars(query, page_key='page'):
    """
    Removes ``page_key`` from query string and return it.

    >>> pagination_getvars("page=1&key=value")
    '&key=value'
    >>> pagination_getvars("")
    ''
    """
    getvars = parse_qs(query)
    getvars.pop(page_key, None)
    if not getvars:
        return ""
    return "&" + urlencode(getvars, True)
