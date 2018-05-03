# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TablesTest::test_default 1'] = '''<div class="table-container">
<table class="table table--toggle-columns table-bordered table-hover table-striped">
<thead>
<tr>
<th class="selection">
<input data-select-all type="checkbox" />
</th><th class="name orderable">
<a href="?sort=name">
Name
</a>
</th><th class="birthday orderable">
<a href="?sort=birthday">
Birthday
</a>
</th><th class="country orderable">
<a href="?sort=country">
Country
</a>
</th><th class="active orderable">
<a href="?sort=active">
Active
</a>
</th><th class="view_link">
Actions
</th>
</tr>
</thead><tbody>
<tr class="even">
<td class="selection">
<input name="selection" type="checkbox" value="1" />
</td><td class="name">
Foo bar
</td><td class="birthday">
01/01/2000
</td><td class="country">
—
</td><td class="active">
<span class="false">
✘
</span>
</td><td class="view_link">
<a href="/author/1/">
View
</a>
</td>
</tr>
</tbody>
</table><ul class="pagination" />
</div>'''

snapshots['TablesTest::test_custom_table 1'] = '''<div class="table-container">
<table>
<thead>
<tr>
<th class="id orderable">
<a href="?sort=id">
ID
</a>
</th><th class="name orderable">
<a href="?sort=name">
Name
</a>
</th><th class="birthday orderable">
<a href="?sort=birthday">
Birthday
</a>
</th><th class="country orderable">
<a href="?sort=country">
Country
</a>
</th><th class="active orderable">
<a href="?sort=active">
Active
</a>
</th>
</tr>
</thead><tbody>
<tr class="even">
<td class="id">
1
</td><td class="name">
Foo bar
</td><td class="birthday">
01/01/2000
</td><td class="country">
—
</td><td class="active">
<span class="false">
✘
</span>
</td>
</tr>
</tbody>
</table><ul class="pagination" />
</div>'''
