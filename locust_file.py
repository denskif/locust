from locust import HttpLocust, TaskSet, task


list_game_headers = {
    'authority': "platform.today",
    'x-grpc-web': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    'content-type': "application/grpc-web+proto",
    'accept': "*/*",
    'origin': "https://platform.today",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://platform.today/en/casino",
    'accept-language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,es;q=0.5,pl;q=0.4,de;q=0.3,fr;q=0.2",
    'cookie': "LANG=en_GB; __ls_uid=d9dc9300-0f5d-4f5a-732d-668d4b1224f8; __ls_sid=d1b5a49a-3e67-4f24-4ee3-f9c9781b8ac7:1; __ls_exp=1586785498; _ga=GA1.2.1755809570.1586969312; __cfduid=d7c881dffc67ebde19d33a2457cabeb961588256546",
    'Cache-Control': "no-cache",
    'Postman-Token': "5cc0d4ad-9de0-456f-ab45-0d60262dd94a,9efa750c-df09-4a24-940a-8f651c9a22ed",
    'Host': "platform.today",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "94",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

list_game_payload = "\\u0000\\u0000\\u0000\\u0000\\u000c\\n\\u0004\\u0008\\u0014\\u0010\\u0001\\u0012\\u0004\\n\\u0002\\u0008\\u0001"


check_session_header = {
  'authority': 'platform.today',
  'x-grpc-web': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
  'content-type': 'application/grpc-web+proto',
  'accept': '*/*',
  'origin': 'https://platform.today',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://platform.today/en/casino',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,es;q=0.5,pl;q=0.4,de;q=0.3,fr;q=0.2',
  'cookie': 'LANG=en_GB; __ls_uid=d9dc9300-0f5d-4f5a-732d-668d4b1224f8; __ls_sid=d1b5a49a-3e67-4f24-4ee3-f9c9781b8ac7:1; __ls_exp=1586785498; _ga=GA1.2.1755809570.1586969312; __cfduid=d7c881dffc67ebde19d33a2457cabeb961588256546',
  'Content-Type': 'application/grpc-web+proto',
}

check_session_payload = "/u0000/u0000/u0000/u0000/u0000"

get_egt_jackpot_header = {
    'authority': 'platform.today',
    'x-grpc-web': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'content-type': 'application/grpc-web+proto',
    'accept': '*/*',
    'origin': 'https://platform.today',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://platform.today/en/casino',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,es;q=0.5,pl;q=0.4,de;q=0.3,fr;q=0.2',
    'cookie': 'LANG=en_GB; __ls_uid=d9dc9300-0f5d-4f5a-732d-668d4b1224f8; __ls_sid=d1b5a49a-3e67-4f24-4ee3-f9c9781b8ac7:1; __ls_exp=1586785498; _ga=GA1.2.1755809570.1586969312; __cfduid=d7c881dffc67ebde19d33a2457cabeb961588256546',
    'Content-Type': 'application/grpc-web+proto',
    'Cookie': '__cfduid=d5a8eef441bab1f686cbef796466cf3c81588848469'
}

get_egt_jackpot_payload = "u0000u0000u0000u0000u0005nu0003RON"

list_last_winners_header = {
    'authority': 'platform.today',
    'x-grpc-web': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'accept': '*/*',
    'origin': 'https://platform.today',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://platform.today/en/casino',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,es;q=0.5,pl;q=0.4,de;q=0.3,fr;q=0.2',
    'cookie': 'LANG=en_GB; __ls_uid=d9dc9300-0f5d-4f5a-732d-668d4b1224f8; __ls_sid=d1b5a49a-3e67-4f24-4ee3-f9c9781b8ac7:1; __ls_exp=1586785498; _ga=GA1.2.1755809570.1586969312; __cfduid=d7c881dffc67ebde19d33a2457cabeb961588256546',
    'content-type': 'application/grpc-web+proto',
    'Cookie': '__cfduid=d5a8eef441bab1f686cbef796466cf3c81588848469'
}

list_last_winners_payload = "/u0000/u0000/u0000/u0000/u0008/u0018/u00142/u0004/n/u0002/u0008/u0001"


list_top_winners_header = {
    'authority': 'platform.today',
    'x-grpc-web': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'content-type': 'application/grpc-web+proto',
    'accept': '*/*',
    'origin': 'https://platform.today',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://platform.today/en/casino',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,es;q=0.5,pl;q=0.4,de;q=0.3,fr;q=0.2',
    'cookie': 'LANG=en_GB; __ls_uid=d9dc9300-0f5d-4f5a-732d-668d4b1224f8; __ls_sid=d1b5a49a-3e67-4f24-4ee3-f9c9781b8ac7:1; __ls_exp=1586785498; _ga=GA1.2.1755809570.1586969312; __cfduid=d7c881dffc67ebde19d33a2457cabeb961588256546',
    'Cookie': '__cfduid=d5a8eef441bab1f686cbef796466cf3c81588848469'
}

list_top_winners_payload = "u0000u0000u0000u0000nu0018u0004 u00012u0004nu0002u0008u0001"


@task(1)
def list_games(l):
    l.client.post("/gapi/ccp.v2.casino.Games/ListGames", data=list_game_payload, headers=list_game_headers)


@task(2)
def check_session(l):
    l.client.post(
        "/gapi/egt.auth.v1.WebAuthService/CheckSession",
        data=check_session_payload,
        headers=check_session_header
    )


@task(3)
def get_egt_jackpot(l):
    l.client.post(
        "/gapi/ccp.v2.casino.Widgets/GetEgtJackpotStream",
        data=get_egt_jackpot_payload,
        headers=get_egt_jackpot_header
    )


@task(4)
def list_last_winners(l):
    l.client.post(
        "/gapi/ccp.v2.casino.Widgets/ListLastWinners",
        data=list_last_winners_payload,
        headers=list_last_winners_header
    )


@task(5)
def list_top_winners(l):
    l.client.post(
        "/gapi/ccp.v2.casino.Widgets/ListTopWinners",
        data=list_top_winners_payload,
        headers=list_top_winners_header
    )


class UserBehavior(TaskSet):
    tasks = {
        list_games: 1,
        get_egt_jackpot: 1,
        check_session: 1,
        list_last_winners: 1,
        list_top_winners: 1
    }

    @staticmethod
    def on_start():
        print(1)

    @staticmethod
    def on_stop():
        print(2)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000