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
or if you want to use it as a package:
```
pip install glouton
```

Here is an example of how to use the glouton Pypi package :
```
    from glouton.domain.parameters.programCmd import ProgramCmd
    from glouton.services.observation.observationsService import \
    ObservationsService

    glouton_conf = ProgramCmd(norad_id=norad_id,
                              ground_station_id=None,
                              start_date=start_date,
                              end_date=end_date,
                              observation_status=None,
                              working_dir="/tmp",
                              payloads=False,
                              waterfalls=False,
                              demoddata=True,
                              payload_modules=None,
                              demoddata_modules=["CSV"],
                              waterfall_modules=None,
                              user=None,
                              transmitter_uuid=None,
                              transmitter_mode=None,
                              transmitter_type=None,
                              frame_modules=None,
                              observer=None,
                              app_source=None,
                              transmitter=None,
                              page_from=None,
                              page_to=None)

    try:
        obs = ObservationsService(glouton_conf)
        obs.extract()
    except Exception as eee:
        LOGGER.error("data collection: %s", eee)
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

simple command example for downloading frames for the satellite with the norad id 43466 from the page 1 to 100 and apply the process within the SomeModule module (You have to provide a module when you download the frames): 
```
python ./bin/glouton --db -n 43466 --page-from 1 --page-to 100 --frame-module SomeModule
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
            * start date
            * end date
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

Docker :
-------
Glouton has a docker image that you can download [here on the docker hub](https://hub.docker.com/r/deckbsd/glouton-satnogs-data-downloader/).

All ideas or contributions are welcome. Feel free to use the [issues](https://github.com/deckbsd/glouton-satnogs-data-downloader/issues) tab :-)

License :
-------
[![license](https://img.shields.io/github/license/deckbsd/glouton-satnogs-data-downloader)](LICENSE)