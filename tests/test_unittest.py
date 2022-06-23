import unittest
from parameterized import parameterized
from main import create_folder
import requests

FIXTURE = [
    ("https://cloud-api.yandex.net/v1/disk/resources", 'AQAAAAAUmhQUAADLWyZhDEGPGUyWoONYkGs_ckQ')
]


class TestFunction(unittest.TestCase):


    @parameterized.expand(FIXTURE)
    def test_response_status_code(self, url, token):
        response = create_folder(url, token)
        self.assertEqual(response.status_code, 201) # проверили, что код ответа 201
        # далее проверяем наличие папки на яндекс диске
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(token)
                   }
        params = {"path": 'Test'}
        folder_exist = requests.get(url, params=params, headers=headers)
        self.assertEqual(folder_exist.status_code, 200)


    def test_fail(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        token = 'AQAAAAAUmhQUAADLWyZhDEGPGUyWoONYkGs' #неправильный токен
        self.assertNotEqual(create_folder(url, token), 201) # проверили, что с неверным токеном код не работает






