# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestPaginatorTags::test_default 1'] = '''







    <ul class="pagination">
        
            <li class="prev disabled"><a>← Previous</a></li>
        
        
            
                <li class="active"><a href="?page=1">1</a></li>
            
        
            
                <li class=""><a href="?page=2">2</a></li>
            
        
            
                <li class=""><a href="?page=3">3</a></li>
            
        
            
                <li class=""><a href="?page=4">4</a></li>
            
        
            
                <li class=""><a href="?page=5">5</a></li>
            
        
            
                <li class=""><a href="?page=6">6</a></li>
            
        
            
                <li class=""><a href="?page=7">7</a></li>
            
        
            
                <li class=""><a href="?page=8">8</a></li>
            
        
            
                <li class=""><a href="?page=9">9</a></li>
            
        
            
                <li class="disabled"><a href="#">…</a></li>
            
        
            
                <li class=""><a href="?page=20">20</a></li>
            
        
        
            <li class="next"><a href="?page=2">Next →</a></li>
        
    </ul>

'''

snapshots['TestPaginatorTags::test_default 2'] = '''







    <ul class="pagination">
        
            <li class="prev">
                <a href="?page=14">← Previous</a>
            </li>
        
        
            
                <li class=""><a href="?page=1">1</a></li>
            
        
            
                <li class="disabled"><a href="#">…</a></li>
            
        
            
                <li class=""><a href="?page=8">8</a></li>
            
        
            
                <li class=""><a href="?page=9">9</a></li>
            
        
            
                <li class=""><a href="?page=10">10</a></li>
            
        
            
                <li class=""><a href="?page=11">11</a></li>
            
        
            
                <li class=""><a href="?page=12">12</a></li>
            
        
            
                <li class=""><a href="?page=13">13</a></li>
            
        
            
                <li class=""><a href="?page=14">14</a></li>
            
        
            
                <li class="active"><a href="?page=15">15</a></li>
            
        
            
                <li class=""><a href="?page=16">16</a></li>
            
        
            
                <li class=""><a href="?page=17">17</a></li>
            
        
            
                <li class=""><a href="?page=18">18</a></li>
            
        
            
                <li class=""><a href="?page=19">19</a></li>
            
        
            
                <li class=""><a href="?page=20">20</a></li>
            
        
        
            <li class="next"><a href="?page=16">Next →</a></li>
        
    </ul>

'''
