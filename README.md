[![Known Vulnerabilities](https://snyk.io/test/github/deckbsd/glouton-satnogs-data-downloader/badge.svg)](https://snyk.io/test/github/deckbsd/glouton-satnogs-data-downloader)
# glouton-satnogs-data-downloader
The console app is a downloader for the data provided by the satnogs network.

command example : 
```
python ./glouton.py -s 2018-01-20T00:51:54 -e 2018-01-21T00:51:54 -n 28654
```
command example if you just want the payload files :
```
python ./glouton.py -s 2018-01-20T00:51:54 -e 2018-01-21T00:51:54 -n 28654 --payload
```

Actual features :
-------
    * waterfall downloading
    * payload downloading
    * filters :
        * norad id
        * start date
        * end date
        * stations
        * observation status
    * working directory selection
    * Docker container
    * modules

Future :
-------
    * automatic mode for downloading automatically the new observations of one or more satellites.

Modules :
-------
You can now create your own modules. These will be executed after each download from the category you selected. 

The module that you develop must herite from ModuleBase and must implement the "runAfterDownload" method. This method receive the file name and the full path as parameters.

Also the module and the name of the python file must be the same. The py file must be placed into the "modules" directory.

Here is a very simple exemple (this module is in the sources) :
```
from modules.moduleBase import ModuleBase

class TestModule(ModuleBase):

    def runAfterDownload(self, file_name, full_path, observation):
        print('executed after ' +  file_name)
```

Here is a exemple of a command you have to use to trigger the TestModule after each waterfall download :

```
-s 2017-05-20T00:51:54 -e 2017-09-20T00:51:54 -n 25338 --waterfallm TestModule,TestModule
```
Docker :
-------
Glouton has a docker image that you can download [here on the docker hub](https://hub.docker.com/r/deckbsd/glouton-satnogs-data-downloader/).

All ideas or contributions are welcome. Feel free to use the [issues](https://github.com/deckbsd/glouton-satnogs-data-downloader/issues) tab :-)
