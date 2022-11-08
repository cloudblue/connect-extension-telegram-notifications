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
DEFAULT_MESSAGE = (
    'Attention: Request №<a href={object_link}>{id}</a> has been updated and is in '
    'status {object_status}. Please check if requires your attention.'
)

ASSET_ADJUSTMENT_REQUEST_PROCESSING = None
ASSET_CANCEL_REQUEST_PROCESSING = None
ASSET_CHANGE_REQUEST_PROCESSING = None
ASSET_PURCHASE_REQUEST_PROCESSING = (
    'Purchase request №<a href={object_link}>{id}</a> has been updated and is in '
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
    '<b>WARNING!</b> \nHelpdesk case №<a href={object_link}>{id}</a> '
    'changed status to {object_status}.'
)
HELPDESK_CASE_PROCESSING_resolved = (
    'Helpdesk case <a href={object_link}>{id}</a> has been resolved.'
)
