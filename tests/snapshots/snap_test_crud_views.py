# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_list 1'] = '''<html>
<head>
<meta charset="utf-8"><meta content="width=device-width" name="viewport"><title>
</head><body>
<div class="cruds-list cruds-page">
<div class="cruds-list__header cruds-page__header">
<h1>
Authors
</h1>
</div><div class="cruds-list__actions cruds-page__actions">
<div class="cruds-actions hidden-print">
<a class="btn btn-primary cruds-actions__btn" href="/author/new/">
New Author
</a>
</div>
</div><div class="cruds-list__filters cruds-page__filters">
<div class="card cruds-filter">
<div class="card-body">
<h5 class="card-title">
Filter
</h5><form action method="GET">
<fieldset>
<div class="control-group" id="div_id_name">
<label class="control-label" for="id_name">
Name contains
</label><div class="controls">
<input class="textInput textinput" id="id_name" name="name" type="text">
</div>
</div><div class="control-group" id="div_id_birthday">
<label class="control-label" for="id_birthday">
Birthday
</label><div class="controls">
<input class="dateinput" id="id_birthday" name="birthday" type="text">
</div>
</div><div class="control-group" id="div_id_country">
<label class="control-label" for="id_country">
Country
</label><div class="controls">
<select class="select" id="id_country" name="country">
<option selected value>
---------
</option>
</select>
</div>
</div><div class="control-group" id="div_id_active">
<label class="control-label" for="id_active">
Active
</label><div class="controls">
<select class="nullbooleanselect" id="id_active" name="active">
<option selected value="unknown">
Unknown
</option><option value="true">
Yes
</option><option value="false">
No
</option>
</select>
</div>
</div>
</fieldset><button class="btn btn-info" type="submit">
submit
</button>
</form>
</div>
</div>
</div><div class="cruds-list__table cruds-page__content">
<div class="table-container">
<table class="table table--toggle-columns table-hover">
<thead>
<tr>
<th>
<input data-select-all type="checkbox">
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
</div><div class="cruds-list__pagination cruds-page__pagination">
</div>
</div>
</body>
</html>'''
