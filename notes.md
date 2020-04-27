# Notes

These are informal notes taken as I worked on this project.

General framework in mind from the beginning:

1. Get coordinates and any other easily-accessible data about all Scottish distilleries
1. Create Django app with Distillery model to store data
1. Create import operation to idempotently dump more data into the app as I find it
1. Create basic presentation layer using d3 (map)

### Initial data

Wiki: copy/pasted data from https://en.wikipedia.org/wiki/List_of_whisky_distilleries_in_Scotland

More Googling:
    - https://www.datascienceblog.net/post/other/whiskey-data-annotation/ - more about taste profile comparison than geo data or ownership tree, but still had geodata, plus interesting data science blog post(s)
    - https://stackoverflow.com/questions/13455842/where-to-find-the-uks-regions-map-on-geojson-format
    - https://blog-en.openalfa.com/how-to-add-interactive-maps-to-a-web-site
    - https://github.com/kbh3rd/shptosvg/wiki
    - https://github.com/kbh3rd/shptosvg/blob/master/shptosvg.pl

Django app easy, probably overkill, may revisit with Flask or some other backbone, but getting started I wanted something I was familiar with

Import script enhanced then consolidated to just wipe the whole DB and re-add everything I'd acquired so far

I've tried several times to get going with d3, but the docs are overwhelming, and the examples either use outdated versions or are vague (no code comments)

https://medium.com/@mbostock/command-line-cartography-part-1-897aa8f8ca2c

So back to my own alma mater:
    - https://www.youtube.com/watch?v=aNbgrqRuoiE

### Source

https://martinjc.github.io/UK-GeoJSON/

### Simplify!

https://bost.ocks.org/mike/simplify/
https://www.jasondavies.com/simplify/

### Get Data as Topojson

1. find and download shapefile (`.shp`)
  - create your own (http://geojson.io)
  - find/request existing (https://martinjc.github.io/UK-GeoJSON/, https://www.ordnancesurvey.co.uk/opendatadownload/products.html)
1. install npm tools to convert shapefile
  - `npm i -g shapefile topojson`
1. convert shapefile to geojson to topojson
  - `shp2json -o output.json input-file.shp`
  - `geo2topo -o final.topojson output.json`
  - https://github.com/mbostock/shapefile#command-line-reference
1. profit

https://bost.ocks.org/mike/map/

#### Quickstart

```sh
shp2json -o data.geojson data.shp
geo2topo -o data.topojson data.geojson
toposimplify -p 100 -o simplified.topojson data.topojson
```

### Continued...

Getting weird spider web of a map, I realized the data points were likely out of order. Looking up the actual commands above (and why the included `.dbf`, `.shx`, and `.prj` files went unused), I realized I'd need another approach that included these files.

https://mapshaper.org/

Click-and-drag is great.

I should probably migrate the d3/js to ES2019 once I get it working...

### Debugging Projection

So I finally got the map looking okay through lots of trial and error with the SVG scaling and translating, though values for these operations seemed arbitrary.

#### Debugging with points

I added a few distilleries' coordinates manually to see how they lined up, and it required more translating (no scaling since they're points instead of polygons). However, even when all test points were visible and on the map, the locations didn't seem right (based on my own geographic knowledge and a sanity check from Wikimedia's map).

another resource
https://github.com/OrdnanceSurvey/GeoDataViz-Toolkit

Still debugging why the line of select distilleries seems to be an east/west trajectory instead of a north/south one. This seems to suggest I have lat/long reversed but the points don't look like they'd line up better flipping over the x=y axis. TBD.

