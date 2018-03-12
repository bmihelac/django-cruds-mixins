# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCRUDListView::test_default 1'] = b'<!DOCTYPE html>\n<html>\n  <head>\n    <meta charset="utf-8" />\n    <meta name="viewport" content="width=device-width" />\n    <title></title>\n  </head>\n  <body>\n\n    \n      \n\n    \n\n    \n\n<h1 class="page-header">\n  Authors\n</h1>\n\n\n  \n  <div class="actions">\n    \n      \n        \n          \n            <a href="/author/new/" class="btn btn btn-default hidden-print">New Author</a>\n          \n        \n      \n    \n  </div>\n\n\n\n\n\n\n\n\n<form action="" method="get" class="inline-form">\n  <fieldset>\n    \n\n<div id="div_id_name" class="control-group"> <label for="id_name" class="control-label ">\n                Name contains\n            </label> <div class="controls"> <input type="text" name="name" class="textinput textInput" id="id_name" /> </div> </div> <div id="div_id_birthday" class="control-group"> <label for="id_birthday" class="control-label ">\n                Birthday\n            </label> <div class="controls"> <input type="text" name="birthday" class="datetimeinput" id="id_birthday" /> </div> </div> <div id="div_id_active" class="control-group"> <label for="id_active" class="control-label ">\n                Active\n            </label> <div class="controls"> <select name="active" class="nullbooleanselect" id="id_active"> <option value="1" selected>Unknown</option> <option value="2">Yes</option> <option value="3">No</option>\n\n</select> </div> </div>\n\n    <div class="control-group">\n      <button type="submit" class="btn btn-primary">Filter</button>\n    </div>\n  </fieldset>\n\n\n\n\n\n\n<div class="table-container">\n\n<table class="table table-bordered table-striped table-hover table--toggle-columns">\n    \n    \n    <thead>\n        <tr>\n        \n            \n            <th class="selection"><input type="checkbox" data-select-all=""/></th>\n            \n        \n            \n            <th class="name orderable"><a href="?sort=name">Name</a></th>\n            \n        \n            \n            <th class="birthday orderable"><a href="?sort=birthday">Birthday</a></th>\n            \n        \n            \n            <th class="active orderable"><a href="?sort=active">Active</a></th>\n            \n        \n            \n            <th class="view_link">Actions</th>\n            \n        \n        </tr>\n    </thead>\n    \n    \n    \n    <tbody>\n         \n        \n        <tr class="even">\n            \n                <td class="selection"><input type="checkbox" name="selection" value="1"/></td>\n            \n                <td class="name">Foo bar</td>\n            \n                <td class="birthday">01/01/2000 midnight</td>\n            \n                <td class="active"><span class="false">\xe2\x9c\x98</span></td>\n            \n                <td class="view_link"><a href="/author/1/">View</a></td>\n            \n        </tr>\n        \n        \n    </tbody>\n    \n    \n    \n    \n</table>\n\n\n\n\n\n\n<ul class="pagination">\n    \n\n    \n\n    \n</ul>\n\n\n\n\n</div>\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n  </body>\n</html>\n'
