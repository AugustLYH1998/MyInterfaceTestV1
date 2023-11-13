        res = LoginApi.login(self.session, data1)
        # print(res.text)
        logging.debug(f'res.text:{res.text}')
        self.assertEquals(data2, res.json()['code'])