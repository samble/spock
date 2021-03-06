""" spock.tests.stuff
"""
import unittest2 as unittest
from types import GeneratorType

from spock.aima import Expr
from spock import (predicate, symbol,Obligation, )

from spock.doctrine import TemporalDoctrine

s = symbol

import datetime
t = datetime.datetime.now()

class TemporalTests(unittest.TestCase):
    def setUp(self):
        self.kb = TemporalDoctrine()

    def test_obligation_basic(self):
        alice, bob, action = 'alice', 'bob', 'dinner'
        obl = Obligation(alice, bob, t, action)
        self.assertTrue(obl.expression.alfa == alice == obl._from)
        self.assertTrue(obl.expression.beta == bob == obl._to)
        return obl

    def test_commitments(self):
        obl = self.test_obligation_basic()
        alice, bob = obl.alfa, obl.beta
        self.kb.obligation(obl)
        alice_commitments = self.kb.commitments[alice]
        self.assertTrue(bob in alice_commitments.keys())
        self.assertTrue(obl in alice_commitments[bob])
