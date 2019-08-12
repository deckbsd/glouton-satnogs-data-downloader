[![Known Vulnerabilities](https://snyk.io/test/github/deckbsd/glouton-satnogs-data-downloader/badge.svg)](https://snyk.io/test/github/deckbsd/glouton-satnogs-data-downloader)
[![Docker Build](https://img.shields.io/docker/build/deckbsd/glouton-satnogs-data-downloader)](https://hub.docker.com/r/deckbsd/glouton-satnogs-data-downloader/)
# glouton-satnogs-data-downloader
This cli app is a downloader for the data provided by the satnogs network and the satnogs db APIs.

Installation :
-------
```
git clone https://github.com/deckbsd/glouton-satnogs-data-downloader.git
cd glouton-satnogs-data-downloader
python ./setup.py install
```
or
```
pip install glouton
```

Usage :
-------
Examples for downloading data from the satnogs network

simple command example for downloading : 
```
python ./bin/glouton -s 2018-01-20T00:51:54 -e 2018-01-21T00:51:54 -n 28654
```
command example if you just want the payload files :
```
python ./bin/glouton -s 2018-01-20T00:51:54 -e 2018-01-21T00:51:54 -n 28654 --payload
```
command example if you want all data type from specific transmitter type, mode and uuid and apply module processing on waterfall :
```
python ./bin/glouton -s 2019-05-09T00:51:54 -e 2019-05-30T00:51:54 -n 40069 --waterfall-module TestModule,CSV --tuuid 8oBdHqMqgmMiWvRru6fWMn --ttype Transmitter --tmode LRPT
```

Examples for downloading data from the satnogs DB

simple command example for downloading frames for the satellite with the norad id 43466 from the page 1 to 100 : 
```
python ./bin/glouton --db -n 43466 --page-from 1 --page-to 100
```

Actual features :
-------
    * download data from satnogs db
    * waterfall downloading
    * payload downloading
    * filters :
        * satnogs network
            * norad id
            * start date
            * end date
            * stations
            * observation status
            * transmitter mode
            * transmitter uuid
            * transmitter type
            * vetted status
            * vetted user
        * satnogs db
            * norad id
            * page from
            * page to
            * observer
            * app_source
            * tranmitter
    * working directory selection
    * Docker container
    * modules

Future :
-------
    * automatic mode for downloading automatically the new observations of one or more satellites.

Modules :
-------

You can now create your own modules. These will be executed after each download from the category you selected. 

The module that you develop must herite from ObservationModuleBase (for data from satnogs network) or TelemetryModuleBase (for data from satnogs db) and must implement the "runAfterDownload" method. This method receive the file name (or the frame in case of download from satnogs db), the observation (or telemetry in case of download from satnogs db) and the full path as parameters.

Also the module and the name of the python file must be the same. The py file must be placed into the "modules" directory.

Here is a very simple example for a module used on the satnogs network data (this module is in the sources) :
```
from glouton.modules.observationModuleBase import ObservationModuleBase

class TestModule(ObservationModuleBase):

    def runAfterDownload(self, file_name, full_path, observation):
        print('executed after ' +  file_name)
```

Here is another example for a module used on the satnogs db data :
```
from glouton.modules.telemetryModuleBase import TelemetryModuleBase

class TestModule(TelemetryModuleBase):

    def runAfterDownload(self, frame, full_path, telemetry):
        print('executed after ' +  frame)
```

Here is a example of a command you have to use to trigger the TestModule after each waterfall download :

```
-s 2017-05-20T00:51:54 -e 2017-09-20T00:51:54 -n 25338 --waterfall-module TestModule,AnotherModule
```

Configuration file :
-------

The config.json file into the glouton folder provides to you the possibilities to configure a proxy if you need it and also to add the modules you want to run permanently.

Important note regarding satnogs db :
-------

At this time, the satnogs db team didn't push in production the change i made to add the start and end dates filters. So for now, to download data from satnogs db we have to use the page-from and page-to filters. When the changes will be pushed into production, i 'll remove those page filters and replace it by dates filters.

Docker :
-------
Glouton has a docker image that you can download [here on the docker hub](https://hub.docker.com/r/deckbsd/glouton-satnogs-data-downloader/).

All ideas or contributions are welcome. Feel free to use the [issues](https://github.com/deckbsd/glouton-satnogs-data-downloader/issues) tab :-)

License :
-------
[![license](https://img.shields.io/github/license/deckbsd/glouton-satnogs-data-downloader)](LICENSE)