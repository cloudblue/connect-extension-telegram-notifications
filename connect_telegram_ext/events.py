# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Cloudblue Connect
# All rights reserved.
#
import telegram.error
from connect.eaas.core.decorators import (event)
from connect.eaas.core.extension import EventsApplicationBase
from connect.eaas.core.responses import (
    BackgroundResponse,
)

from connect_telegram_ext.constants import Errors, Events
from connect_telegram_ext.models import Event
from connect_telegram_ext.telegram import TelegramClient


class TelegramNotifyApplication(EventsApplicationBase):
    def _get_settings_attr(self, path: str):
        tokens = path.split('.')
        value = self.installation['settings']
        for token in tokens:
            value = value.get(token)
            if not value or not isinstance(value, dict):
                break
        return value

    def _handle_event(self, request, event_type: Event):
        self.logger.info(f"Obtained {event_type.title} request with id {request['id']}")
        telegram_token = self._get_settings_attr('token')
        if not telegram_token:
            self.logger.error(Errors.TOKEN_NOT_SET)
            return BackgroundResponse.done()
        if self._get_settings_attr(
                f"notifications.{event_type.name}.statuses.{request[event_type.status_filed]}",
        ):
            try:
                TelegramClient(
                    telegram_token,
                    self._get_settings_attr('chatId'),
                ).send_message(
                    event_type.message_callback(event_type, self.client, request),
                )
            except telegram.error.TelegramError as err:
                self.logger.error(str(err))
                return BackgroundResponse.reschedule()
        else:
            self.logger.info(f"request with id {request['id']} skipped because of settings")
        return BackgroundResponse.done()

    @event(
        Events.INSTALLATION_STATUS_CHANGE.name,
        statuses=Events.INSTALLATION_STATUS_CHANGE.statuses,
    )
    def handle_installation_status_change(self, request):
        return self._handle_event(request, Events.INSTALLATION_STATUS_CHANGE)

    @event(
        Events.TIER_CONFIG_ADJUSTMENT_REQUEST_PROCESSING.name,
        statuses=Events.TIER_CONFIG_ADJUSTMENT_REQUEST_PROCESSING.statuses,
    )
    def handle_tier_config_adjustment_request_processing(self, request):
        return self._handle_event(request, Events.TIER_CONFIG_ADJUSTMENT_REQUEST_PROCESSING)

    @event(
        Events.TIER_CONFIG_CHANGE_REQUEST_PROCESSING.name,
        statuses=Events.TIER_CONFIG_CHANGE_REQUEST_PROCESSING.statuses,
    )
    def handle_tier_config_change_request_processing(self, request):
        return self._handle_event(request, Events.TIER_CONFIG_CHANGE_REQUEST_PROCESSING)

    @event(
        Events.ASSET_CANCEL_REQUEST_PROCESSING.name,
        statuses=Events.ASSET_CANCEL_REQUEST_PROCESSING.statuses,
    )
    def handle_asset_cancel_request_processing(self, request):
        return self._handle_event(request, Events.ASSET_CANCEL_REQUEST_PROCESSING)

    @event(
        Events.TIER_CONFIG_SETUP_REQUEST_PROCESSING.name,
        statuses=Events.TIER_CONFIG_SETUP_REQUEST_PROCESSING.statuses,
    )
    def handle_tier_config_setup_request_processing(self, request):
        return self._handle_event(request, Events.TIER_CONFIG_SETUP_REQUEST_PROCESSING)

    @event(
        Events.ASSET_RESUME_REQUEST_PROCESSING.name,
        statuses=Events.ASSET_RESUME_REQUEST_PROCESSING.statuses,
    )
    def handle_asset_resume_request_processing(self, request):
        return self._handle_event(request, Events.ASSET_RESUME_REQUEST_PROCESSING)

    @event(
        Events.ASSET_ADJUSTMENT_REQUEST_PROCESSING.name,
        statuses=Events.ASSET_ADJUSTMENT_REQUEST_PROCESSING.statuses,
    )
    def handle_asset_adjustment_request_processing(self, request):
        return self._handle_event(request, Events.ASSET_ADJUSTMENT_REQUEST_PROCESSING)

    @event(
        Events.ASSET_SUSPEND_REQUEST_PROCESSING.name,
        statuses=Events.ASSET_SUSPEND_REQUEST_PROCESSING.statuses,
    )
    def handle_asset_suspend_request_processing(self, request):
        return self._handle_event(request, Events.ASSET_SUSPEND_REQUEST_PROCESSING)

    @event(
        Events.TIER_ACCOUNT_UPDATE_REQUEST_PROCESSING.name,
        statuses=Events.TIER_ACCOUNT_UPDATE_REQUEST_PROCESSING.statuses,
    )
    def handle_tier_account_update_request_processing(self, request):
        return self._handle_event(request, Events.TIER_ACCOUNT_UPDATE_REQUEST_PROCESSING)

    @event(
        Events.ASSET_CHANGE_REQUEST_PROCESSING.name,
        statuses=Events.ASSET_CHANGE_REQUEST_PROCESSING.statuses,
    )
    def handle_asset_change_request_processing(self, request):
        return self._handle_event(request, Events.ASSET_CHANGE_REQUEST_PROCESSING)

    @event(
        Events.ASSET_PURCHASE_REQUEST_PROCESSING.name,
        statuses=Events.ASSET_PURCHASE_REQUEST_PROCESSING.statuses,
    )
    def handle_asset_purchase_request_processing(self, request):
        return self._handle_event(request, Events.ASSET_PURCHASE_REQUEST_PROCESSING)

    @event(
        Events.PART_USAGE_FILE_REQUEST_PROCESSING.name,
        statuses=Events.PART_USAGE_FILE_REQUEST_PROCESSING.statuses,
    )
    def handle_part_usage_file_request_processing(self, request):
        return self._handle_event(request, Events.PART_USAGE_FILE_REQUEST_PROCESSING)

    @event(
        Events.USAGE_FILE_REQUEST_PROCESSING.name,
        statuses=Events.USAGE_FILE_REQUEST_PROCESSING.statuses,
    )
    def handle_usage_file_request_processing(self, request):
        return self._handle_event(request, Events.USAGE_FILE_REQUEST_PROCESSING)

    @event(
        Events.HELPDESK_CASE_PROCESSING.name,
        statuses=Events.HELPDESK_CASE_PROCESSING.statuses,
    )
    def handle_helpdesk_case_processing(self, request):
        return self._handle_event(request, Events.HELPDESK_CASE_PROCESSING)
