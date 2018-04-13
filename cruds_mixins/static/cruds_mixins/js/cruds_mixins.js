/*global $ */

$(document).ready(function() {
  'use strict';

  $('table th.selection input[type=checkbox]').on('click', function() {
    var selected = $(this).is(':checked');
    var $table = $(this).parents('table');
    $('input[name=selection]', $table).prop('checked', selected);
  });
});
