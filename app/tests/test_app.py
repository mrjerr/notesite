import re
import pytest

import main


@pytest.fixture
def client():
    app = main.create_app()
    app.debug = True
    app.config['WTF_CSRF_ENABLED'] = False
    return app.test_client()


def test_index_pade(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Add Note" in res.data


def test_note_list_page(client):
    res = client.get("/note-list")
    assert res.status_code == 200
    assert b"Note list" in res.data


def test_post_note(client):
    res = client.post(
            '/',
            data={'text': 'Text for testing'},
            follow_redirects=True)
    assert "успешно добавлена".encode('utf8') in res.data

    note_id = re.findall(r'№\((\d+)\)'.encode('utf8'), res.data)[0]
    res = client.get("/note/{}".format(note_id.decode()))
    assert res.status_code == 200

    unique_word_count = re.findall(rb':\s(\d+)</b>', res.data)[0]
    assert int(unique_word_count) == 3
