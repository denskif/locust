import urllib3
from locust import HttpUser, task, between

import header_data
import payload_data
import urls


urllib3.disable_warnings()


class WebsiteUser(HttpUser):
    wait_time = between(0, 1)

    @task
    def list_games(self):
        self.client.post(
            urls.LIST_GAMES,
            data=payload_data.list_game_payload,
            headers=header_data.list_game_headers,
            verify=False
        )

    @task
    def check_session(self):
        self.client.post(
            urls.CHECK_SESSION,
            data=payload_data.check_session_payload,
            headers=header_data.check_session_header,
            verify=False
        )

    @task
    def get_egt_jackpot(self):
        self.client.post(
            urls.EGT_JACKPOT_STREAM,
            data=payload_data.get_egt_jackpot_payload,
            headers=header_data.get_egt_jackpot_header,
            verify=False
        )

    @task
    def list_last_winners(self):
        self.client.post(
            urls.LIST_LAST_WINNERS,
            data=payload_data.list_last_winners_payload,
            headers=header_data.list_last_winners_header,
            verify=False
        )

    @task
    def list_top_winners(self):
        self.client.post(
            urls.LIST_TOP_WINNERS,
            data=payload_data.list_top_winners_payload,
            headers=header_data.list_top_winners_header,
            verify=False
        )

    def on_start(self):
        print('User started')

    def on_stop(self):
        print(2)
