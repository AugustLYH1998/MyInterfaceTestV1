def my_assert(myself,res,status_code=None,code = None):
    myself.assertEqual(status_code, res.status_code)
    myself.assertEqual(code, res.json()['code'])
