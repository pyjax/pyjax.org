import pathlib

import feedparser
import icalendar
import requests
import typer
from pelican.settings import DEFAULT_CONFIG
from pelican.utils import slugify
from typing_extensions import Annotated

cli = typer.Typer(name="meetup-events")

event_template = """Title: {title}
Date: {date}
Slug: {slug}

_RSVP: [{url}]({url})_

{content}
"""


@cli.command()
def main(
        group: Annotated[str, typer.Option()],
        output: Annotated[pathlib.Path, typer.Option()] = "content/events",
):
    typer.echo("Pulling events from Meetup")
    ics = requests.get(f"https://www.meetup.com/{group}/events/ical/")
    calendar = icalendar.Calendar.from_ical(ics.text)

    event_items = {}
    for event in calendar.walk():
        if event.name == "VEVENT":
            event_id = str(event.uid).split("@")[0].split("_")[-1]
            event_items[event_id] = {
                "event_id": event_id,
                "event_uid": event.uid,
                "title": event.get("summary"),
                "content": event.get("description"),
                "start_time": event.start,
                "end_time": event.end,
                "modified": event.get("last_modified"),
                "url": event.get("url"),
            }

    parsed_feed = feedparser.parse(f"https://www.meetup.com/{group}/events/rss/")
    for entry in parsed_feed.entries:
        entry_id = entry.id.split("/")[-2]
        event_items[entry_id].update({
            "content": entry.get("summary").replace("\n", "\n\n").replace("\n\n\n", "\n\n").replace("\n\n\n", "\n\n"),
        })

    for event_id, event in event_items.items():
        event_path = output / f"{event['event_uid']}.md"
        event_path.write_text(event_template.format(**event, **{
            "date": event["start_time"],
            "slug": slugify(event["title"], regex_subs=DEFAULT_CONFIG['SLUG_REGEX_SUBSTITUTIONS']),
        }))

    typer.echo("Meetup events complete")


if __name__ == "__main__":
    cli()
