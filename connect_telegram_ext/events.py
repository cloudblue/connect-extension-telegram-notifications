# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Cloudblue Connect
# All rights reserved.
#
import telegram.error
from connect.eaas.core.decorators import (
    event, variables,
)
from connect.eaas.core.extension import EventsExtension as BaseExtension
from connect.eaas.core.responses import (
    BackgroundResponse,
)

from connect_telegram_ext.constants import Errors, Event, Events
from connect_telegram_ext.telegram import TelegramClient
import connect_telegram_ext.messages as event_messages


@variables([{
    "name": "PORTAL_URL",
    "initial_value": "https://change.me/",
}])
class TelegramNotifyExtension(BaseExtension):
    def _get_object_link(self, request, event_type):
        domain = self.installation_client.branding.action('portal').get()['domain']
        return f"https://{domain}/{event_type.path}/{request['id']}"

    def _get_message(self, request, event_type: Event):
        message_template = None
        try:
            message_template = vars(event_messages)[
                f"{event_type.name.upper()}_{request[event_type.status_filed]}"
            ]
        except KeyError:
            pass

        if not message_template:
            try:
                message_template = vars(event_messages)[f"{event_type.name.upper()}"]
            except KeyError:
                pass

        if not message_template:
            message_template = event_messages.DEFAULT_MESSAGE

        return message_template.format(
            object_link=self._get_object_link(request, event_type),
            object_status=request[event_type.status_filed],
            **request,
        ).replace('-', '\-').replace('.', '\.').replace('!', '\!')  # noqa: W605

    def _handle_event(self, request, event_type: Event):
        self.logger.info(f"Obtained {event_type.title} request with id {request['id']}")
        if 'token' not in self.installation['settings']:
            self.logger.error(Errors.TOKEN_NOT_SET)
            return BackgroundResponse.fail(Errors.TOKEN_NOT_SET)
        try:
            if self.installation['settings'][
                'notifications'
            ][event_type.name]['statuses'][request[event_type.status_filed]]:
                TelegramClient(
                    self.installation['settings']['token'],
                    self.installation['settings']['chatId'],
                ).send_message(
                    self._get_message(request, event_type),
                )
            else:
                self.logger.info(f"request with id {request['id']} skipped because of settings")
        except telegram.error.TelegramError as err:
            self.logger.error(str(err))
            return BackgroundResponse.fail(str(err))
        except KeyError as err:
            self.logger.error(str(err))
            self.logger.error('Event was skipped due to user settings')
            return BackgroundResponse.done()

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
