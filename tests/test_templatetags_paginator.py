from django.template import loader
from django.core.paginator import Paginator, Page


def test_paginator_tags(snapshot):
    objects = [
        'object %d' % i
        for i in range(100)
    ]
    paginator = Paginator(objects, 5)
    template = loader.get_template('cruds_mixins/partials/pagination.html')
    page = Page(objects, 1, paginator)
    c = {'page_obj': page, 'is_paginated': True}
    result = template.render(c)
    snapshot.assert_match(result)

    page = Page(objects, 15, paginator)
    c = {'page_obj': page, 'is_paginated': True}
    result = template.render(c)
    snapshot.assert_match(result)
