from connect_telegram_ext.messages import get_object_link, helpdesk_message
from connect_telegram_ext.constants import Events


def test_get_object_link(client_mocker_factory, connect_client):
    client_mocker = client_mocker_factory()
    client_mocker.branding('brand').get(
        return_value={
            'portals': {
                'portal.cnct.info': {
                    'domain': 'portal.cnct.info.mocked',
                },
            },
        },
    )
    client_mocker.accounts.all().first().mock(
        return_value=[{
            'brand': 'BR-000',
        }],
    )
    assert get_object_link(
        connect_client,
        'test/path',
        1,
    ) == 'https://portal.cnct.info.mocked/test/path/1'


def test_helpdesk_message_with_creator(client_mocker_factory, connect_client):
    client_mocker = client_mocker_factory()
    helpdesk_event = Events.HELPDESK_CASE_PROCESSING
    test_conversation = {
        'id': 'CONV-001',
    }
    test_message = {
        'id': 'MSG-001',
        'created': '2023-01-18',
        'text': 'test text',
        'creator': {
            'name': 'Test creator',
        },
    }
    test_request = {
        'id': 'REQ-001',
        'state': 'pending',
        'issuer': {
            'account': {
                'name': 'Test Issuer',
            },
        },
        'receiver': {
            'account': {
                'name': 'Test Receiver',
            },
        },
        'subject': 'Test subject',
        'description': 'Test description',
        'type': 'Test type',
        'priority': 'Test priority',
    }
    client_mocker.conversations.filter().first().mock(
        return_value=[test_conversation],
    )
    client_mocker.conversations[test_conversation['id']].messages.all().order_by().first().mock(
        return_value=[test_message],
    )
    expected_message = """
Case updated [<a href="https://portal.cnct.info.mocked/helpdesk/cases/REQ-001">REQ-001</a>]
<b>From:</b> Test Issuer
<b>To:</b> Test Receiver
<b>Subject:</b> Test subject
<b>Description:</b> Test description

<b>Last comment</b> from Test creator at 18-01-2023, 00:01:00:
test text

Id: REQ-001
Type: Test type
Priority: Test priority"""
    assert helpdesk_message(
        helpdesk_event,
        connect_client,
        test_request,
    ).replace("\n", "").replace(" ", "") == expected_message.replace("\n", "").replace(" ", "")


def test_helpdesk_message_without_creator(client_mocker_factory, connect_client):
    client_mocker = client_mocker_factory()
    helpdesk_event = Events.HELPDESK_CASE_PROCESSING
    test_conversation = {
        'id': 'CONV-001',
    }
    test_message = {
        'id': 'MSG-001',
        'created': '2023-01-18',
        'text': 'test text',
    }
    test_request = {
        'id': 'REQ-001',
        'state': 'pending',
        'issuer': {
            'account': {
                'name': 'Test Issuer',
            },
        },
        'receiver': {
            'account': {
                'name': 'Test Receiver',
            },
        },
        'subject': 'Test subject',
        'description': 'Test description',
        'type': 'Test type',
        'priority': 'Test priority',
    }
    client_mocker.conversations.filter().first().mock(
        return_value=[test_conversation],
    )
    client_mocker.conversations[test_conversation['id']].messages.all().order_by().first().mock(
        return_value=[test_message],
    )
    expected_message = """
Case updated [<a href="https://portal.cnct.info.mocked/helpdesk/cases/REQ-001">REQ-001</a>]
<b>From:</b> Test Issuer
<b>To:</b> Test Receiver
<b>Subject:</b> Test subject
<b>Description:</b> Test description

<b>Last comment</b> at 18-01-2023, 00:01:00:
test text

Id: REQ-001
Type: Test type
Priority: Test priority"""
    assert helpdesk_message(
        helpdesk_event,
        connect_client,
        test_request,
    ).replace("\n", "").replace(" ", "") == expected_message.replace("\n", "").replace(" ", "")
