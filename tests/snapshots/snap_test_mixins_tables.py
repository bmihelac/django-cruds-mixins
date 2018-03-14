# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TablesTest::test_custom_table 1'] = GenericRepr("b'\n\n\n\n\n<div class="table-container">
\n\n<table>
\n \n \n<thead>
\n<tr>
\n \n \n<th class="id orderable">
<a href="?sort=id">
ID
</a>
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
</th>\n \n \n
</tr>\n
</thead>\n \n \n \n<tbody>
\n \n \n<tr class="even">
\n \n<td class="id">
1
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
</td>\n \n
</tr>\n \n \n
</tbody>\n \n \n \n \n
</table>\n\n\n\n\n\n\n<ul class="pagination">
\n \n\n \n\n \n
</ul>\n\n\n\n\n
</div>\n\n\n'")

snapshots['TablesTest::test_default 1'] = GenericRepr("b'\n\n\n\n\n<div class="table-container">
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
</div>\n\n\n'")
