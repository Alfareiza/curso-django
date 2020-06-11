from django.test import Client

from pypro.django_assertions import assert_contains


def test_status_code(client: Client):
    resp = client.get('/')
    print('resp = ', resp)
    assert resp.status_code == 200


def test_title(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<title>Qwerty App</title>')
