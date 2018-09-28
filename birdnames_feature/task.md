# bird_html_creater.py

JibJib needs a script that dynamically populates a HTML file with a list of all birds [jibjib-model](https://github.com/gojibjib/jibjib-model) is currently trained for. 

## Input

There are two artifacts created during build which are needed to serve the model. Both are serialized in Python's [pickle format](https://docs.python.org/3.6/library/pickle.html).

### [bird_id_map_\<version\>.pickle](https://github.com/gojibjib/jibjib-data/blob/master/birds/bird_id_map_1.pickle)

Birds are saved in a JSON file which gets dumped into a a [MongoDB](https://www.mongodb.com/) instance, resulting in [jibjib-data](https://github.com/gojibjib/jibjib-data). The model is not talking to the database, so we need to provide mappings from the scientific name of the bird, to the database ID. This pickle file itself is a Python dictionary representating that relationship:

```json
{
    "Chlidonias_niger": 0,
    "Cuculus_canorus": 1,
    ...
}
```

> The reason for having it as a dictionary and not a simple list is because lookups are later done by the scientific name. Key-based lookups in dictionaries have O(1) [time complexity](https://en.wikipedia.org/wiki/Time_complexity), where searches in arrays are O(n) in the worst case.

Querying the database for that ID will deliver the scientific name:

```bash
$ curl -sSL "https://gojibjib.org/api/birds/0?desc_de=false&desc_en=false" | python -m json.tool
{
    "status": 200,
    "message": "Bird found",
    "count": 1,
    "data": {
        "id": 0,
        "name": "Chlidonias niger",
        "genus": "Chlidonias",
        "species": "niger",
        "title_de": "Trauerseeschwalbe",
        "title_en": "Black tern",
        "desc_de": "",
        "desc_en": ""
    }
}
```

### [train_id_list_\<version\>.pickle](https://github.com/gojibjib/jibjib-data/blob/master/birds/1.1.0/train_id_list_1.1.0.pickle)

This file holds all birds the model is currently able to identify, with the index indicating the model-specific encoding:

```
["Acrocephalus_arundinaceus","Acrocephalus_palustris"m "Acrocephalus_schoenobaenus", "Acrocephalus_scirpaceus", ...]
```

## Output

A list of birds the model is currently able to identify as HTML file (default name: `birds.html`), **sorted by their database id**. Include a  link to the German and English Wikipedia entry of that specific bird:

```html
<p>Chlidonias niger | <a href="https://de.wikipedia.org/wiki/Chlidonias_Niger">Trauerseeschwalbe</a> | <a href="https://en.wikipedia.org/Chlidonias_Niger"Black tern</a></p><br>
<p>Cuculus canorus | <a href="https://de.wikipedia.org/wiki/Cuculus_canorus">Kuckuck</a> | <a href="https://en.wikipedia.org/Cuculus_canorus"Common cuckoo</a></p><br>
...
```

## Requirements

- No external libraries
- Python 2 and Python 3 support
- Use [argparse](https://docs.python.org/3.6/library/argparse.html) to pass file names (and other parameters that might change) from the command line ([example](https://github.com/gojibjib/jibjib-model/blob/master/modelbuilder.py#L15))
- Proper error handling. Print descriptive error messages and the stacktrace. Script should then exit with status code > 0. Errors could be but are not limited to:
    - Invalid paths passed to script
    - Files can't be found or opened
    - Files are empty
    - Birds in `train_id_list_<version>.pickle` not found in `bird_id_map_<version>.pickle`
    - Bird has no Wikipedia entry
    - Duplicates
- Commented code

## Nice to have

- Logger, verbosity level configurable via commandline arguments
- Unit tests
- If you're querying external APIs, be nice and build in [`time.sleep()`](https://docs.python.org/3.6/library/time.html#time.sleep) between requests

## Steps

1. Clone [jibjib-data](https://github.com/gojibjib/jibjib-data)
2. Develop on new feature branch
3. Create pull request to merge branch into origin master