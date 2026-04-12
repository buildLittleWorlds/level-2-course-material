---
title: The Bluest Hour
emoji: 🌆
colorFrom: indigo
colorTo: blue
sdk: gradio
sdk_version: "5.23.0"
app_file: app.py
pinned: false
---

# The Bluest Hour

*"In certain latitudes there comes a span of time approaching and following the summer solstice, some weeks in all, when the twilights turn long and blue."*
— Joan Didion, *Blue Nights*

A small tool that tells you when to start your evening walk in Godfrey, IL so that you're outside during the bluest hour — the period between civil and nautical twilight, when the sky deepens into Didion's "blue of the glass on a clear day at Chartres."

## How it works

The blue hour occurs when the sun is between 6° and 12° below the horizon. The app fetches today's civil and nautical twilight times from the [Sunrise-Sunset API](https://sunrise-sunset.org/api), calculates the blue hour window, and centers a 20-minute walk within it.
