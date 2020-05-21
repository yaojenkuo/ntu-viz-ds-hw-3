class TestHomework3(unittest.TestCase):
    def test_find_divisors(self):
        self.assertEqual(find_divisors(1), {1})
        self.assertEqual(find_divisors(2), {1, 2})
        self.assertEqual(find_divisors(3), {1, 3})
    def test_find_primes(self):
        self.assertEqual(find_primes(1, 5), [2, 3, 5])
        self.assertEqual(find_primes(1, 10), [2, 3, 5, 7])
        self.assertEqual(find_primes(2, 17), [2, 3, 5, 7, 11, 13, 17])
    def test_calc_daily_increase(self):
        self.assertEqual(calc_daily_increase([1, 2, 3]), [1, 1, 1])
        self.assertEqual(calc_daily_increase([2, 3, 4]), [2, 1, 1])
        self.assertEqual(calc_daily_increase([5, 5, 6, 6]), [5, 0, 1, 0])
    def test_calc_std(self):
        self.assertEqual(calc_std(1, 2, 3, 4), '1.12')
        self.assertEqual(calc_std(1, 2, 3, 4, 5), '1.41')
        self.assertEqual(calc_std(1, 2, 3, 4, 5, 6, 7), '2.00')
    def test_check_bailout(self):
        self.assertEqual(check_bailout('臺北市', 34000, 500000, 3), '核發1萬元')
        self.assertEqual(check_bailout('非六都之縣市', 34000, 500000, 3), '不符資格')
        self.assertEqual(check_bailout('臺北市', 20000, 500000, 3), '核發1-3萬元')
        self.assertEqual(check_bailout('台北市', 34000, 500000, 3), '請重新輸入居住縣市別')

suite = unittest.TestLoader().loadTestsFromTestCase(TestHomework3)
runner = unittest.TextTestRunner(verbosity=2,stream=sys.stderr)
test_results = runner.run(suite)