# coding: utf-8

import os
from uuid import uuid1
from datetime import datetime
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.models import Model


class Todo(Model):
    """Represent todo
    """
    class Meta:
        table_name = os.getenv(
            'TODO_TABLE',
            'enigma-scrum-todo-todo-table-dev'
        )
        region = os.getenv('PROVIDER_REGION', 'eu-central-1')

        if os.getenv('IS_OFFLINE') == 'True':
            host = 'http://localhost:8000'

    uuid = UnicodeAttribute(
        null=False,
        default=lambda: str(uuid1())
    )
    owner = UnicodeAttribute(hash_key=True, null=False)
    created_at = NumberAttribute(
        null=False,
        default=lambda: datetime.timestamp(datetime.now()),
        range_key=True
    )

    content = UnicodeAttribute(null=False)
