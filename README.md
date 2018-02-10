# glouton-satnogs-data-downloader
The console app is a downloader for the data provided by the satnogs network.

command example : "python ./glouton.py -s 2018-01-20T00:51:54 -e 2018-01-21T00:51:54 -n 28654"

Actual features :
-------
    * waterfall downloading
    * payload downloading
    * filters :
        * norad id
        * start date
        * end date
        * stations
    * working directory selection
    * Docker container

futur :
-------
    * filters :
        * observation status
    * automatic mode for downloading automatically the new observations of one or more satellites.
    * modules : to be able to perform some process on satnogs data directly (like the creation of one ogg file for the payloads, ...). All of this has to be modular for adding new modules easily.

All ideas or contributions are welcome. Feel free to use the [issues](https://github.com/deckbsd/glouton-satnogs-data-downloader/issues) tab :-)
