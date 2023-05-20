##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2023 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


import typing as t
from dataclasses import dataclass

from atproto.xrpc_client.models import base


@dataclass
class Data(base.DataModelBase):

    """Input data model for :obj:`com.atproto.repo.rebaseRepo`.

    Attributes:
        repo: The handle or DID of the repo.
        swapCommit: Compare and swap with the previous commit by cid.
    """

    repo: str
    swapCommit: t.Optional[str] = None