from collections import OrderedDict
from copy import deepcopy

import telegram.error

from connect_telegram_ext.models import SettingsPayload, TestMessagePayload
from connect_telegram_ext.webapp import _format_notification_settings, TelegramNotifyWebApplication


def _get_default_settings():
    return deepcopy(OrderedDict([(
        'asset_adjustment_request_processing',
        {
            'title': 'Asset adjustment request processing',
            'statuses': {
                'pending': False, 'approved': False, 'failed': False,
                'inquiring': False, 'scheduled': False, 'revoking': False,
                'revoked': False,
            },
        },
    ), (
        'asset_cancel_request_processing',
        {
            'title': 'Asset cancel request processing',
            'statuses': {
                'pending': False, 'approved': False, 'failed': False,
                'inquiring': False, 'scheduled': False, 'revoking': False,
                'revoked': False,
            },
        },
    ), (
        'asset_change_request_processing',
        {
            'title': 'Asset change request processing',
            'statuses': {
                'pending': False, 'approved': False,
                'failed': False, 'inquiring': False,
                'scheduled': False, 'revoking': False,
                'revoked': False,
            },
        },
    ), (
        'asset_purchase_request_processing',
        {
            'title': 'Asset purchase request processing',
            'statuses': {
                'pending': False, 'approved': False,
                'failed': False, 'inquiring': False,
                'scheduled': False, 'revoking': False,
                'revoked': False,
            },
        },
    ), (
        'asset_resume_request_processing',
        {
            'title': 'Asset resume request processing',
            'statuses': {
                'pending': False, 'approved': False,
                'failed': False, 'inquiring': False,
                'scheduled': False, 'revoking': False,
                'revoked': False,
            },
        },
    ), (
        'asset_suspend_request_processing',
        {
            'title': 'Asset suspend request processing',
            'statuses': {
                'pending': False, 'approved': False,
                'failed': False, 'inquiring': False,
                'scheduled': False, 'revoking': False,
                'revoked': False,
            },
        },
    ), (
        'helpdesk_case_processing',
        {
            'title': 'Helpdesk case processing',
            'statuses': {
                'pending': False, 'inquiring': False,
                'resolved': False, 'closed': False,
            },
        },
    ), (
        'installation_status_change',
        {
            'title': 'Installation status change',
            'statuses': {
                'installed': False, 'uninstalled': False,
            },
        },
    ), (
        'part_usage_file_request_processing',
        {
            'title': 'Part usage file request processing',
            'statuses': {
                'draft': False, 'ready': False,
                'closed': False, 'failed': False,
            },
        },
    ), (
        'tier_account_update_request_processing',
        {
            'title': 'Tier account update request processing',
            'statuses': {
                'pending': False, 'accepted': False, 'ignored': False,
            },
        },
    ), (
        'tier_config_adjustment_request_processing',
        {
            'title': 'Tier config adjustment request processing',
            'statuses': {
                'pending': False, 'approved': False,
                'failed': False, 'inquiring': False,
            },
        },
    ), (
        'tier_config_change_request_processing',
        {
            'title': 'Tier config change request processing',
            'statuses': {
                'pending': False,
                'approved': False,
                'failed': False,
                'inquiring': False,
            },
        },
    ), (
        'tier_config_setup_request_processing',
        {
            'title': 'Tier config setup request processing',
            'statuses': {
                'pending': False,
                'approved': False, 'failed': False,
                'inquiring': False,
            },
        },
    ), (
        'usage_file_request_processing',
        {
            'title': 'Usage file request processing',
            'statuses': {
                'draft': False, 'uploading': False,
                'uploaded': False, 'invalid': False,
                'processing': False,
                'processed': False,
                'ready': False, 'rejected': False,
                'pending': False, 'accepted': False,
                'closed': False,
            },
        },
    )]))


def _get_test_settings():
    return deepcopy({
        "asset_adjustment_request_processing": {
            "title": "Asset adjustment request processing",
            "statuses": {
                "pending": True,
            },
        },
        "asset_cancel_request_processing": {
            "title": "Asset cancel request processing",
            "statuses": {
                "failed": True,
            },
        },
        "asset_change_request_processing": {
            "title": "Asset change request processing",
            "statuses": {
                "revoking": False,
            },
        },
        "asset_purchase_request_processing": {
            "title": "Asset purchase request processing",
            "statuses": {
                "failed": True,
                "inquiring": True,
            },
        },
    })


def test__format_notification_settings():
    default_dict = _get_default_settings()
    default_dict['asset_adjustment_request_processing']['statuses']['pending'] = True
    default_dict['asset_cancel_request_processing']['statuses']['failed'] = True
    default_dict['asset_purchase_request_processing']['statuses']['failed'] = True
    default_dict['asset_purchase_request_processing']['statuses']['inquiring'] = True

    assert _format_notification_settings({'notifications': _get_test_settings()}) == default_dict


def test_retrieve_empty_settings(test_client_factory):
    installation = {
        'id': 'EIN-000',
        'settings': {},
    }
    client = test_client_factory(TelegramNotifyWebApplication)
    response = client.get('/api/settings', installation=installation)
    assert response.status_code == 200

    data = response.json()
    assert data['token'] is None
    assert data['notifications'] == _get_default_settings()


def test_retrieve_settings_500(test_client_factory, mocker):
    installation = {
        'id': 'EIN-000',
        'settings': {},
    }
    client = test_client_factory(TelegramNotifyWebApplication)
    mocker.patch(
        'connect_telegram_ext.webapp._format_notification_settings',
        side_effect=Exception('mocker error'),
    )
    response = client.get('/api/settings', installation=installation)
    assert response.status_code == 500
    assert response.json()['detail'] == 'Something went wrong on our side: mocker error'


