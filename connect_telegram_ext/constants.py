from dataclasses import dataclass

import connect_telegram_ext.titles as event_titles


@dataclass
class Event:
    name: str
    statuses: list
    title: str
    path: str
    enabled: bool = False
    status_filed: str = 'status'


class Events:
    INSTALLATION_STATUS_CHANGE = Event(
        'installation_status_change',
        ['installed', 'uninstalled'],
        event_titles.INSTALLATION_STATUS_CHANGE_PROCESSING,
        'devops/installations',
    )
    TIER_CONFIG_ADJUSTMENT_REQUEST_PROCESSING = Event(
        'tier_config_adjustment_request_processing',
        ['pending', 'approved', 'failed', 'inquiring'],
        event_titles.TIER_CONFIG_ADJUSTMENT_REQUEST_PROCESSING,
        'tier/config-requests',
    )
    TIER_CONFIG_CHANGE_REQUEST_PROCESSING = Event(
        'tier_config_change_request_processing',
        ['pending', 'approved', 'failed', 'inquiring'],
        event_titles.TIER_CONFIG_CHANGE_REQUEST_PROCESSING,
        'tier/config-requests',
    )
    ASSET_CANCEL_REQUEST_PROCESSING = Event(
        'asset_cancel_request_processing',
        ['pending', 'approved', 'failed', 'inquiring', 'scheduled', 'revoking', 'revoked'],
        event_titles.ASSET_CANCEL_REQUEST_PROCESSING,
        'requests',
    )
    TIER_CONFIG_SETUP_REQUEST_PROCESSING = Event(
        'tier_config_setup_request_processing',
        ['pending', 'approved', 'failed', 'inquiring'],
        event_titles.TIER_CONFIG_SETUP_REQUEST_PROCESSING,
        'tier/config-requests',
    )
    ASSET_RESUME_REQUEST_PROCESSING = Event(
        'asset_resume_request_processing',
        ['pending', 'approved', 'failed', 'inquiring', 'scheduled', 'revoking', 'revoked'],
        event_titles.ASSET_RESUME_REQUEST_PROCESSING,
        'requests',
    )
    ASSET_ADJUSTMENT_REQUEST_PROCESSING = Event(
        'asset_adjustment_request_processing',
        ['pending', 'approved', 'failed', 'inquiring', 'scheduled', 'revoking', 'revoked'],
        event_titles.ASSET_ADJUSTMENT_REQUEST_PROCESSING,
        'requests',
    )
    ASSET_SUSPEND_REQUEST_PROCESSING = Event(
        'asset_suspend_request_processing',
        ['pending', 'approved', 'failed', 'inquiring', 'scheduled', 'revoking', 'revoked'],
        event_titles.ASSET_SUSPEND_REQUEST_PROCESSING,
        'requests',
    )
    TIER_ACCOUNT_UPDATE_REQUEST_PROCESSING = Event(
        'tier_account_update_request_processing',
        ['pending', 'accepted', 'ignored'],
        event_titles.TIER_ACCOUNT_UPDATE_REQUEST_PROCESSING,
        'tier/account-requests',
    )
    ASSET_CHANGE_REQUEST_PROCESSING = Event(
        'asset_change_request_processing',
        ['pending', 'approved', 'failed', 'inquiring', 'scheduled', 'revoking', 'revoked'],
        event_titles.ASSET_CHANGE_REQUEST_PROCESSING,
        'requests',
    )
    ASSET_PURCHASE_REQUEST_PROCESSING = Event(
        'asset_purchase_request_processing',
        ['pending', 'approved', 'failed', 'inquiring', 'scheduled', 'revoking', 'revoked'],
        event_titles.ASSET_PURCHASE_REQUEST_PROCESSING,
        'requests/',
    )
    PART_USAGE_FILE_REQUEST_PROCESSING = Event(
        'part_usage_file_request_processing',
        ['draft', 'ready', 'closed', 'failed'],
        event_titles.PART_USAGE_FILE_REQUEST_PROCESSING,
        'usage/chunks',
    )
    USAGE_FILE_REQUEST_PROCESSING = Event(
        'usage_file_request_processing',
        ["draft", "uploading", "uploaded", "invalid", "processing",
         "processed", "ready", "rejected", "pending", "accepted", "closed"],
        event_titles.USAGE_FILE_REQUEST_PROCESSING,
        'usage/files',
    )
    HELPDESK_CASE_PROCESSING = Event(
        'helpdesk_case_processing',
        ["pending", "inquiring", "resolved", "closed"],
        event_titles.HELPDESK_CASE_PROCESSING,
        'helpdesk/cases',
        status_filed='state',
    )


class Errors:
    TOKEN_NOT_SET = 'Telegram token not set'
    CHAT_ID_NOT_SET = 'Telegram chat ID not set'


EVENT_LIST = [
    Events.INSTALLATION_STATUS_CHANGE, Events.TIER_CONFIG_ADJUSTMENT_REQUEST_PROCESSING,
    Events.TIER_CONFIG_CHANGE_REQUEST_PROCESSING, Events.ASSET_CANCEL_REQUEST_PROCESSING,
    Events.TIER_CONFIG_SETUP_REQUEST_PROCESSING, Events.ASSET_RESUME_REQUEST_PROCESSING,
    Events.ASSET_ADJUSTMENT_REQUEST_PROCESSING, Events.ASSET_SUSPEND_REQUEST_PROCESSING,
    Events.TIER_ACCOUNT_UPDATE_REQUEST_PROCESSING, Events.ASSET_CHANGE_REQUEST_PROCESSING,
    Events.ASSET_PURCHASE_REQUEST_PROCESSING, Events.PART_USAGE_FILE_REQUEST_PROCESSING,
    Events.USAGE_FILE_REQUEST_PROCESSING, Events.HELPDESK_CASE_PROCESSING,
]
