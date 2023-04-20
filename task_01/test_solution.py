import logging
from unittest import TestCase

try:
    from solution import calculate_LNC
except:
    from .solution import calculate_LNC


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestSolution(TestCase):
    def test_case_01(self):
        lnc, found_coins = calculate_LNC([1, 5, 7, 9, 11], 25)
        logger.debug(f"{lnc} {found_coins}")
        self.assertEqual(lnc, 3)

    def test_case_02(self):
        lnc, found_coins = calculate_LNC([1, 5, 7, 9, 11], 14)
        logger.debug(f"{lnc} {found_coins}")
        self.assertEqual(lnc, 2)

    def test_case_03(self):
        lnc, found_coins = calculate_LNC([7, 9], 20)
        logger.debug(f"{lnc} {found_coins}")
        self.assertEqual(lnc, -1)
