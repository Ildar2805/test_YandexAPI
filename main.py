import requests


def create_folder(url, token):
    create_folder_url = url
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }
    params = {"path": 'Test'}
    response = requests.put(create_folder_url, params=params, headers=headers)
    return response



def main():
    token = 'AQAAAAAUmhQUAADLWyZhDEGPGUyWoONYkGs_ckQ'
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    result = create_folder(url, token)
    return result


if __name__ == '__main__':
    main()

