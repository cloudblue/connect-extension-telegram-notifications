# -*- coding: utf-8 -*-
#
# This is a message file for telegram extension
# How to use this file?
#
# BASIC USAGE:
# Simply rewrite desired constant with the message you want
# The list of available variables depends on each type of object
# but "id", "object_status" and "object_link" are guaranteed to present
# Empty message means that the default one "Obtained request with id {id}" will be used
#
# ADVANCED USAGE:
# TIP ONE: You can define variable named <event_name>_<event_status>
# (ex: HELPDESK_CASE_PROCESSING_pending)
# to create exact message for given status
#
# TIP TWO: You can use markdown!
#
# Copyright (c) 2022, Cloudblue Connect
# All rights reserved.
#
from datetime import datetime

from connect.client.fluent import ConnectClient

from connect_telegram_ext.models import Event


class Messages:
    DEFAULT_MESSAGE = (
        'Attention: Request №<a href="{object_link}">{id}</a> has been updated and is in '
        'status {object_status}. Please check if requires your attention.'
    )

    ASSET_ADJUSTMENT_REQUEST_PROCESSING = None
    ASSET_CANCEL_REQUEST_PROCESSING = None
    ASSET_CHANGE_REQUEST_PROCESSING = None
    ASSET_PURCHASE_REQUEST_PROCESSING = (
        'Purchase request №<a href="{object_link}">{id}</a> has been updated and is in '
        'status {object_status}. Please check if requires your attention.'
    )
    ASSET_RESUME_REQUEST_PROCESSING = None
    ASSET_SUSPEND_REQUEST_PROCESSING = None

    TIER_ACCOUNT_UPDATE_REQUEST_PROCESSING = None
    TIER_CONFIG_ADJUSTMENT_REQUEST_PROCESSING = None
    TIER_CONFIG_CHANGE_REQUEST_PROCESSING = None
    TIER_CONFIG_SETUP_REQUEST_PROCESSING = None

    INSTALLATION_STATUS_CHANGE_PROCESSING = None

    PART_USAGE_FILE_REQUEST_PROCESSING = None
    USAGE_FILE_REQUEST_PROCESSING = None
    USAGE_FILE_CREATION_PROCESSING = None
    USAGE_FILE_UPLOAD_PROCESSING = None

    HELPDESK_CASE_PROCESSING = (
        'Case [<a href="{object_link}">{id}</a>] \n'
        '\n'
        '<b>From:</b> {issuer[account][name]} \n'
        '<b>To:</b> {receiver[account][name]} \n'
        '\n'
        '<b>Subject:</b> {subject} \n'
        '\n'
        'Changed status to <b>{object_status}</b>.'
    )
    HELPDESK_CASE_PROCESSING_resolved = (
        'Case resolved [<a href="{object_link}">{id}</a>] \n'
        '\n'
        '<b>From:</b> {issuer[account][name]} \n'
        '<b>To:</b> {receiver[account][name]} \n'
        '\n'
        '<b>Subject:</b> {subject} \n'
        '\n'
        'Id: {id} \n'
        'Type: {type} \n'
        'Priority: {priority}'
    )
    HELPDESK_CASE_PROCESSING_inquiring = (
        'Case [<a href="{object_link}">{id}</a>] has been inquired\n'
        '\n'
        '<b>From:</b> {issuer[account][name]} \n'
        '<b>To:</b> {receiver[account][name]} \n'
        '\n'
        '<b>Subject:</b> {subject} \n'
        '\n'
        '<b>Description:</b> {description} \n'
        '\n'
        '{last_message_string}'
        'Id: {id} \n'
        'Type: {type} \n'
        'Priority: {priority}'
    )
    HELPDESK_CASE_PROCESSING_pending = (
        'Case updated [<a href="{object_link}">{id}</a>] \n'
        '\n'
        '<b>From:</b> {issuer[account][name]} \n'
        '<b>To:</b> {receiver[account][name]} \n'
        '\n'
        '<b>Subject:</b> {subject} \n'
        '\n'
        '<b>Description:</b> {description} \n'
        '\n'
        '{last_message_string}'
        'Id: {id} \n'
        'Type: {type} \n'
        'Priority: {priority}'
    )


def get_object_link(client: ConnectClient, path, object_id) -> str:
    try:
        brand_id = client.accounts.all().first()['brand']
    except KeyError:
        brand_id = None
    if not brand_id:
        brand_id = 'BR-000'
    brand = client.branding('brand').get(params={'id': brand_id})
    domain = brand['portals'][list(brand['portals'])[0]]['domain']
    domain = f"https://{domain}/"
    return f"{domain}{path}/{object_id}"


def default_message_callback(event: Event, client: ConnectClient, request: dict) -> str:
    message_template = getattr(
        Messages,
        f"{event.name.upper()}_{request[event.status_filed]}",
        getattr(
            Messages,
            f"{event.name.upper()}",
            Messages.DEFAULT_MESSAGE,
        )
    )

    return message_template.format(
        object_link=get_object_link(client, event.path, request['id']),
        object_status=request[event.status_filed],
        **request,
    )


def helpdesk_message(event: Event, client: ConnectClient, request: dict) -> str:
    last_message_string = ""
    conversation = client.conversations.filter(f"eq(instance_id,{request['id']})").first()
    last_message = client.conversations[conversation['id']].messages.all().order_by(
        '-created',
    ).first()
    if last_message:
        last_message['created'] = datetime.fromisoformat(last_message['created']).strftime(
            "%d-%m-%Y, %H:%m:%S",
        )
        last_message_string = (
            '<b>Last comment</b> from {creator[name]} at {created}: \n'
            '{text} \n\n'
        ).format(**last_message)
    request['last_message_string'] = last_message_string
    return default_message_callback(event, client, request)
