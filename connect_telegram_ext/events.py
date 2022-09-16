# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Cloudblue Connect
# All rights reserved.
#
from connect.eaas.core.decorators import (
    event,
)
from connect.eaas.core.extension import EventsExtension as BaseExtension
from connect.eaas.core.responses import (
    BackgroundResponse,
)

from connect_telegram_ext.telegram import TelegramClient


class TelegramNotifyExtension(BaseExtension):
    @event(
        'installation_status_change',
        statuses=[
            'installed', 'uninstalled',
        ],
    )
    def handle_installation_status_change(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if 'token' in self.installation['settings']:
            TelegramClient(self.installation['settings']['token'], self.installation['settings']['chatId']).send_message(
                f"Installation status change received {request['id']}",
            )
        return BackgroundResponse.done()

    @event(
        'tier_config_adjustment_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'inquiring',
        ],
    )
    def handle_tier_config_adjustment_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if 'token' in self.installation['settings']:
            TelegramClient(self.installation['settings']['token'], self.installation['settings']['chatId']).send_message(
                f"Tier config adjustment received {request['id']}",
            )
        return BackgroundResponse.done()

    @event(
        'tier_config_change_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'inquiring',
        ],
    )
    def handle_tier_config_change_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if 'token' in self.installation['settings']:
            TelegramClient(self.installation['settings']['token'], self.installation['settings']['chatId']).send_message(
                f"Tier config change received {request['id']}",
            )
        return BackgroundResponse.done()

    @event(
        'asset_cancel_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'inquiring', 'scheduled', 'revoking',
            'revoked',
        ],
    )
    def handle_asset_cancel_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if 'token' in self.installation['settings']:
            TelegramClient(self.installation['settings']['token'], self.installation['settings']['chatId']).send_message(
                f"Asset cancel request received {request['id']}",
            )
        return BackgroundResponse.done()

    @event(
        'tier_config_setup_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'inquiring',
        ],
    )
    def handle_tier_config_setup_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if 'token' in self.installation['settings']:
            TelegramClient(self.installation['settings']['token'], self.installation['settings']['chatId']).send_message(
                f"Tier config setup received {request['id']}",
            )
        return BackgroundResponse.done()

    @event(
        'asset_resume_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'inquiring', 'scheduled', 'revoking',
            'revoked',
        ],
    )
    def handle_asset_resume_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if 'token' in self.installation['settings']:
            TelegramClient(self.installation['settings']['token'], self.installation['settings']['chatId']).send_message(
                f"Asset resume request received {request['id']}",
            )
        return BackgroundResponse.done()

    @event(
        'asset_adjustment_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'inquiring', 'scheduled', 'revoking',
            'revoked',
        ],
    )
    def handle_asset_adjustment_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if 'token' in self.installation['settings']:
            TelegramClient(self.installation['settings']['token'], self.installation['settings']['chatId']).send_message(
                f"Asset adjustment request received {request['id']}",
            )
        return BackgroundResponse.done()

    @event(
        'asset_suspend_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'inquiring', 'scheduled', 'revoking',
            'revoked',
        ],
    )
    def handle_asset_suspend_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if 'token' in self.installation['settings']:
            TelegramClient(self.installation['settings']['token'], self.installation['settings']['chatId']).send_message(
                f"Asset suspend request received {request['id']}",
            )
        return BackgroundResponse.done()

    @event(
        'tier_account_update_request_processing',
        statuses=[
            'pending', 'accepted', 'ignored',
        ],
    )
    def handle_tier_account_update_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if 'token' in self.installation['settings']:
            TelegramClient(self.installation['settings']['token'], self.installation['settings']['chatId']).send_message(
                f"Tier account update received {request['id']}",
            )
        return BackgroundResponse.done()

    @event(
        'asset_change_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'inquiring', 'scheduled', 'revoking',
            'revoked',
        ],
    )
    def handle_asset_change_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if 'token' in self.installation['settings']:
            TelegramClient(self.installation['settings']['token'], self.installation['settings']['chatId']).send_message(
                f"Asset change request received {request['id']}",
            )
        return BackgroundResponse.done()

    @event(
        'asset_purchase_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'inquiring', 'scheduled', 'revoking',
            'revoked',
        ],
    )
    def handle_asset_purchase_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if 'token' in self.installation['settings']:
            TelegramClient(self.installation['settings']['token'], self.installation['settings']['chatId']).send_message(
                f"Asset purchase request received {request['id']}",
            )
        return BackgroundResponse.done()

    @event(
        'part_usage_file_request_processing',
        statuses=[
            'draft', 'ready', 'closed',
            'failed',
        ],
    )
    def handle_part_usage_file_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if 'token' in self.installation['settings']:
            TelegramClient(self.installation['settings']['token'], self.installation['settings']['chatId']).send_message(
                f"Part usage file request received {request['id']}",
            )
        return BackgroundResponse.done()

    @event(
        'usage_file_request_processing',
        statuses=[
            'pending', 'accepted', 'ignored',
        ],
    )
    def handle_usage_file_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if 'token' in self.installation['settings']:
            TelegramClient(self.installation['settings']['token'], self.installation['settings']['chatId']).send_message(
                f"Usage file request received {request['id']}",
            )
        return BackgroundResponse.done()
