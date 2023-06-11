import argparse
from sigtom.database.engine import SignalEngine
from sigtom.database.signal import SignalPoint

args = argparse.ArgumentParser()

args.add_argument("--user", default="test", type=str)

args.add_argument("--password", default="test", type=str)

args.add_argument("--org", default="test")


if __name__ == "__main__":
    arguments = args.parse_args()

    print(arguments.user)
    print(arguments.password)

    engine = SignalEngine(arguments.user, arguments.password, arguments.org)

    ## hardcoded values -- for testing purposes atm.
    engine.setup("172.18.0.4", 8806)

    print(engine.client)

    j = SignalPoint(127, "ettus")

    point = j.convert()

    engine.write(field=point)