plotted some points where I know they should be, even updated the test data manually (from datascienceblog.net's dataset) to match exactly with manual Google Maps searches for the distilleries.

Aha!

It's not the wrong projection, it looks like it's using a different geographic coordinate system (json file from UK office coordinate system != google maps coordinates)

This would explain why my painstakingly curated coordinates of Bowmore distillery in Scotland are way off:
`Screenshot from 2020-02-22 11-38-05.png`
https://community.esri.com/thread/191774-converting-geographic-coordinate-system

----

Decided to move on since I wasn't getting anywhere with debugging the projections/coordinate systems.

Implemented click and drag + zoom functionality with d3.zoom and d3.drag libraries - pretty darn easy.

```html
<script src="https://d3js.org/d3-drag.v1.min.js"></script>
<script src="https://d3js.org/d3-zoom.v1.min.js"></script>
```

```js
svg.call(d3.zoom().on('zoom', function() {
  g.attr("transform", d3.event.transform);
}));
```

but zoom wasn't applying to distillery points, so I needed to put the circles on the same `<g>` parent element as `<path>` (instead of directly onto `<svg>`)

## Wow

Got it. `d3.geoMercator()` projection means it's showingthe map of the whole world in Mercator projection.

I only have Scotland data.

So it's showing Scotland in its size and location relative to a regular world map (Mercator) :slam:

I'm an idiot.

### Testing new understanding

Use geoMercator projection, no scaling or translating

Based on d3 github wiki docs, projection is based on 960x500 map, so use `width=960, height=500`

Plot Scotland with no scale/translate/transform, then add points going [0, 0] to [90, 0]... then [0, 0] to [0, 90]

(screenshots)

Then apply projection to CENTER OF EARTH (0, 0), which looks like it's actually 0 meaning on the equator, but also 0 meaning exactly on left border of map... :thinking:

FML **I WAS FLIPPING X/Y BUT APPLYING PROJECTION BEFORE THAT FIX (USING 0/1 INDICES OF PROJECTION(d))**:

Before:

```js
      bowmore = [55.75602, -6.28381];
      auchentoshen = [55.92237, -4.43934];
      jura = [55.83301, -5.95143];
      tomatin = [57.34110, -4.01003];
      highland_park = [58.96701, -2.95222];
      points = [bowmore, auchentoshen, jura, tomatin, highland_park]
```

After:

```js
      bowmore = [55.75602, -6.28381];
      auchentoshen = [55.92237, -4.43934];
      jura = [55.83301, -5.95143];
      tomatin = [57.34110, -4.01003];
      highland_park = [58.96701, -2.95222];
      points = [bowmore, auchentoshen, jura, tomatin, highland_park]
      points = points.map((c) => [c[1], c[0]])
```

### Scaling whole thing

Ok now points are lined up.

To scale projection, I figured `scale(2)` meant 2x (200%), or _maybe_ 2% (x0.02).

Nope, docs say scaling factor "depends on projection" :slam:

So to the source code for geoMercator we go...

And it's `961 / tau` = `961 / (Math.PI * 2)` ≈ 152.9

Sure enough, `scale(153)` is the same as ommitting `scale()` entirely. VINDICATION!

So maybe 300 = 2x? Yep, looks like it (screenshots)

(scale___.png) <-- dragged to center for size comparison only

So now I should be able to edit the width/height of the SVG container along with the scale and reasonably get an appropriate sized Scotland with some trial and error.

### Redraw

On zoom, circle isn't scaling in size (1px radius looks like 300px when zoomed way in)

Solution: redraw circle by removing it and re-appending it to `<g>` on zoom event listener.

Exact formula for decent dynamic px value is TBD, but by trial and error, `2 / Math.sqrt(scale)` seems to be okay.

## It's Been a While

I haven't worked on this in a few weeks now since creating a working MVP. After going over professional goals with my boss yesterday, this project came up and I decided to get back into it.

After reviewing my notes and current site, I decided to look into a better way of storing the geospatial data.

It's slow to load and seems to take up a lot of memory in the browser, and I think replacing sqlite with postgres+postgis will help with that.

### Postgres

Since I got a new Macbook from Celerity IT a few months ago, I hadn't needed Postgres locally (I use VMs with psql on them instead).

```sh
brew install postgresql
brew services start postgresql
psql postgres
```

Then inside postgres:

```sql
CREATE USER dougie WITH PASSWORD 'scotchwhiskeyman';
CREATE DATABASE distilleries WITH OWNER dougie;
```

### New Way

Instead of creating SVG from shapefile, there's a shp2postgis (not used yet, side-tracked by trying to center/fullscreen map on all screen sizes)

Also this

```sh
pip install django-location-field
```

|                   | SQLite+Django | PostGIS+React |
|-------------------|---------------|---------------|
| Load Time         |     6.04s     |     0.96s     |
| Data Transferred  |     1.33M     |     3.28M     |
| Page Memory       |     38.4M     |     34.6M     |

### Reactify

Figured it was worth rethinking this

Adding React + django is easy, though still kind of overkill in my mind.  Django renders an empty template with no context data, then requires multiple server calls to get map data, distillery data, etc.

Virtual DOM does appear faster though, and thinking Reactively works fairly well for my object-oriented mind.

#### Adding d3

Adding d3 to the mix is tough though: d3 is about easy access to create/update the DOM, whereas React uses a virtual DOM (explicitly leaving out direct interactions to DOM).

Once we're in d3 land, there's no going back to React (components, states, etc.). So that means all JS event listeners in d3 have to call the post-rendered React components without the benefit of `setState`.

Example: hovering on d3 circle can't call `tooltip.setState({'active': true, 'distillery': {...}})`.

WHAT A PAIN.

## Getting d3 and React to play along

d3: access/update DOM
react: build virtual DOM to avoid explicitly touching touching actual DOM)

Workaround:

Render distilleries via `<Distillery />` React component (`fetch` then `setState` in `BaseMap`).
Then in `BaseMap`'s `didComponentMount` method, include d3 listener for click/drag/zoom:

```js
svg.call(d3.zoom().on('zoom', () => {
  // scale/transform
  // remove old distillery markers (rendered `<Distillery />`s)
  // add new markers via d3
  ...
}));
```

Not ideal, but the React components are loaded onto the page and don't disappear even when the rendered circles are removed by d3.
Tooltip still works as expected, and we pass off future rendering logic to d3.
