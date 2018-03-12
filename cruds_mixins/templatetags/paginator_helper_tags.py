from django import template

register = template.Library()


@register.simple_tag
def page_range(page_obj, window=7):
    """Return page numbers respecting window.
    """
    last_page = page_obj.paginator.num_pages
    start_page = max(page_obj.number - window, 1)
    end_page = min(page_obj.number + window + 1, last_page)
    page_numbers = list(range(start_page, end_page + 1))
    if 1 not in page_numbers:
        page_numbers.insert(0, None)
        page_numbers.insert(0, 1)
    if last_page not in page_numbers:
        page_numbers.append(None)
        page_numbers.append(last_page)
    return page_numbers
