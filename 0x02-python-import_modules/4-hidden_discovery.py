#!/usr/bin/python3
# 4-hidden_discovery.py


if __name__ == "__main__":
    """program that prints all the names defined by hidden_4 module."""
    import hidden_4.pyc

    names = dir(hidden_4.pyc)
    for name in names:
        if name[:2] != "__":
            print(name)
