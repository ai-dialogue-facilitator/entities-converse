# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from typing import List, Dict
from dataclasses import dataclass, field, asdict
import json
import jsonlines


@dataclass
class Participant:
    name:           str = field(default="")
    role:           str = field(default="")
    instructions:   str = field(default="")
    id:             str = field(default="")
    thread_id:      str = field(default="")

    def to_dict(self):
        return asdict(self)


@dataclass
class Utterance:
    utterance:    str = field(default="This is a content of a message.")
    author:       str = field(default="")

    def to_dict(self):
        return asdict(self)


class Conversation():
    """Represents a conversation."""
    participants:   List = field(default_factory=list)
    record:         List = field(default_factory=list)
    threads:        List = field(default_factory=list)
    agenda: dict = field(default_factory=dict)

    def __init__(self, **kwargs):
        self._load_agenda()
        self._load_record()
        for key, value in kwargs.items():
            setattr(self, key, value)
        super(Conversation, self).__init__()

    def add_utterance(self, utterance: Utterance):
        self.record.append(utterance)

    def _save_utterance(self, utterance: Utterance):
        dict = utterance.to_dict()
        with jsonlines.open('../record.jsonl', 'w') as writer:
            writer.write(utterance.to_dict())

    def _load_participants(self):
        with open('../participants/list.json', 'r') as file:
            self.participants = json.load(file)

    def _load_record(self):
        with jsonlines.open('../record.jsonl', 'r') as reader:
            self.record = [Utterance(**line) for line in reader.iter()]

    def _load_agenda(self):
        with open('../agenda.json', 'r') as file:
            self.agenda = json.load(file)

    def next_statement(self):
        return self.record.pop(0)


if __name__ == '__main__':
    conv = Conversation()
    conv._load_agenda()
    conv._load_record()
    print('ok')