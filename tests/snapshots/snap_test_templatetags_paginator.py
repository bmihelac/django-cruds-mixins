# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_paginator_tags 1'] = '''



<div class="cruds-pagination">
  
  <p class="cruds-pagination__title">
    100 results. Displaying: 100.
  </p>

  <ul class="cruds-pagination__pagination pagination">
      
          <li class="page-item prev disabled"><a class="page-link" >← Previous</a></li>
      
      
          
              <li class="page-item active"><a class="page-link" href="?page=1">1</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=2">2</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=3">3</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=4">4</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=5">5</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=6">6</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=7">7</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=8">8</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=9">9</a></li>
          
      
          
              <li class="page-item disabled"><a class="page-link"  href="#">…</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=20">20</a></li>
          
      
      
          <li class="page-item next"><a class="page-link" href="?page=2">Next →</a></li>
      
  </ul>
</div>

'''

snapshots['test_paginator_tags 2'] = '''



<div class="cruds-pagination">
  
  <p class="cruds-pagination__title">
    100 results. Displaying: 100.
  </p>

  <ul class="cruds-pagination__pagination pagination">
      
          <li class="page-item prev">
              <a class="page-link" href="?page=14">← Previous</a>
          </li>
      
      
          
              <li class="page-item "><a class="page-link" href="?page=1">1</a></li>
          
      
          
              <li class="page-item disabled"><a class="page-link"  href="#">…</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=8">8</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=9">9</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=10">10</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=11">11</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=12">12</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=13">13</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=14">14</a></li>
          
      
          
              <li class="page-item active"><a class="page-link" href="?page=15">15</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=16">16</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=17">17</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=18">18</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=19">19</a></li>
          
      
          
              <li class="page-item "><a class="page-link" href="?page=20">20</a></li>
          
      
      
          <li class="page-item next"><a class="page-link" href="?page=16">Next →</a></li>
      
  </ul>
</div>

'''
