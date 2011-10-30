import unittest
import sys
from os.path import dirname, abspath, join, isdir, isfile

import pyx12.dataele 
from pyx12.errors import EngineError
import pyx12.params
from pyx12.tests.support import getMapPath

class BadDataElem(unittest.TestCase):
    def setUp(self):
        map_path = getMapPath()
        params = pyx12.params.params()
        if map_path is None:
            map_path = params.get('map_path')
        self.de = pyx12.dataele.DataElements(map_path)

    def testNone(self):
        self.failUnlessRaises(EngineError, self.de.get_by_elem_num, None)

    def testInvalid(self):
        self.failUnlessRaises(EngineError, self.de.get_by_elem_num, '28902')
        self.failUnlessRaises(EngineError, self.de.get_by_elem_num, '0')
        self.failUnlessRaises(EngineError, self.de.get_by_elem_num, '99991')

class LookupDataElem(unittest.TestCase):

    def setUp(self):
        map_path = getMapPath()
        params = pyx12.params.params()
        if map_path is None:
            map_path = params.get('map_path')
        self.de = pyx12.dataele.DataElements(map_path)
    
    def testOK_AN(self):
        self.assertEqual(self.de.get_by_elem_num('1204'), {'max_len': 50, 'name': 'Plan Coverage Description', 'data_type': 'AN', 'min_len': 1})

    def testOK_ID(self):
        self.assertEqual(self.de.get_by_elem_num('116'), {'max_len': 15, 'name': 'Postal Code', 'data_type': 'ID', 'min_len': 3})

    def testOK_N(self):
        self.assertEqual(self.de.get_by_elem_num('554'), {'max_len': 6, 'name': 'Assigned Number', 'data_type': 'N0', 'min_len': 1})

    def testOK_DT(self):
        self.assertEqual(self.de.get_by_elem_num('373'), 
                {'max_len': 8, 'name': 'Date', 'data_type': 'DT', 'min_len': 8})

    def testOK_TM(self):
        self.assertEqual(self.de.get_by_elem_num('337'), {'max_len': 8, 'name': 'Time', 'data_type': 'TM', 'min_len': 4})
