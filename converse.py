# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from conversation import Conversation, Participant, Utterance


def main():
    human = Participant(name="human",
                        role="user",
                        instructions="")

    facilitator_instructions = ("This is a facilitator"
                                " instructions.")
    facilitator = Participant(name="facilitator",
                            role="assistant",
                            instructions=facilitator_instructions)

    protagonist = Participant(name="protagonist",
                              role="assistant",
                              instructions="")
    antagonist = Participant(name="antagonist",
                            role="assistant",
                            instructions="")

    participant_list = [human, facilitator, protagonist, antagonist]
    conversation = Conversation(participants=participant_list)
    pass


if __name__ == "__main__":
    main()
    print("ok")