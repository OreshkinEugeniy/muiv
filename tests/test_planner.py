import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from planner import order, load, save

class PlannerTests(unittest.TestCase):
    def test_order(self):
        tasks=[dict(id=i,deadline=d,priority=p,done=s) for i,d,p,s in [(1,'2027-01-02',3,False),(2,'2027-01-01',1,False),(3,'2027-01-01',3,False),(4,'2026-01-01',3,True)]]
        self.assertEqual([t['id'] for t in order(tasks)],[3,2,1,4])
    def test_empty(self): self.assertEqual(order([]),[])
    def test_storage(self):
        with TemporaryDirectory() as d:
            p=Path(d)/'tasks.json'; self.assertEqual(load(p),[]); save(p,[{'title':'Задача'}]); self.assertEqual(load(p),[{'title':'Задача'}])
