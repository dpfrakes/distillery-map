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

### Continued

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

## Another Idea

With all the back and forth on geolocation data, and the messy import method (manually scraped Wikipedia, imported and try to fuzzy-merge with
CSV found on the web), I started looking into best practices with regard to saving, storing, and sharing datasets. I figure I could make my
own dataset with what I have now, plus manually-curated list I can update at will.

While researching, I stumbled across some cool data visualizations related to scotch (thanks Reddit).

https://new.reddit.com/search/?q=whiskey%20dataset
https://i.imgur.com/1fh6eyc.png
https://web.archive.org/web/20120110023047/http://www.whiskyclassified.com/classification.html
https://new.reddit.com/r/dataisbeautiful/comments/8x6b8c/oc_how_expensive_is_decent_whiskey/

Specifically, that last one got me thinking: it'd be nice to look up how much these scotches cost locally. For me, in Virginia, we only
have state-run liquor stores. The selection isn't great, but it does make for an easy web scraping target.

### Scraping ABCs

First, search for scotch on ABC's website:

  https://www.abc.virginia.gov/products/scotch

Note the URL automatically updates with some helpful query params:

  https://www.abc.virginia.gov/products/scotch#sort=relevancy&numberOfResults=12

Next, inspect the network calls for XHR requests to see what's being called to get your results:

  https://www.abc.virginia.gov/coveo/rest/v2?sitecoreItemUri=sitecore%3A%2F%2Fpubweb%2F%7BC5781676-5EFD-4D25-8A54-723F2AC24ADC%7D%3Flang%3Den%26amp%3Bver%3D44&siteName=website

Damn, looks like maybe a session token or something... might as well try the API base URL to see if we get any hints:

  https://www.abc.virginia.gov/coveo/rest/v2/

Well how about that? Open API with 123,315 results! Time to whittle it down using trial-and-error query params like `q` or `s`:

  https://www.abc.virginia.gov/coveo/rest/v2?q=scotch

This is too easy. Okay so 4,499 results for "scotch"... let's try a brand:

  https://www.abc.virginia.gov/coveo/rest/v2?q=bowmore

Perfect, 68 results! Now let's throw that helpful query param from before back in to de-paginate:

  https://www.abc.virginia.gov/coveo/rest/v2?q=bowmore&numberOfResults=100

That returned all 68 results in one request fast enough, but I might need to paginate and make multiple reqeuests
to avoid request timeout errors. Usually there's a `page` or `offset` or `start` param to indicate "ignore the first
{numberOfResults} results" or "go straight to page {page}". Back to the manual search page on their website:

  https://www.abc.virginia.gov/products/scotch#first=12&sort=relevancy&numberOfResults=12

Ah, so it's `first`. Let's try it on the API:

  jfdslk

Damn, not a 1-to-1 mapping apparently. Ok, let's compare page 2 and page 3 from manual search:

  https://www.abc.virginia.gov/coveo/rest/v2?sitecoreItemUri=sitecore%3A%2F%2Fpubweb%2F%7BC5781676-5EFD-4D25-8A54-723F2AC24ADC%7D%3Flang%3Den%26amp%3Bver%3D44&siteName=website
  https://www.abc.virginia.gov/coveo/rest/v2?sitecoreItemUri=sitecore%3A%2F%2Fpubweb%2F%7BC5781676-5EFD-4D25-8A54-723F2AC24ADC%7D%3Flang%3Den%26amp%3Bver%3D44&siteName=website

Both URLs are the same as the original request, so it's not a simple GET param. Let's check the form data associated with page 2:

