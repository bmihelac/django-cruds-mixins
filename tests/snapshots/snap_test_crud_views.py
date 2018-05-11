# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_list 1'] = '''<html>
<head>
<meta charset="utf-8" /><meta content="width=device-width" name="viewport" /><title />
</head><body>
<h1 class="page-header">
Authors
</h1><div class="actions">
<a class="btn btn-primary hidden-print" href="/author/new/">
New Author
</a>
</div><form action class="inline-form" method="get">
<fieldset>
<div class="control-group" id="div_id_name">
<label class=" control-label" for="id_name">
Name contains
</label><div class="controls">
<input class="textInput textinput" id="id_name" name="name" type="text" />
</div>
</div><div class="control-group" id="div_id_birthday">
<label class=" control-label" for="id_birthday">
Birthday
</label><div class="controls">
<input class="dateinput" id="id_birthday" name="birthday" type="text" />
</div>
</div><div class="control-group" id="div_id_country">
<label class=" control-label" for="id_country">
Country
</label><div class="controls">
<select class="select" id="id_country" name="country">
<option selected value>
---------
</option>
</select>
</div>
</div><div class="control-group" id="div_id_active">
<label class=" control-label" for="id_active">
Active
</label><div class="controls">
<select class="nullbooleanselect" id="id_active" name="active">
<option selected value="1">
Unknown
</option><option value="2">
Yes
</option><option value="3">
No
</option>
</select>
</div>
</div><div class="control-group">
<button class="btn btn-primary" type="submit">
Filter
</button>
</div>
</fieldset><div class="table-container">
<table class="table table--toggle-columns table-hover">
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
</thead><tbody />
</table>
</div>
</form>
</body>
</html>'''
