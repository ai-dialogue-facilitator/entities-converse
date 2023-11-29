# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from typing import List
from dataclasses import dataclass, field, asdict


@dataclass
class Participant:
    name:           str = field(default="")
    role:           str = field(default="")
    instructions:   str = field(default="")

    def to_dict(self):
        return asdict(self)


@dataclass
class Utterance:
    utterance:    str = field(default="This is a content of a message.")
    author:       str = field(default="")

    def to_dict(self):
        return asdict(self)


@dataclass
class Conversation:
    """Represents a conversation."""
    participants: List = field(default_factory=list)
    record: List = field(default_factory=list)

    def add_utterance(self, utterance: Utterance):
        self.record.append(utterance)

    def next_statement(self):
        return self.record.pop(0)