def test_retrieve_settings_no_installation(test_client_factory):
    client = test_client_factory(TelegramNotifyWebApplication)
    response = client.get('/api/settings')
    assert response.status_code == 404


def test_retrieve_settings(test_client_factory):
    installation = {
        'id': 'EIN-000',
        'settings': {
            'token': 'test-token',
            'notifications': {
                'asset_purchase_request_processing': {
                    'statuses': {
                        'inquiring': True,
                    },
                },
            },
        },
    }
    client = test_client_factory(TelegramNotifyWebApplication)
    response = client.get('/api/settings', installation=installation)
    assert response.status_code == 200

    data = response.json()
    assert data['token'] == 'test-token'
    default_settings = _get_default_settings()
    default_settings['asset_purchase_request_processing']['statuses']['inquiring'] = True
    assert data['notifications'] == default_settings


def test_update_settings(test_client_factory, client_mocker_factory):
    installation = {
        'id': 'EIN-000',
        'settings': {},
    }
    test_settings = _get_test_settings()
    test_settings['asset_purchase_request_processing']['statuses']['failed'] = True
    test_settings['asset_adjustment_request_processing']['statuses']['pending'] = True
    payload = SettingsPayload(
        token='test_token',
        chatId=-5,
        notifications=test_settings,
    )

    client_mocker = client_mocker_factory()
    client_mocker('devops').installations['EIN-000'].update(
        return_value={
            'id': 'EIN-000',
            'settings': {
                'token': 'test_token',
                'chatId': -5,
                'notifications': test_settings,
            },
        },
    )
    client = test_client_factory(TelegramNotifyWebApplication)

    result = client.post('/api/settings', json=payload.dict(), installation=installation)

    assert result.status_code == 200
    assert result.json()['token'] == payload.dict()['token']
    assert result.json()['chatId'] == payload.dict()['chatId']
    received_statuses = result.json()['notifications']['asset_purchase_request_processing']
    sent_statuses = payload.dict()['notifications']['asset_purchase_request_processing']
    assert received_statuses['statuses']['failed'] == sent_statuses['statuses']['failed']
    assert received_statuses['statuses']['scheduled'] is False


def test_update_settings_failed(test_client_factory, mocker):
    installation = {
        'id': 'EIN-000',
        'settings': {},
    }
    payload = SettingsPayload(
        token='test_token',
        chatId=-5,
        notifications=_get_test_settings(),
    )
    mocker.patch(
        'connect_telegram_ext.webapp._format_notification_settings',
        side_effect=Exception('mocker error'),
    )
    client = test_client_factory(TelegramNotifyWebApplication)

    result = client.post('/api/settings', json=payload.dict(), installation=installation)

    assert result.status_code == 500
    assert result.json()['detail'] == 'Something went wrong on our side: Unexpected error'


def test_test_message_no_token(test_client_factory):
    installation = {
        'id': 'EIN-000',
        'settings': {},
    }
    client = test_client_factory(TelegramNotifyWebApplication)
    payload = TestMessagePayload(
        message='test',
    )
    response = client.post('/api/test-message', json=payload.dict(), installation=installation)
    assert response.status_code == 400
    assert response.json()['detail'] == 'Telegram token not set'


def test_test_message_no_chat_id(test_client_factory):
    installation = {
        'id': 'EIN-000',
        'settings': {'token': 'test_token'},
    }
    client = test_client_factory(TelegramNotifyWebApplication)
    payload = TestMessagePayload(
        message='test',
    )
    response = client.post('/api/test-message', json=payload.dict(), installation=installation)
    assert response.status_code == 400
    assert response.json()['detail'] == 'Telegram chat ID not set'


def test_test_message_invalid_token(test_client_factory, mocker):
    installation = {
        'id': 'EIN-000',
        'settings': {'token': 'test_token', 'chatId': -5},
    }
    client = test_client_factory(TelegramNotifyWebApplication)
    payload = TestMessagePayload(
        message='test',
    )
    mocker.patch(
        'telegram.bot.Bot.send_message',
        side_effect=Exception('you gone too far with your test'),
    )
    response = client.post('/api/test-message', json=payload.dict(), installation=installation)
    assert response.status_code == 400
    assert response.json()['detail'] == 'Invalid token'


def test_test_message_invalid_chat_id(test_client_factory, mocker):
    installation = {
        'id': 'EIN-000',
        'settings': {'token': '5584437396:AAFnY_NQZreuvE3eDOAu_BQzrSTfMLyMXmU', 'chatId': -5},
    }
    client = test_client_factory(TelegramNotifyWebApplication)
    payload = TestMessagePayload(
        message='test',
    )
    mocker.patch(
        'telegram.bot.Bot._post',
        side_effect=telegram.error.TelegramError('Chat not found test'),
    )
    response = client.post('/api/test-message', json=payload.dict(), installation=installation)
    assert response.status_code == 400
    assert response.json()['detail'] == 'Chat not found test'


def test_test_message_ok(test_client_factory, mocker):
    installation = {
        'id': 'EIN-000',
        'settings': {'token': '5584437396:AAFnY_NQZreuvE3eDOAu_BQzrSTfMLyMXmU', 'chatId': -5},
    }
    client = test_client_factory(TelegramNotifyWebApplication)
    payload = TestMessagePayload(
        message='test',
    )
    mocker.patch('connect_telegram_ext.telegram.TelegramClient.send_message', return_value={})
    response = client.post('/api/test-message', json=payload.dict(), installation=installation)
    assert response.status_code == 204
    assert response.json() is None
