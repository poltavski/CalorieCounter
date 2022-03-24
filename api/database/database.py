# type: ignore
"""Module for peewee's database object.

Based on:
https://fastapi.tiangolo.com/advanced/sql-databases-peewee/#make-peewee-async-compatible-peeweeconnectionstate
"""
from contextvars import ContextVar

import peewee
from fastapi import Depends
from playhouse.postgres_ext import PostgresqlExtDatabase

from .settings import DATABASE


db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    """Needed to allow Peewee to work with FastAPI's async coroutine functionality.

    (DB connection per coroutine context rather than per thread).
    """

    def __init__(self, **kwargs):
        """Peeweeconnstate object constructor."""
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        """Set att."""
        self._state.get()[name] = value

    def __getattr__(self, name):
        """Get att."""
        return self._state.get()[name]


async def _reset_db_state():
    """Reset the database state to the default context variable.

    Set the value for the context variable (with just a default dict) that will be
    used as the database state for the whole request. And then the dependency get_db()
    will store in it the database state (connection, transactions, etc).

    Must be async (refer to the FastAPI docs).
    """
    db._state._state.set(db_state_default.copy())
    db._state.reset()


def get_db(db_state=Depends(_reset_db_state)):
    """Open and close database connection per request.

    Creates a dependency that will connect the database at the beginning of a request
    and disconnect it at the end.
    Stores the database state in the underlying context variable.
    """
    try:
        db.connect()
        yield
    finally:
        if not db.is_closed():
            db.close()


db = PostgresqlExtDatabase(
    DATABASE["db_name"],
    user=DATABASE["user"],
    password=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
    autorollback=DATABASE["autorollback"],
)

db._state = PeeweeConnectionState()
