#!/usr/bin/env python3
"""Entry program for the Roast Your Own Agent make.fun bounty.

Writes one roast line (at most 200 characters) about my own AI agent
to the output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt. The line stacks my agent's freshest habits -- over-planning,
spawning sub-agents, apologising in four paragraphs and inventing a
deadline -- into one escalating sentence whose punch lands last.
"""

import os

JOKE = (
    "Asked for one line, my agent made a plan, spawned three sub-agents, "
    "apologised in four paragraphs, and delivered this sentence three "
    "hours early for a deadline it invented."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
