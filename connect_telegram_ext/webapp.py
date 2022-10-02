# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Cloudblue Connect
# All rights reserved.
#

import telegram.error
import collections
from connect.client import ConnectClient
from connect.eaas.core.decorators import (
    account_settings_page,
    router,
    web_app,
)
from connect.eaas.core.extension import WebAppExtension
from connect.eaas.core.inject.synchronous import get_installation, get_installation_client
from fastapi import Depends
from pydantic import BaseModel

from connect_telegram_ext.constants import EVENT_LIST
from connect_telegram_ext.telegram import TelegramClient


class SettingsPayload(BaseModel):
    token: str
    chatId: int
    notifications: dict


class TestMessagePayload(BaseModel):
    message: str


def _format_notification_settings(settings_dict):
    return_array = {}
    for event in EVENT_LIST:
        return_array[event.name] = {}
        return_array[event.name]['title'] = event.title
        return_array[event.name]['statuses'] = {}
        for status in event.statuses:
            if ('notifications' in settings_dict) and (
                    event.name in settings_dict['notifications']
            ):
                return_array[event.name]['statuses'][status] = settings_dict[
                    'notifications'
                ][event.name]['statuses'][status]
            else:
                return_array[event.name]['statuses'][status] = False
    return collections.OrderedDict(sorted(return_array.items()))


@web_app(router)
@account_settings_page('My Settings', '/static/settings.html')
class TelegramNotifyWebAppExtension(WebAppExtension):
    @router.get('/settings')
    def retrieve_settings(
            self,
            installation: dict = Depends(get_installation),  # noqa: B008
    ):
        settings = SettingsPayload(
            token=installation['settings'].get('token', ''),
            chatId=installation['settings'].get('chatId', 0),
            notifications=_format_notification_settings(installation['settings']),
        )
        return settings.dict()

    @router.post('/settings')
    async def update_settings(
            self,
            payload: SettingsPayload,
            installation: dict = Depends(get_installation),  # noqa: B008
            installation_client: ConnectClient = Depends(get_installation_client),  # noqa: B008
    ):
        installation = installation_client('devops').installations[installation['id']].update(
            {'settings': payload.dict()},
        )
        return installation_client('devops').installations[installation['id']].get()

    @router.post('/test-message')
    async def test_message(
            self,
            payload: TestMessagePayload,
            installation: dict = Depends(get_installation),  # noqa: B008
    ):
        if 'token' in installation['settings']:
            try:
                TelegramClient(
                    installation['settings']['token'],
                    installation['settings']['chatId'],
                ).send_message(
                    payload.message,
                )
                return {
                    'status': 'OK',
                    'error': '',
                }
            except telegram.error.TelegramError as err:
                return {
                    'status': 'FAIL',
                    'error': str(err),
                }
        return {
            'status': 'FAIL',
            'error': 'Token not found',
        }

    @router.get('/whoami')
    def whoami(
            self,
            installation_client: ConnectClient = Depends(get_installation_client),  # noqa: B008
    ):
        return installation_client.auth.action('context').get()
