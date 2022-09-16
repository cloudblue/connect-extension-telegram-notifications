# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Cloudblue Connect
# All rights reserved.
#
from fastapi import Body, Depends
from connect.client import ConnectClient
from connect.eaas.core.decorators import router, web_app
from connect.eaas.core.extension import WebAppExtension
from connect.eaas.core.inject.synchronous import get_installation, get_installation_client
from pydantic import BaseModel


class SettingsPayload(BaseModel):
    token: str
    chatId: int


@web_app(router)
class TelegramNotifyWebAppExtension(WebAppExtension):
    @router.get('/settings')
    def retrieve_settings(
        self,
        installation: dict = Depends(get_installation),     # noqa: B008
    ):
        return installation

    @router.post('/settings')
    async def update_settings(
        self,
        payload: SettingsPayload,
        installation: dict = Depends(get_installation),     # noqa: B008
        installation_client: ConnectClient = Depends(get_installation_client),     # noqa: B008
    ):
        installation = installation_client('devops').installations[installation['id']].update(
            {'settings': payload.dict()},
        )
        return installation_client('devops').installations[installation['id']].get()

    @router.get('/whoami')
    def whoami(
        self,
        installation_client: ConnectClient = Depends(get_installation_client),     # noqa: B008
    ):
        return installation_client.auth.action('context').get()
