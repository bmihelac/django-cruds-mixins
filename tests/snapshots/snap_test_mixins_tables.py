# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_default 1'] = '''<div class="table-container">
<table class="table table--toggle-columns table-hover">
<thead>
<tr>
<th>
<input data-select-all="" type="checkbox">
</th><th class="orderable">
<a href="?sort=name">
Name
</a>
</th><th class="orderable">
<a href="?sort=birthday">
Birthday
</a>
</th><th class="orderable">
<a href="?sort=country">
Country
</a>
</th><th class="orderable">
<a href="?sort=active">
Active
</a>
</th><th>
Actions
</th>
</tr>
</thead><tbody>
</table>
</div>'''

snapshots['test_custom_table 1'] = '''<div class="table-container">
<table>
<thead>
<tr>
<th class="orderable">
<a href="?sort=id">
ID
</a>
</th><th class="orderable">
<a href="?sort=name">
Name
</a>
</th><th class="orderable">
<a href="?sort=birthday">
Birthday
</a>
</th><th class="orderable">
<a href="?sort=country">
Country
</a>
</th><th class="orderable">
<a href="?sort=active">
Active
</a>
</th>
</tr>
</thead><tbody>
</table>
</div>'''
