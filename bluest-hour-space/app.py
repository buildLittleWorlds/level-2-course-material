from datetime import datetime, timedelta
from html import escape

import gradio as gr
import pytz
import requests

# Godfrey, IL coordinates
LAT = 38.9556
LNG = -90.1868
TZID = "America/Chicago"
WALK_MINUTES = 20

# Local horizon offset (minutes). The bluest moment arrives earlier than the
# astronomical midpoint because terrain, trees, and buildings on the western
# horizon block the sun before it reaches the geometric horizon. This offset
# is calibrated by nightly observation and recorded in the tracking spreadsheet.
# Positive value = shift the predicted bluest moment earlier.
LOCAL_OFFSET_MINUTES = 35

DIDION_QUOTE = (
    '"In certain latitudes there comes a span of time approaching and following '
    'the summer solstice, some weeks in all, when the twilights turn long and blue."'
)
DIDION_ATTR = "Joan Didion, <em>Blue Nights</em>"


def get_twilight_data(date_str):
    """Fetch twilight times from sunrisesunset.io API."""
    url = "https://api.sunrisesunset.io/json"
    params = {
        "lat": LAT,
        "lng": LNG,
        "date": date_str,
        "timezone": TZID,
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    if data.get("status") != "OK":
        raise ValueError(f"API returned status: {data.get('status')}")
    return data["results"]


def parse_local_time(time_str, date_str):
    """Parse a time string like '7:36:00 PM' with a date into a datetime."""
    dt_str = f"{date_str} {time_str}"
    return datetime.strptime(dt_str, "%Y-%m-%d %I:%M:%S %p")


def fmt_time(dt):
    """Format a datetime as a friendly 12-hour time string."""
    return dt.strftime("%-I:%M %p").lower()


def fmt_duration_minutes(total_minutes):
    """Format minutes as 'Xh Ym' or 'Ym'."""
    if total_minutes >= 60:
        return f"{total_minutes // 60}h {total_minutes % 60}m"
    return f"{total_minutes}m"


def fmt_day_length(day_length):
    """Format an API day-length value into a friendlier string."""
    if not day_length:
        return "Unavailable"
    try:
        hours, minutes, seconds = [int(part) for part in day_length.split(":")]
    except ValueError:
        return day_length
    total_minutes = round((hours * 3600 + minutes * 60 + seconds) / 60)
    return fmt_duration_minutes(total_minutes)


def minutes_between(start, end):
    """Return the rounded whole-minute difference between two datetimes."""
    return round((end - start).total_seconds() / 60)


def clamp_pct(value):
    """Clamp a percentage so the timeline remains well-formed."""
    return max(0.0, min(100.0, value))


def position_pct(moment, window_start, window_seconds):
    """Position a timestamp within the displayed timeline window."""
    delta_seconds = (moment - window_start).total_seconds()
    return clamp_pct((delta_seconds / window_seconds) * 100)


def build_walk_context(date_str):
    """Calculate all twilight and walk details for the selected date."""
    datetime.strptime(date_str, "%Y-%m-%d")
    results = get_twilight_data(date_str)

    sunset = parse_local_time(results["sunset"], date_str)
    dusk = parse_local_time(results["dusk"], date_str)
    nautical_end = parse_local_time(results["nautical_twilight_end"], date_str)

    astro_midpoint = dusk + (nautical_end - dusk) / 2
    bluest_moment = astro_midpoint - timedelta(minutes=LOCAL_OFFSET_MINUTES)

    walk_half = timedelta(minutes=WALK_MINUTES / 2)
    walk_start = bluest_moment - walk_half
    walk_end = bluest_moment + walk_half

    display_date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%A, %B %-d, %Y")
    blue_hour_minutes = max(0, minutes_between(dusk, nautical_end))

    # Match the Pages version's visual framing by showing sunset through the end
    # of nautical twilight with a little padding on both sides.
    window_start = sunset - timedelta(minutes=5)
    window_end = nautical_end + timedelta(minutes=5)
    window_seconds = max((window_end - window_start).total_seconds(), 1)

    walk_left = position_pct(walk_start, window_start, window_seconds)
    walk_right = position_pct(walk_end, window_start, window_seconds)
    walk_width = max(walk_right - walk_left, 6.0)

    return {
        "date_str": date_str,
        "display_date": display_date,
        "day_length": fmt_day_length(results.get("day_length", "")),
        "sunset": sunset,
        "dusk": dusk,
        "nautical_end": nautical_end,
        "astro_midpoint": astro_midpoint,
        "bluest_moment": bluest_moment,
        "walk_start": walk_start,
        "walk_end": walk_end,
        "blue_hour_minutes": blue_hour_minutes,
        "walk_left": walk_left,
        "walk_width": min(walk_width, 100.0 - walk_left),
        "sunset_pct": position_pct(sunset, window_start, window_seconds),
        "dusk_pct": position_pct(dusk, window_start, window_seconds),
        "bluest_pct": position_pct(bluest_moment, window_start, window_seconds),
        "nautical_pct": position_pct(nautical_end, window_start, window_seconds),
    }


def render_error(message):
    """Render a styled error state that matches the rest of the interface."""
    return f"""
    <section class="bh-shell">
        <div class="bh-card bh-error-card">
            <div class="bh-kicker">Twilight data unavailable</div>
            <h2 class="bh-error-title">Could not calculate tonight's walk.</h2>
            <p class="bh-error-copy">{escape(message)}</p>
        </div>
    </section>
    """


def render_result(context):
    """Render the atmospheric HTML result card for the selected date."""
    return f"""
    <section class="bh-shell">
        <div class="bh-card bh-quote-card">
            <p class="bh-quote">{DIDION_QUOTE}</p>
            <p class="bh-attribution">— {DIDION_ATTR}</p>
        </div>

        <div class="bh-card bh-walk-card">
            <div class="bh-meta-row">
                <span class="bh-kicker">Evening walk prediction</span>
                <span class="bh-location">Godfrey, Illinois</span>
            </div>
            <h2 class="bh-date">{context["display_date"]}</h2>
            <div class="bh-time-block">
                <div class="bh-time-label">Start your walk at</div>
                <div class="bh-time">{fmt_time(context["walk_start"])}</div>
                <div class="bh-time-sub">
                    A centered {WALK_MINUTES}-minute walk from {fmt_time(context["walk_start"])}
                    to {fmt_time(context["walk_end"])}
                </div>
            </div>

            <div class="bh-callout-row">
                <div class="bh-pill">
                    <span class="bh-pill-label">Predicted bluest moment</span>
                    <span class="bh-pill-value">{fmt_time(context["bluest_moment"])}</span>
                </div>
                <div class="bh-pill">
                    <span class="bh-pill-label">Local offset</span>
                    <span class="bh-pill-value">{LOCAL_OFFSET_MINUTES} minutes earlier</span>
                </div>
            </div>
        </div>

        <div class="bh-card">
            <div class="bh-section-head">
                <span class="bh-kicker">Twilight timeline</span>
                <span class="bh-section-note">Sunset to nautical twilight end</span>
            </div>
            <div class="bh-timeline">
                <div
                    class="bh-walk-window"
                    style="left: {context["walk_left"]:.2f}%; width: {context["walk_width"]:.2f}%"
                ></div>
                <div class="bh-marker" style="left: {context["sunset_pct"]:.2f}%">
                    <span class="bh-marker-dot sun"></span>
                    <span class="bh-marker-label">Sunset</span>
                    <span class="bh-marker-time">{fmt_time(context["sunset"])}</span>
                </div>
                <div class="bh-marker" style="left: {context["dusk_pct"]:.2f}%">
                    <span class="bh-marker-dot civil"></span>
                    <span class="bh-marker-label">Dusk</span>
                    <span class="bh-marker-time">{fmt_time(context["dusk"])}</span>
                </div>
                <div class="bh-marker bh-marker-featured" style="left: {context["bluest_pct"]:.2f}%">
                    <span class="bh-marker-dot blue"></span>
                    <span class="bh-marker-label">Bluest moment</span>
                    <span class="bh-marker-time">{fmt_time(context["bluest_moment"])}</span>
                </div>
                <div class="bh-marker" style="left: {context["nautical_pct"]:.2f}%">
                    <span class="bh-marker-dot nautical"></span>
                    <span class="bh-marker-label">Nautical end</span>
                    <span class="bh-marker-time">{fmt_time(context["nautical_end"])}</span>
                </div>
            </div>
            <div class="bh-timeline-caption">
                The highlighted band is the recommended walk window, centered on the locally adjusted bluest point.
            </div>
        </div>

        <div class="bh-stats">
            <div class="bh-card bh-stat-card">
                <div class="bh-stat-label">Sunset (API)</div>
                <div class="bh-stat-value">{fmt_time(context["sunset"])}</div>
            </div>
            <div class="bh-card bh-stat-card">
                <div class="bh-stat-label">Dusk (API)</div>
                <div class="bh-stat-value">{fmt_time(context["dusk"])}</div>
            </div>
            <div class="bh-card bh-stat-card">
                <div class="bh-stat-label">Blue hour span</div>
                <div class="bh-stat-value">{fmt_duration_minutes(context["blue_hour_minutes"])}</div>
            </div>
            <div class="bh-card bh-stat-card">
                <div class="bh-stat-label">Daylight</div>
                <div class="bh-stat-value">{context["day_length"]}</div>
            </div>
        </div>

        <div class="bh-card bh-note-card">
            <div class="bh-note-title">How this stays grounded in the local landscape</div>
            <p class="bh-note-copy">
                Twilight times come directly from the API for Godfrey, IL ({LAT:.4f}, {LNG:.4f}).
                The astronomical midpoint is then shifted {LOCAL_OFFSET_MINUTES} minutes earlier to reflect
                the observed western horizon, and the walk is centered on that adjusted moment.
            </p>
        </div>
    </section>
    """


def calculate_blue_hour(date_str):
    """Calculate the predicted bluest moment and render the HTML panel."""
    try:
        context = build_walk_context(date_str)
    except Exception as exc:
        return render_error(f"Could not fetch twilight data: {exc}")
    return render_result(context)


def on_load():
    """Calculate for today on first load."""
    tz = pytz.timezone(TZID)
    today = datetime.now(tz).strftime("%Y-%m-%d")
    return today, calculate_blue_hour(today)


def on_date_change(date_str):
    """Recalculate when the date changes."""
    if not date_str:
        return render_error("Choose a date to calculate the evening walk window.")
    return calculate_blue_hour(date_str)


HEADER_HTML = f"""
<section class="bh-hero">
    <div class="bh-hero-copy">
        <div class="bh-kicker">The Bluest Hour</div>
        <h1 class="bh-title">A calmer way to catch the evening blue.</h1>
        <p class="bh-intro">
            A small Gradio Space that tells you when to start a twilight walk in Godfrey, Illinois,
            so that twenty quiet minutes are centered on the deepest local blue.
        </p>
    </div>
    <div class="bh-hero-aside">
        <div class="bh-hero-chip">Godfrey, IL</div>
        <div class="bh-hero-chip">35-minute local offset</div>
        <div class="bh-hero-chip">Twilight data from the API</div>
    </div>
</section>
"""


FOOTER_HTML = """
<div class="bh-footer">
    Twilight data from <a href="https://sunrisesunset.io/api/" target="_blank" rel="noopener noreferrer">sunrisesunset.io</a>
    for Godfrey, Illinois. The walk recommendation keeps the original local offset and centered 20-minute window.
</div>
"""


CSS = """
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Manrope:wght@400;500;600;700&display=swap');

:root {
    --bh-night: #091321;
    --bh-indigo: #10233c;
    --bh-twilight: #1d466d;
    --bh-sky: #4075a8;
    --bh-glow: #d7b267;
    --bh-amber: #c9833e;
    --bh-mist: #f2ece2;
    --bh-soft: rgba(242, 236, 226, 0.74);
    --bh-card: rgba(10, 24, 40, 0.46);
    --bh-card-strong: rgba(8, 18, 31, 0.68);
    --bh-border: rgba(215, 178, 103, 0.22);
    --bh-line: rgba(255, 255, 255, 0.16);
    --bh-shadow: 0 24px 70px rgba(4, 10, 20, 0.42);
}

html, body {
    min-height: 100%;
    background:
        radial-gradient(circle at top, rgba(215, 178, 103, 0.18), transparent 30%),
        linear-gradient(180deg, #07111d 0%, #0d2034 20%, #173658 46%, #316491 70%, #7f91a9 88%, #cf9347 100%);
    color: var(--bh-mist);
}

body {
    font-family: 'Manrope', 'Avenir Next', 'Segoe UI', sans-serif;
}

.gradio-container {
    max-width: 980px !important;
    margin: 0 auto;
    padding: 32px 18px 56px !important;
    background: transparent !important;
}

.gradio-container .prose,
.gradio-container .prose * {
    color: inherit;
}

#bh-controls,
#bh-results {
    border: none !important;
    background: transparent !important;
    box-shadow: none !important;
    padding: 0 !important;
}

.bh-hero {
    display: grid;
    grid-template-columns: minmax(0, 1.5fr) minmax(220px, 0.8fr);
    gap: 18px;
    align-items: end;
    margin-bottom: 22px;
}

.bh-kicker {
    font-size: 0.75rem;
    letter-spacing: 0.24em;
    text-transform: uppercase;
    color: rgba(242, 236, 226, 0.76);
    margin-bottom: 10px;
}

.bh-title {
    margin: 0;
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(3.2rem, 6vw, 4.9rem);
    line-height: 0.9;
    font-weight: 600;
    letter-spacing: 0.01em;
}

.bh-intro {
    margin: 18px 0 0;
    max-width: 620px;
    font-size: 1rem;
    line-height: 1.75;
    color: var(--bh-soft);
}

.bh-hero-aside {
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-self: center;
}

.bh-hero-chip {
    padding: 12px 14px;
    border: 1px solid var(--bh-border);
    border-radius: 999px;
    background: rgba(9, 19, 33, 0.34);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    font-size: 0.82rem;
    color: rgba(242, 236, 226, 0.84);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.05);
}

#date-input {
    margin-bottom: 10px;
}

#date-input label {
    font-size: 0.78rem !important;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: rgba(242, 236, 226, 0.72) !important;
}

#date-input .wrap,
#date-input .form,
#date-input .container {
    background: transparent !important;
}

#date-input input {
    min-height: 58px;
    border-radius: 18px !important;
    border: 1px solid var(--bh-border) !important;
    background: rgba(8, 18, 31, 0.42) !important;
    color: var(--bh-mist) !important;
    box-shadow: var(--bh-shadow);
    padding: 0 18px !important;
    font-size: 1rem !important;
}

#date-input input:focus {
    border-color: rgba(215, 178, 103, 0.52) !important;
    box-shadow: 0 0 0 1px rgba(215, 178, 103, 0.34), var(--bh-shadow) !important;
}

.bh-shell {
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.bh-card {
    position: relative;
    overflow: hidden;
    border-radius: 26px;
    border: 1px solid var(--bh-border);
    background: linear-gradient(180deg, rgba(10, 24, 40, 0.72) 0%, rgba(9, 21, 35, 0.48) 100%);
    box-shadow: var(--bh-shadow);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    padding: 22px;
}

.bh-card::before {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(140deg, rgba(255, 255, 255, 0.08), transparent 38%);
    pointer-events: none;
}

.bh-quote-card {
    padding: 22px 24px 20px;
}

.bh-quote {
    margin: 0;
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(1.32rem, 2vw, 1.62rem);
    line-height: 1.45;
    color: rgba(242, 236, 226, 0.92);
}

.bh-attribution {
    margin: 10px 0 0;
    color: rgba(242, 236, 226, 0.7);
    font-size: 0.88rem;
    letter-spacing: 0.03em;
}

.bh-walk-card {
    padding: 26px;
    background:
        radial-gradient(circle at top right, rgba(215, 178, 103, 0.16), transparent 32%),
        linear-gradient(180deg, rgba(8, 20, 34, 0.82) 0%, rgba(22, 57, 90, 0.72) 58%, rgba(58, 95, 132, 0.56) 100%);
}

.bh-meta-row,
.bh-section-head {
    display: flex;
    justify-content: space-between;
    gap: 14px;
    align-items: center;
    flex-wrap: wrap;
}

.bh-location,
.bh-section-note {
    font-size: 0.84rem;
    color: rgba(242, 236, 226, 0.72);
}

.bh-date {
    margin: 12px 0 0;
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(2rem, 3.3vw, 2.9rem);
    font-weight: 500;
    line-height: 1;
}

.bh-time-block {
    margin-top: 20px;
    text-align: center;
    padding: 20px 18px;
    border-radius: 22px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.12);
}

.bh-time-label,
.bh-pill-label,
.bh-stat-label,
.bh-marker-label {
    font-size: 0.74rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
}

.bh-time-label {
    color: rgba(242, 236, 226, 0.72);
}

.bh-time {
    margin-top: 8px;
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(3rem, 7vw, 4.4rem);
    line-height: 0.92;
    color: #f3dc9a;
    text-shadow: 0 0 28px rgba(215, 178, 103, 0.22);
}

.bh-time-sub {
    margin-top: 10px;
    font-size: 0.95rem;
    color: rgba(242, 236, 226, 0.82);
}

.bh-callout-row {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
    margin-top: 16px;
}

.bh-pill {
    display: flex;
    flex-direction: column;
    gap: 6px;
    padding: 16px 18px;
    border-radius: 18px;
    background: rgba(9, 19, 33, 0.34);
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.bh-pill-value {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.45rem;
    color: var(--bh-mist);
}

.bh-timeline {
    position: relative;
    height: 118px;
    margin-top: 18px;
    border-radius: 24px;
    overflow: hidden;
    border: 1px solid rgba(255, 255, 255, 0.1);
    background:
        linear-gradient(90deg, rgba(210, 134, 62, 0.9) 0%, rgba(105, 152, 197, 0.95) 22%, rgba(47, 95, 145, 0.98) 52%, rgba(16, 35, 60, 1) 82%, rgba(8, 17, 29, 1) 100%);
}

.bh-timeline::after {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.06), transparent 40%, rgba(4, 10, 20, 0.28) 100%);
    pointer-events: none;
}

.bh-walk-window {
    position: absolute;
    top: 14px;
    bottom: 14px;
    min-width: 18px;
    border-radius: 18px;
    background: rgba(243, 220, 154, 0.18);
    border-left: 2px solid rgba(243, 220, 154, 0.95);
    border-right: 2px solid rgba(243, 220, 154, 0.95);
    box-shadow: 0 0 32px rgba(243, 220, 154, 0.16);
}

.bh-marker {
    position: absolute;
    top: 14px;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    text-align: center;
    min-width: 96px;
    z-index: 2;
}

.bh-marker-dot {
    width: 10px;
    height: 10px;
    border-radius: 999px;
    box-shadow: 0 0 0 3px rgba(9, 19, 33, 0.35);
}

.bh-marker-dot.sun { background: #f1b35a; }
.bh-marker-dot.civil { background: #84acd3; }
.bh-marker-dot.blue { background: #d9dff9; }
.bh-marker-dot.nautical { background: #112742; }

.bh-marker-label {
    color: rgba(242, 236, 226, 0.82);
}

.bh-marker-time {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.08rem;
    color: var(--bh-mist);
}

.bh-marker-featured .bh-marker-time {
    color: #f3dc9a;
}

.bh-timeline-caption {
    margin-top: 12px;
    color: rgba(242, 236, 226, 0.72);
    font-size: 0.92rem;
    line-height: 1.65;
}

.bh-stats {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
}

.bh-stat-card {
    min-height: 126px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: linear-gradient(180deg, rgba(9, 19, 33, 0.58), rgba(10, 24, 40, 0.42));
}

.bh-stat-label {
    color: rgba(242, 236, 226, 0.68);
}

.bh-stat-value {
    margin-top: 18px;
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(1.8rem, 3vw, 2.4rem);
    line-height: 1;
    color: var(--bh-mist);
}

.bh-note-title,
.bh-error-title {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.9rem;
    line-height: 1.05;
    margin: 0;
}

.bh-note-copy,
.bh-error-copy {
    margin: 12px 0 0;
    color: rgba(242, 236, 226, 0.8);
    line-height: 1.75;
    font-size: 0.96rem;
}

.bh-error-card {
    background: linear-gradient(180deg, rgba(44, 18, 21, 0.76), rgba(20, 11, 14, 0.66));
    border-color: rgba(224, 133, 110, 0.28);
}

.bh-footer {
    margin-top: 18px;
    color: rgba(242, 236, 226, 0.62);
    font-size: 0.84rem;
    line-height: 1.7;
    text-align: center;
}

.bh-footer a {
    color: #f1cd84;
    text-decoration: none;
}

.bh-footer a:hover {
    text-decoration: underline;
}

@media (max-width: 820px) {
    .bh-hero {
        grid-template-columns: 1fr;
    }

    .bh-hero-aside {
        flex-direction: row;
        flex-wrap: wrap;
    }
}

@media (max-width: 680px) {
    .gradio-container {
        padding: 20px 12px 42px !important;
    }

    .bh-card,
    .bh-walk-card {
        padding: 18px;
        border-radius: 22px;
    }

    .bh-callout-row,
    .bh-stats {
        grid-template-columns: 1fr;
    }

    .bh-timeline {
        height: 168px;
        padding-top: 6px;
    }

    .bh-marker {
        min-width: 70px;
    }
}

@media (max-width: 520px) {
    .bh-title {
        font-size: 2.9rem;
    }

    .bh-date {
        font-size: 2rem;
    }

    .bh-time {
        font-size: 3rem;
    }

    .bh-quote {
        font-size: 1.2rem;
    }

    .bh-marker {
        top: 12px;
        min-width: 58px;
    }

    .bh-marker-label {
        font-size: 0.6rem;
        letter-spacing: 0.12em;
    }

    .bh-marker-time {
        font-size: 0.92rem;
    }
}
"""


with gr.Blocks(title="The Bluest Hour", css=CSS) as demo:
    gr.HTML(HEADER_HTML)

    with gr.Group(elem_id="bh-controls"):
        date_input = gr.Textbox(
            label="Choose a date",
            placeholder="YYYY-MM-DD",
            max_lines=1,
            elem_id="date-input",
            html_attributes={"type": "date"},
        )

    result = gr.HTML(elem_id="bh-results")
    gr.HTML(FOOTER_HTML)

    date_input.change(fn=on_date_change, inputs=date_input, outputs=result)
    date_input.submit(fn=on_date_change, inputs=date_input, outputs=result)
    demo.load(fn=on_load, outputs=[date_input, result])

demo.launch()
