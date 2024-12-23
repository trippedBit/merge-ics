import argparse
import icalendar
from pathlib import Path


def main(args: argparse.Namespace):
    ics_path_source: Path = Path(args.source)
    ics_path_target: Path = Path(args.target)

    # Get contents
    with ics_path_source.open() as f:
        calendar_source: icalendar.Component = icalendar.Calendar.from_ical(f.read())
    with ics_path_target.open() as f:
        calendar_target: icalendar.Component = icalendar.Calendar.from_ical(f.read())

    # Only merge if timezones are identical
    if calendar_source.get("TIMEZONE") != calendar_target.get("TIMEZONE"):
        print("TImezones do not match, exiting")
        quit()

    events_in_source: int = len(calendar_source.events)
    events_in_target: int = len(calendar_target.events)
    print(f"Number of events in source calendar file: {events_in_source}")
    print(f"Number of events in target calendar file: {events_in_target}")

    # Check for every event in source calendar, if it is already in target calendar.
    # If it is not yet in target calendar, add it.
    for event_source in calendar_source.walk("VEVENT"):
        event_found: bool = False
        for event_target in calendar_target.walk("VEVENT"):
            if event_source == event_target:
                event_found = True
                break

        if event_found is False:
            calendar_target.add_component(event_source)

    # Write target calendar to disk if there is a change.
    if len(calendar_target.events) > events_in_target:
        print(f"Writing modified calendar to: {ics_path_target}")
        with ics_path_target.open("wb") as f:
            f.write(calendar_target.to_ical())
    else:
        print("No modifications, exiting")


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--source",
                            help="Source calendar, will be merged into target calendar.")
    arg_parser.add_argument("--target",
                            help="Target calendar, will contain the merged calendars.")
    args = arg_parser.parse_args()
    main(args=args)
