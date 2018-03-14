# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCRUDListView::test_default 1'] = GenericRepr("b'\n<html>
\n<head>
\n<meta charset="utf-8" />\n<meta content="width=device-width" name="viewport" />\n<title />\n
</head>\n<body>
\n\n \n \n\n \n\n \n\n<h1 class="page-header">
\n Authors\n
</h1>\n\n\n \n<div class="actions">
\n \n \n \n \n<a class="btn btn btn-default hidden-print" href="/author/new/">
New Author
</a>\n \n \n \n \n
</div>\n\n\n\n\n\n\n\n\n<form action class="inline-form" method="get">
\n<fieldset>
\n \n\n<div class="control-group" id="div_id_name">
<label class=" control-label" for="id_name">
\n Name contains\n
</label><div class="controls">
<input class="textInput textinput" id="id_name" name="name" type="text" />
</div>
</div><div class="control-group" id="div_id_birthday">
<label class=" control-label" for="id_birthday">
\n Birthday\n
</label><div class="controls">
<input class="dateinput" id="id_birthday" name="birthday" type="text" />
</div>
</div><div class="control-group" id="div_id_country">
<label class=" control-label" for="id_country">
\n Country\n
</label><div class="controls">
<select class="select" id="id_country" name="country">
<option selected value>
---------
</option>\n\n
</select>
</div>
</div><div class="control-group" id="div_id_active">
<label class=" control-label" for="id_active">
\n Active\n
</label><div class="controls">
<select class="nullbooleanselect" id="id_active" name="active">
<option selected value="1">
Unknown
</option><option value="2">
Yes
</option><option value="3">
No
</option>\n\n
</select>
</div>
</div>\n\n<div class="control-group">
\n<button class="btn btn-primary" type="submit">
Filter
</button>\n
</div>\n
</fieldset>\n\n\n\n\n\n\n<div class="table-container">
\n\n<table class="table table--toggle-columns table-bordered table-hover table-striped">
\n \n \n<thead>
\n<tr>
\n \n \n<th class="selection">
<input data-select-all type="checkbox" />
</th>\n \n \n \n<th class="name orderable">
<a href="?sort=name">
Name
</a>
</th>\n \n \n \n<th class="birthday orderable">
<a href="?sort=birthday">
Birthday
</a>
</th>\n \n \n \n<th class="country orderable">
<a href="?sort=country">
Country
</a>
</th>\n \n \n \n<th class="active orderable">
<a href="?sort=active">
Active
</a>
</th>\n \n \n \n<th class="view_link">
Actions
</th>\n \n \n
</tr>\n
</thead>\n \n \n \n<tbody>
\n \n \n<tr class="even">
\n \n<td class="selection">
<input name="selection" type="checkbox" value="1" />
</td>\n \n<td class="name">
Foo bar
</td>\n \n<td class="birthday">
01/01/2000
</td>\n \n<td class="country">
\xe2\x80\x94
</td>\n \n<td class="active">
<span class="false">
\xe2\x9c\x98
</span>
</td>\n \n<td class="view_link">
<a href="/author/1/">
View
</a>
</td>\n \n
</tr>\n \n \n
</tbody>\n \n \n \n \n
</table>\n\n\n\n\n\n\n<ul class="pagination">
\n \n\n \n\n \n
</ul>\n\n\n\n\n
</div>\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
</form>
</body>\n
</html>\n'")