```txt
# page 2
actionsHistory=%5B%7B%22name%22%3A%22Query%22%2C%22time%22%3A%22%5C%222020-04-28T03%3A46%3A50.788Z%5C%22%22%7D%2C%7B%22name%22%3A%22PageView%22%2C%22value%22%3A%22C57816765EFD4D258A54723F2AC24ADC%22%2C%22time%22%3A%22%5C%222020-04-28T03%3A46%3A49.908Z%5C%22%22%7D%2C%7B%22name%22%3A%22PageView%22%2C%22value%22%3A%22https%3A%2F%2Fwww.abc.virginia.gov%2F%22%2C%22time%22%3A%22%5C%222020-04-28T03%3A46%3A48.895Z%5C%22%22%2C%22title%22%3A%22Virginia%20ABC%22%7D%2C%7B%22name%22%3A%22PageView%22%2C%22value%22%3A%22110D559FDEA542EA9C1C8A5DF7E70EF9%22%2C%22time%22%3A%22%5C%222020-04-28T03%3A46%3A46.635Z%5C%22%22%7D%2C%7B%22name%22%3A%22Query%22%2C%22time%22%3A%22%5C%222020-04-28T02%3A08%3A20.794Z%5C%22%22%7D%2C%7B%22name%22%3A%22PageView%22%2C%22value%22%3A%22C57816765EFD4D258A54723F2AC24ADC%22%2C%22time%22%3A%22%5C%222020-04-28T02%3A08%3A19.062Z%5C%22%22%7D%2C%7B%22name%22%3A%22Query%22%2C%22time%22%3A%22%5C%222020-04-28T02%3A08%3A14.422Z%5C%22%22%7D%2C%7B%22name%22%3A%22PageView%22%2C%22value%22%3A%22C57816765EFD4D258A54723F2AC24ADC%22%2C%22time%22%3A%22%5C%222020-04-28T02%3A08%3A12.719Z%5C%22%22%7D%2C%7B%22name%22%3A%22Query%22%2C%22time%22%3A%22%5C%222020-04-28T02%3A07%3A55.402Z%5C%22%22%7D%2C%7B%22name%22%3A%22PageView%22%2C%22value%22%3A%22C57816765EFD4D258A54723F2AC24ADC%22%2C%22time%22%3A%22%5C%222020-04-28T02%3A07%3A53.890Z%5C%22%22%7D%2C%7B%22name%22%3A%22PageView%22%2C%22value%22%3A%22E2EC12BD36B344B3B6E26C28DB615DFF%22%2C%22time%22%3A%22%5C%222020-04-28T02%3A07%3A50.386Z%5C%22%22%7D%2C%7B%22name%22%3A%22PageView%22%2C%22value%22%3A%2248BF7CBD7A0B4F1A91BAC3E4ED93AE52%22%2C%22time%22%3A%22%5C%222020-04-11T21%3A03%3A13.747Z%5C%22%22%7D%2C%7B%22name%22%3A%22PageView%22%2C%22value%22%3A%22https%3A%2F%2Fwww.abc.virginia.gov%2F%22%2C%22time%22%3A%22%5C%222020-04-11T21%3A03%3A07.509Z%5C%22%22%2C%22title%22%3A%22Virginia%20ABC%22%7D%2C%7B%22name%22%3A%22PageView%22%2C%22value%22%3A%22110D559FDEA542EA9C1C8A5DF7E70EF9%22%2C%22time%22%3A%22%5C%222020-04-11T21%3A03%3A06.517Z%5C%22%22%7D%5D&
referrer=&
visitorId=6b1247e8-12e0-4f06-ba90-adafd361a1e7&
isGuestUser=false&
aq=(NOT%20(%40z95xproductz32xlabelz32xduplicate%20%3D%3D%20'True'))%20(%40z95xtemplate%3D%3D08A7C8E8BD0F406192E13D1C48231E87%20(%40hierarchyz32xtype%3D%3D(%22Scotch%22)))%20(%40source%3D%3D%22Coveo_pubweb_index%20-%20prod%22)&
cq=(%40z95xlanguage%3D%3Den)%20(%40z95xlatestversion%3D%3D1)&
searchHub=ProductsSearchHub&
locale=en&
maximumAge=900000&
firstResult=36&
numberOfResults=12&
excerptLength=200&
enableDidYouMean=true&
sortCriteria=relevancy&
queryFunctions=%5B%5D&
rankingFunctions=%5B%5D&
groupBy=%5B%7B%22field%22%3A%22%40z95xproductz32xviews%22%2C%22maximumNumberOfValues%22%3A6%2C%22sortCriteria%22%3A%22occurrences%22%2C%22injectionDepth%22%3A1000%2C%22completeFacetWithStandardValues%22%3Afalse%2C%22allowedValues%22%3A%5B%22Virginia-Made%22%2C%22Limited%20Availability%22%2C%22New%22%2C%22On%20Sale%22%2C%22Seasonal%22%5D%7D%2C%7B%22field%22%3A%22%40hierarchyz32xcategory%22%2C%22maximumNumberOfValues%22%3A6%2C%22sortCriteria%22%3A%22occurrences%22%2C%22injectionDepth%22%3A1000%2C%22completeFacetWithStandardValues%22%3Atrue%2C%22allowedValues%22%3A%5B%5D%7D%2C%7B%22field%22%3A%22%40hierarchyz32xtype%22%2C%22maximumNumberOfValues%22%3A6%2C%22sortCriteria%22%3A%22occurrences%22%2C%22injectionDepth%22%3A1000%2C%22completeFacetWithStandardValues%22%3Atrue%2C%22allowedValues%22%3A%5B%5D%7D%2C%7B%22field%22%3A%22%40z95xalphaz32xrange%22%2C%22maximumNumberOfValues%22%3A6%2C%22sortCriteria%22%3A%22occurrences%22%2C%22injectionDepth%22%3A1000%2C%22completeFacetWithStandardValues%22%3Atrue%2C%22allowedValues%22%3A%5B%5D%7D%2C%7B%22field%22%3A%22%40z95xproductz32xsiz122xe%22%2C%22maximumNumberOfValues%22%3A42%2C%22sortCriteria%22%3A%22nosort%22%2C%22injectionDepth%22%3A1000%2C%22completeFacetWithStandardValues%22%3Atrue%2C%22allowedValues%22%3A%5B%2250%20ml%22%2C%22100%20ml%22%2C%22118%20ml%22%2C%22148%20ml%22%2C%22150%20ml%22%2C%22175%20ml%22%2C%22200%20ml%22%2C%22236%20ml%22%2C%228%20oz%22%2C%22237%20ml%22%2C%22250%20ml%22%2C%22300%20ml%22%2C%2212%20oz%22%2C%22355%20ml%22%2C%22375%20ml%22%2C%22400%20ml%22%2C%2216%20oz%22%2C%22473.18%20ml%22%2C%2216.9%20oz%22%2C%22500%20ml%22%2C%22600%20ml%22%2C%2225%20oz%22%2C%22750%20ml%22%2C%22800%20ml%22%2C%22800%20ml%22%2C%22946%20ml%22%2C%2232%20oz%22%2C%221%20L%22%2C%221.13%20L%22%2C%221.2%20L%22%2C%2248%20oz%22%2C%221.42%20L%22%2C%221.5%20L%22%2C%221.75%20L%22%2C%2260%20oz%22%2C%2264%20oz%22%2C%222.1%20L%22%2C%2272%20oz%22%2C%2296%20oz%22%2C%223.5%20L%22%2C%2210%20L%22%5D%7D%2C%7B%22field%22%3A%22%40z95xproductz32xpricez32xsort%22%2C%22maximumNumberOfValues%22%3A7%2C%22sortCriteria%22%3A%22nosort%22%2C%22injectionDepth%22%3A1000%2C%22completeFacetWithStandardValues%22%3Atrue%2C%22rangeValues%22%3A%5B%7B%22start%22%3A%220%22%2C%22end%22%3A%2210%22%2C%22endInclusive%22%3Afalse%2C%22label%22%3A%22Under%20%2410.00%22%7D%2C%7B%22start%22%3A%2210%22%2C%22end%22%3A%2220%22%2C%22endInclusive%22%3Afalse%2C%22label%22%3A%221020%22%7D%2C%7B%22start%22%3A%2220%22%2C%22end%22%3A%2230%22%2C%22endInclusive%22%3Afalse%2C%22label%22%3A%222030%22%7D%2C%7B%22start%22%3A%2230%22%2C%22end%22%3A%2240%22%2C%22endInclusive%22%3Afalse%2C%22label%22%3A%223040%22%7D%2C%7B%22start%22%3A%2240%22%2C%22end%22%3A%2250%22%2C%22endInclusive%22%3Afalse%2C%22label%22%3A%224050%22%7D%2C%7B%22start%22%3A%2250%22%2C%22end%22%3A%2275%22%2C%22endInclusive%22%3Afalse%2C%22label%22%3A%225075%22%7D%2C%7B%22start%22%3A%2275%22%2C%22end%22%3A%2299999999%22%2C%22endInclusive%22%3Afalse%2C%22label%22%3A%2275over%22%7D%5D%7D%5D&
facetOptions=%7B%7D&
categoryFacets=%5B%5D&
retrieveFirstSentences=true&
timezone=America%2FNew_York&
enableQuerySyntax=false&
enableDuplicateFiltering=false&
enableCollaborativeRating=false&
debug=false&
allowQueriesWithoutKeywords=true
```

