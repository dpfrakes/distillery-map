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


### Simplify!

```
https://bost.ocks.org/mike/simplify/
https://www.jasondavies.com/simplify/
```

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
