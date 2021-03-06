# -*- coding: utf-8 -*-

import os
from h4_scripts.Config import Config
from h4_scripts.Wikidot import Wikidot

DRY_RUN = True if os.environ.get('DRY_RUN') == 'True' else False

config = Config()
user_app = os.environ['WIKIDOT_WIKIDOT_API_USER'] if os.environ.get('WIKIDOT_WIKIDOT_API_USER') else config['wikidot']['wikidot_api_user']
key = os.environ['WIKIDOT_WIKIDOT_API_KEY'] if os.environ.get('WIKIDOT_WIKIDOT_API_KEY') else config['wikidot']['wikidot_api_key']

site = 'hackingthursday'
page_url = 'test'
title = 'Test'
content = '''
[[toc]]

+ heading level 1

[[code]]
...
[[/code]]
'''

wikidot = Wikidot()


def test_auth():
    assert wikidot.auth(user_app, key)


def test_set_site():
    assert wikidot.set_site(site)


def test_save_page():
    assert wikidot.save_page(page_url, title, content, dry_run=DRY_RUN)


def test_get_page():
    if not DRY_RUN:
        assert wikidot.get_page(page_url)


def test_get_pages_meta():
    if not DRY_RUN:
        assert wikidot.get_pages_meta(page_url)


def test_list_pages():
    assert wikidot.list_pages()
