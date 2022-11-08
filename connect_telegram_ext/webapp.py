# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Cloudblue Connect
# All rights reserved.
#

import collections

import telegram.error
from connect.client import ConnectClient
from connect.eaas.core.decorators import (
    account_settings_page,
    router,
    web_app,
)
from connect.eaas.core.extension import WebApplicationBase
from connect.eaas.core.inject.synchronous import get_installation, get_installation_client
from fastapi import Depends
from fastapi import HTTPException
from starlette.status import HTTP_204_NO_CONTENT

from connect_telegram_ext.constants import Errors, EVENT_LIST
from connect_telegram_ext.models import (
    ErrorResponse, SettingsPayload, TestMessagePayload,
)
from connect_telegram_ext.telegram import TelegramClient


def _format_notification_settings(settings_dict):
    return_array = {}
    for event in EVENT_LIST:
        return_array[event.name] = {}
        return_array[event.name]['title'] = event.title
        return_array[event.name]['statuses'] = {}
        for status in event.statuses:
            if (
                'notifications' in settings_dict
            ) and (
                event.name in settings_dict['notifications']
            ) and (
                status in settings_dict['notifications'][event.name]['statuses']
            ):
                return_array[event.name]['statuses'][status] = settings_dict[
                    'notifications'
                ][event.name]['statuses'][status]
            else:
                return_array[event.name]['statuses'][status] = False
    return collections.OrderedDict(sorted(return_array.items()))


@web_app(router)
@account_settings_page('Settings', '/static/settings.html')
class TelegramNotifyWebApplication(WebApplicationBase):
    @router.get(
        '/settings',
        summary="Returns list of settings",
        response_model=SettingsPayload,
        responses={
            500: {
                "model": ErrorResponse,
                "description": "Something wrong happened on our side. There are some "
                               "hints in the response but usually they shouldn't help much",
            },
        },
        description="This function returns connectivity and notification settings",
    )
    def retrieve_settings(
            self,
            installation: dict = Depends(get_installation),
    ):
        try:
            settings = SettingsPayload(
                token=installation['settings'].get('token'),
                chatId=installation['settings'].get('chatId'),
                notifications=_format_notification_settings(installation['settings']),
            )
        except Exception as err:
            raise HTTPException(
                status_code=500,
                detail="Something went wrong on our side: " + str(err),
            )
        return settings

    @router.post(
        '/settings',
        summary="Saves the list of settings",
        response_model=SettingsPayload,
        responses={
            500: {
                "model": ErrorResponse,
                "description": "Something wrong happened on our side. There are some hints "
                               "in the response but usually they shouldn't help much ",
            },
        },
        description="This method saves given settings.",
    )
    def update_settings(
            self,
            payload: SettingsPayload,
            installation: dict = Depends(get_installation),
            installation_client: ConnectClient = Depends(get_installation_client),
    ):
        try:
            installation = installation_client('devops').installations[installation['id']].update(
                {'settings': payload.dict()},
            )
            return SettingsPayload(
                token=installation['settings'].get('token'),
                chatId=installation['settings'].get('chatId'),
                notifications=_format_notification_settings(installation['settings']),
            )
        except Exception as err:
            raise HTTPException(
                status_code=500,
                detail="Something went wrong on our side: " + str(err),
            )

    @router.post(
        '/test-message',
        summary="An endpoint to send a test message",
        status_code=HTTP_204_NO_CONTENT,
        responses={
            400: {
                "model": ErrorResponse,
                "description": "Something wrong with the payload, more info in the response",
            },
        },
        description="This method sends a test message to the telegram chat with given credentials",
    )
    def test_message(
            self,
            payload: TestMessagePayload,
            installation: dict = Depends(get_installation),
    ):
        if 'token' not in installation['settings'] or installation['settings']['token'] is None:
            raise HTTPException(status_code=400, detail=Errors.TOKEN_NOT_SET)
        if 'chatId' not in installation['settings'] or installation['settings']['chatId'] is None:
            raise HTTPException(status_code=400, detail=Errors.CHAT_ID_NOT_SET)
        try:
            TelegramClient(
                installation['settings']['token'],
                installation['settings']['chatId'],
            ).send_message(
                payload.message,
            )
        except telegram.error.TelegramError as err:
            raise HTTPException(status_code=400, detail=str(err))
        return
