# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Cloudblue Connect
# All rights reserved.
#
from connect_telegram_ext.events import TelegramNotifyExtension


def test_handle_installation_status_change(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TelegramNotifyExtension(client, logger, config)
    result = ext.handle_installation_status_change(request)
    assert result.status == 'success'


def test_handle_tier_config_adjustment_request_processing(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TelegramNotifyExtension(client, logger, config)
    result = ext.handle_tier_config_adjustment_request_processing(request)
    assert result.status == 'success'


def test_handle_tier_config_change_request_processing(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TelegramNotifyExtension(client, logger, config)
    result = ext.handle_tier_config_change_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_cancel_request_processing(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TelegramNotifyExtension(client, logger, config)
    result = ext.handle_asset_cancel_request_processing(request)
    assert result.status == 'success'


def test_handle_tier_config_setup_request_processing(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TelegramNotifyExtension(client, logger, config)
    result = ext.handle_tier_config_setup_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_resume_request_processing(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TelegramNotifyExtension(client, logger, config)
    result = ext.handle_asset_resume_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_adjustment_request_processing(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TelegramNotifyExtension(client, logger, config)
    result = ext.handle_asset_adjustment_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_suspend_request_processing(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TelegramNotifyExtension(client, logger, config)
    result = ext.handle_asset_suspend_request_processing(request)
    assert result.status == 'success'


def test_handle_tier_account_update_request_processing(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TelegramNotifyExtension(client, logger, config)
    result = ext.handle_tier_account_update_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_change_request_processing(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TelegramNotifyExtension(client, logger, config)
    result = ext.handle_asset_change_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_purchase_request_processing(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TelegramNotifyExtension(client, logger, config)
    result = ext.handle_asset_purchase_request_processing(request)
    assert result.status == 'success'


def test_handle_part_usage_file_request_processing(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TelegramNotifyExtension(client, logger, config)
    result = ext.handle_part_usage_file_request_processing(request)
    assert result.status == 'success'


def test_handle_usage_file_request_processing(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = TelegramNotifyExtension(client, logger, config)
    result = ext.handle_usage_file_request_processing(request)
    assert result.status == 'success'
