# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TablesTest::test_default 1'] = b'\n\n\n\n\n<div class="table-container">\n\n<table class="table table-bordered table-striped table-hover table--toggle-columns">\n    \n    \n    <thead>\n        <tr>\n        \n            \n            <th class="selection"><input type="checkbox" data-select-all=""/></th>\n            \n        \n            \n            <th class="name orderable"><a href="?sort=name">Name</a></th>\n            \n        \n            \n            <th class="birthday orderable"><a href="?sort=birthday">Birthday</a></th>\n            \n        \n            \n            <th class="view_link">Actions</th>\n            \n        \n        </tr>\n    </thead>\n    \n    \n    \n    <tbody>\n         \n        \n        <tr class="even">\n            \n                <td class="selection"><input type="checkbox" name="selection" value="1"/></td>\n            \n                <td class="name">Foo bar</td>\n            \n                <td class="birthday">01/01/2000 midnight</td>\n            \n                <td class="view_link"></td>\n            \n        </tr>\n        \n        \n    </tbody>\n    \n    \n    \n    \n</table>\n\n\n\n\n\n\n<ul class="pagination">\n    \n\n    \n\n    \n</ul>\n\n\n\n\n</div>\n\n\n'
