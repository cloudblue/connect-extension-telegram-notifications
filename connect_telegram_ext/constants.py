from dataclasses import dataclass


@dataclass
class Event:
    name: str
    statuses: list
    title: str
    message_template: str = 'Obtained request with id {id}'
    enabled: bool = False


class Events:
    INSTALLATION_STATUS_CHANGE = Event(
        'installation_status_change',
        ['installed', 'uninstalled'],
        'Installation status change',
    )
    TIER_CONFIG_ADJUSTMENT_REQUEST_PROCESSING = Event(
        'tier_config_adjustment_request_processing',
        ['pending', 'approved', 'failed', 'inquiring'],
        'Tier config adjustment request processing',
    )
    TIER_CONFIG_CHANGE_REQUEST_PROCESSING = Event(
        'tier_config_change_request_processing',
        ['pending', 'approved', 'failed', 'inquiring'],
        'Tier config change request processing',
    )
    ASSET_CANCEL_REQUEST_PROCESSING = Event(
        'asset_cancel_request_processing',
        ['pending', 'approved', 'failed', 'inquiring', 'scheduled', 'revoking', 'revoked'],
        'Asset cancel request processing',
    )
    TIER_CONFIG_SETUP_REQUEST_PROCESSING = Event(
        'tier_config_setup_request_processing',
        ['pending', 'approved', 'failed', 'inquiring'],
        'Tier config setup request processing',
    )
    ASSET_RESUME_REQUEST_PROCESSING = Event(
        'asset_resume_request_processing',
        ['pending', 'approved', 'failed', 'inquiring', 'scheduled', 'revoking', 'revoked'],
        'Asset resume request processing',
    )
    ASSET_ADJUSTMENT_REQUEST_PROCESSING = Event(
        'asset_adjustment_request_processing',
        ['pending', 'approved', 'failed', 'inquiring', 'scheduled', 'revoking', 'revoked'],
        'Asset adjustment request processing',
    )
    ASSET_SUSPEND_REQUEST_PROCESSING = Event(
        'asset_suspend_request_processing',
        ['pending', 'approved', 'failed', 'inquiring', 'scheduled', 'revoking', 'revoked'],
        'Asset suspend request processing',
    )
    TIER_ACCOUNT_UPDATE_REQUEST_PROCESSING = Event(
        'tier_account_update_request_processing',
        ['pending', 'accepted', 'ignored'],
        'Tier account update request processing',
    )
    ASSET_CHANGE_REQUEST_PROCESSING = Event(
        'asset_change_request_processing',
        ['pending', 'approved', 'failed', 'inquiring', 'scheduled', 'revoking', 'revoked'],
        'Asset change request processing',
    )
    ASSET_PURCHASE_REQUEST_PROCESSING = Event(
        'asset_purchase_request_processing',
        ['pending', 'approved', 'failed', 'inquiring', 'scheduled', 'revoking', 'revoked'],
        'Asset purchase request processing',
        'Purchase request {id} got update. The current status is {status}. '
        '{portal_url}/subscriptions/fulfillment/{id}',
    )
    PART_USAGE_FILE_REQUEST_PROCESSING = Event(
        'part_usage_file_request_processing',
        ['draft', 'ready', 'closed', 'failed'],
        'Part usage file request processing',
    )
    USAGE_FILE_REQUEST_PROCESSING = Event(
        'usage_file_request_processing',
        ['pending', 'accepted', 'ignored'],
        'Usage file request processing',
    )
    HELPDESK_CASE_PROCESSING = Event(
        'helpdesk_case_processing',
        ["pending", "inquiring", "resolved", "closed"],
        'Helpdesk case processing',
    )


class Errors:
    TOKEN_NOT_SET = 'Telegram token not set'


EVENT_LIST = [
    Events.INSTALLATION_STATUS_CHANGE, Events.TIER_CONFIG_ADJUSTMENT_REQUEST_PROCESSING,
    Events.TIER_CONFIG_CHANGE_REQUEST_PROCESSING, Events.ASSET_CANCEL_REQUEST_PROCESSING,
    Events.TIER_CONFIG_SETUP_REQUEST_PROCESSING, Events.ASSET_RESUME_REQUEST_PROCESSING,
    Events.ASSET_ADJUSTMENT_REQUEST_PROCESSING, Events.ASSET_SUSPEND_REQUEST_PROCESSING,
    Events.TIER_ACCOUNT_UPDATE_REQUEST_PROCESSING, Events.ASSET_CHANGE_REQUEST_PROCESSING,
    Events.ASSET_PURCHASE_REQUEST_PROCESSING, Events.PART_USAGE_FILE_REQUEST_PROCESSING,
    Events.USAGE_FILE_REQUEST_PROCESSING, Events.HELPDESK_CASE_PROCESSING,
]