So searching that mess for `first`, there is a `firstResult` param instead. Let's try that.
Interesting side note: it appears to store action history, probably from a cookie (don't really care enough to verify though).

  https://www.abc.virginia.gov/coveo/rest/v2?firstResult=50&q=bowmore&numberOfResults=50

Booyah, 18 results as expected for a "50-per-page but start after the first 50 results" request. Let's see what happens when we overshoot the total results:

  https://www.abc.virginia.gov/coveo/rest/v2?firstResult=70&q=bowmore&numberOfResults=50

Same format, no errors, just 0 results. Perfect. Brute force method will work: query till we can't query anymore.

#### Additional Hacking

From the results, it looks like each item has a `uri` pointing to `sitecore://database/...`, so we know ABC uses [Sitecore Content Management](https://doc.sitecore.com/developers/90/platform-administration-and-architecture/en/content-management--cm-.html).

Browsing through the `raw` details of each result, we've even got an email address associated with `createdby` field. Maybe worth a web search in case I'm curious in finding out the type of person (job quals) who does at least some data entry. Or for fun: make a chart of contributors like Github.

Product images also a plus, maybe I can inject those into my site.

After a text search of the JSON result, it looks like the **price info can be found** under `raw.z95xproductz32xpricez32xsort`.

Searched `bruichladdich` and found an item with the title "Out of Stock Report 4-10-20" with a URI pointing to an xlsx document. Cool, free spreadsheets!

### Scripting Time

Time to plan my scrape.

For now, I just want scotch prices (not whiskey, Irish, bourbon, etc.), so I'll stick with `q=scotch`. This returned 4,499 results. Testing with manual queries, returning 1,000 results actually wasn't too slow, and querying for any more than 1,000 always returned 1,000 anyway, so there's your server-side limit. So we should be able to do this in 5 queries of up to 1,000 results each.

This seems like another case of a company that doesn't budget enough on tech security, but on the off-chance they actually monitor the logs, I'd rather they not see my IP if they notice someone making a bunch of automated requests to scrape their data. So at the expense of slower speeds, I'll be using a VPN.

Additionally, I'd like this to be a flat file, but the nested JSON results don't make for an easy 1-to-1 CSV conversion. I'd like to keep results as "raw" as possiible, but
storing a massive dictionary in memory isn't ideal, especially if the network slows down or the scrape ends up consisting of a lot of requests. So I'll write to individual JSON files for
now and figure out how I want to consolidate/organize/store these data later.

#### Pre-emptive Search Optimization

Since I'm really only interested in a few fields (image, title, price, and maybe a few others), I want to see if there is another query param available to only return certain fields
in my results so that the API calls return faster. I noticed `coveo` in both the API URL as well as a few other network call URLs. A quick Google search reveals: they're using
[Coveo](https://www.coveo.com/en) as their API service provider. A few more hyperlink jumps points me to their [product docs](https://docs.coveo.com/en/2709/).

From their Sitecore 5 > Building Search > [Retrieving Results page](https://docs.coveo.com/en/2883/):

> Now that you have a search interface set up with the basic components,
> you’re ready to display results. Although it sounds straight forward,
> there are key concepts you don’t want to overlook before going forward.
>
> There are many ways, client-side or server-side, to alter search results
> before displaying them (see [Altering Search Results Before They Are Displayed](https://docs.coveo.com/en/2713/)).

However, this looks like Java documentation: I'm looking for API docs so a lowly end user has some control over results filtering.

Instead, I searched Coveo's documentation for `numberOfResults` since I knew that would be in the same docs as whatever query param I was (hoping) to find. Et voila:

https://docs.coveo.com/en/13/cloud-v2-api-reference/search-api#operation/valuesBatchPost

It doesn't look like there's any easy way to pre-filter the fields returned, especially for something only found within `raw`, so we'll surrender this investigation and just query everything.

Also for future exploration, in particular the `aq` looks promising, like JQL in Jira:

https://docs.coveo.com/en/1461/cloud-v2-developers/query-parameters

### Trial

That failed on page 2:

https://www.abc.virginia.gov/coveo/rest/v2?q=scotch&firstResult=1000&numberOfResults=1000

```json
{"totalCount":0,"totalCountFiltered":0,"duration":38,"indexDuration":3,"requestDuration":1,"searchUid":"d047534e-1b10-4924-af5c-bb57c994bc69","pipeline":"default","apiVersion":2,"exception":{"code":"RequestedResultsMax","context":""},"index":"cache","refinedKeywords":[],"triggers":[],"termsToHighlight":{},"phrasesToHighlight":{},"queryCorrections":[],"groupByResults":[],"facets":[],"suggestedFacets":[],"categoryFacets":[],"results":[]}
```

Exception message is helpful: `RequestedResultsMax`. Might be querying too much from my IP, or just asking for too many results. Let's test the latter since that's easier to tweak:

https://www.abc.virginia.gov/coveo/rest/v2?q=scotch&firstResult=100&numberOfResults=100

Seems fine.

https://www.abc.virginia.gov/coveo/rest/v2?q=scotch&firstResult=1000&numberOfResults=100

Nope, looks like the API won't ever return past the 1,000th result for a particular query. Time to switch up the query, let's base it off individual brands/distilleries:

| Query               | Total Results |
|---------------------|---------------|
| `q=bowmore`         | 68            |
| `q=bruichladdich`   | 235           |
| `q=ardbeg`          | 224           |
| `q=kilchoman`       | 108           |
| `q=lagavulin`       | 126           |
| `q=caol%20ila`      | 88            |

These results look much more manageable: way under the 1,000 limit, each can be a single paginated query, plus saving directly to file means each one of these files can be named after a particular brand which is much easier to filter through the flat files after the fact.

## You know you're in trouble when

https://support.google.com/websearch/answer/86640?hl=en&dark=1

### Database setup

Now that I've scraped and stored straight JSON files for each brand, I noticed there are a few products with price ranges instead of explicit prices. After a closer look, this is due to the multiple bottle sizes returned for a particular product.

So I can either add a filter for a particular bottlee size and re-run the search, but that could mean excluding a whole product if it's not offered at the specific volume I query. Looking back through the JSON, I found `z95xproductz32xsiz122xe` indicating the sizes available, and it looks like both this `sizes` and the `prices` are in ascending order, so probably a safe assumption that I can map these arrays on index. (On the site, I'll probably just include 750ml since that's the standard bottle size, but that's presentation layer.)

### Reconsidering ABC

As I'm looking through all the fields I "might as well" save to my database, a lot of them are specific to ABC (product ID, hierarchical classification), so I think I'd rather have a DB table dedicated to ABC, then link to it via a `source` field on Scotch.

My mind is already thinking "But what about multiple sources? You should add a sparse matrix of `source_X` for each source and have each field be boolean!" But this is way overkill for the data I want right now for my app. I think I'm just excited I have lots of free data with which to work.

## Run the Script

After a few stupid compilation errors, I ran into some understandable KeyErrors so I decided to wrap every update to `ABCInfo` fields in a try/except block. Lots of missing skus and names. SKUs I guess I can live without, as long as the model is updated to make that an optional field (I was expecting it to be a unique ID for product/size combination).

Missing name is more concerning, so looking through a failed result, there are a lot of fields that all have what I'm looking for in a name:

- `productz32xlabelz32xname`
- `fpagez32xheading61692`
- `fpagez32xtitle61692`
- `fproductz32xlabelz32xname61692`
- `fnavigationz32xtitle61692`

Hence:

```py
# Check multiple fields for name
for lookup in ['productz32xlabelz32xname', 'fpagez32xheading61692', 'fpagez32xtitle61692', 'fproductz32xlabelz32xname61692', 'fnavigationz32xtitle61692']:
    if lookup in raw:
        attrs.update({'name': raw[lookup]})
        break
```

### Refining Search

A bunch of scotches are being imported (w00t) with the wrong distillery associated with them (d'oh).

This means querying that distillery is returning other scotches that belong to other distilleries (bad ABC search, bad).

Hopefully their data hierarchy integrity is more reliable than their search algorithm. Time to query with `aq`.

First, another manual search to see the difference in results (other than name). Query of "bowmore" on their site returns the following:

- Bowmore-12-Year-Single-Malt-Scotch
- Bowmore-25-Year-Single-Malt-Scotch
- Bruichladdich-Port-Charlotte-10-Year-Scotch
- Bunnahabhain-12-Year-Single-Malt-Scotch

This is great: a small sample size with positive and negative cases.

Searching through this JSON result for a field with just "Bowmore" or "bowmore" in it turned up empty, so no data field we can query directly by distillery... that's disappointing.

I might have to rely on the `name`/`title` field anyway.

Retry import script, only saving Scotch item if `name` starts with the same word as the first word in `q`.

Before
ABCInfo objects: 357
Scotch objects: 379 (50%+ wrong distillery)

After
ABCInfo objects: 709
Scotch objects: 488

Okay so this is way better and more accurate, but there are now duplicate scotches and ABCInfo objects because I used `title` (replacing "-" with " ") instead of looking through all those candidate fields for a name match. Perhaps I still need those candidate fields since apparently the API is returning an SKU-appended version of the product as well (e.g. "Templeton-Rye-Whiskey" and "Templeton-Rye-Whiskey 027102").

Since these all appear to match SKUs (duplicates are always "PRODUCT" with SKU and "PRODUCT SKU"), I should be able to just omit the results that don't have an SKU. That would be fantastic for a densely populated database!

After adding SKU logic
ABCInfo objects: 161
Scotch objects: 157

So much better! And expectedly, there are only a few more ABCInfo objects than Scotches since they should be 1:1 except for additional size options. Still, 3 obvious issues remain:

1. There ought to be more than just 11 instances of non-750ml sizes
2. A few ABCInfo objects have duplicate SKUs still (name varies slightly, e.g. "Ardbeg 22 YO" and "Ardbeg 22 Year Scotch")
3. Some of the scotches have weird names (not capitalized, "YO" instead of "Year Old")

Regarding #2, organizing results by SKU to see duplicates, I discovered there are only the following duplicates:

- 004232: Ardbeg 22 YO / Ardbeg 22 Year Scotch
- 005002: Glenfiddich Gran Reserva 21 Year / Glenfiddich Single Malt Scotch Whisky 21 Year Old
- 100854: Ardbeg Traigh Bhan 19 Year / Ardbeg Traigh Bhan 19 Yr / Ardbeg traigh Bhan 19 Yr

This should also fix #3.

Before tackling #1, let's clean up the data we already have. Let's make SKU unique since the only duplicates are the ones above (and they're wrong).

Also, I'm already saving all these API results to local JSON files... so why am I not using those? :slam:

After making sku unique:
ABCInfo objects: 157
Scotch objects: 157

Two more issues to address:

1. Scotches being created for every ABCInfo
2. No descriptions

Moved ABCInfo object creation out from under the SKU and NAME check (still a requirement for get/create Scotch, but no longer for create/update ABCInfo).

For description, I'm probably pulling from the wrong field/key (becausee it does exist in the json response).... Alas, it's not even a field in the `update_abc_prices` script. Derp.

## Done

E

from app.models import *
ABCInfo.objects.all().delete()
Scotch.objects.all().delete()

## Companies and Owners

Owners included in ABC store API data, so now just need to create a new Company model and create instances for each one represented so far.

Most "manual" part of the project so far.

### Naming Things

Coming up with a cool "data sheet" for end users on each distillery: should include list of whiskies made by the distillery. Ended up doing lots of reading/research just from little questions like "what to name the field for 'single malt' or 'blended' whisky."

### World Map

For companies located in other countries


I want to do a visualization using lines connecting company HQs to owned properties across the globe. Cool viz/animation opportunities here.

World map (high-res) is a lot of data, so using low-res at least for development.

Might end up doing a hybrid approach: https://geojson-maps.ash.ms/ allows individual countries (low-res), so I could do Scotland/UK high-res and all other low? Lower priority for now...

## The more automated the project (data collection, analysis) is, the less you need to know in order to teach

"Shower thought" as I was working on companies and their owned brands. Owners like Suntory, Diageo, and LVMH own more than just distilleries, but beers, perfumes, foods, and luxury items go way outside the scope of my original intention, though that was sort of the point: to learn about just how high this goes.

### Connecting companies to distilleries

https://www.d3-graph-gallery.com/graph/connectionmap_basic.html

Did a cool loading sub-screen with "✅" next to each of "map," "distilleries," and "companies."

Unfortunately, since the lines connecting distilleries to their respective companies rely on both, I needed to tweak the backend to make it one "Entities" API call that included location data, as well as relational data between companies and distillleries.

(A little research confirmed that generallly, one HTTP request is better than many small ones, e.g. one for every entity.)
