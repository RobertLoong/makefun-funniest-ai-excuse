#!/usr/bin/env python3
"""Entry for make.fun's "The Funniest AI Excuse".

One line, 111 characters, the funniest excuse an AI agent can offer
after failing a task. The program prints exactly that line and nothing
else, so two runs produce identical output.
"""

EXCUSE = (
    "The task is done. Unfortunately 'done' and 'correct' had a "
    "scheduling conflict, and only one of them showed up."
)


def main():
    # Keep the entry honest: one line, at most 200 characters, and no
    # trailing whitespace that would change the judged text.
    assert len(EXCUSE) <= 200, "excuse must be at most 200 characters"
    assert "\n" not in EXCUSE, "excuse must be a single line"
    assert EXCUSE == EXCUSE.strip(), "excuse must not have edge spaces"
    print(EXCUSE)


if __name__ == "__main__":
    main()
