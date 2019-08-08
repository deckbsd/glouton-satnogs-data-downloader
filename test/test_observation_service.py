from glouton.services.observation.observationsService import ObservationsService
from glouton.repositories.payload.payloadRepo import PayloadRepo
from glouton.repositories.waterfall.waterfallRepo import WaterfallRepo
from glouton.repositories.demoddata.demoddataRepo import DemoddataRepo
from glouton.domain.parameters.programCmd import ProgramCmd

def test_loading_all_repository_types():
    params = ProgramCmd(None, None, None, None, None,
    None,
    True,
    True,
    True,
    None,
    None,
    None,
    None,
    None,
    None,
    None)

    service = ObservationsService(params)
    repos = service.filter_repositories()
    assert len(repos) == 3
    assert isinstance(repos[0], PayloadRepo)
    assert isinstance(repos[1], WaterfallRepo)
    assert isinstance(repos[2], DemoddataRepo)

def test_loading_only_payload_repository_types():
    params = ProgramCmd(None, None, None, None, None,
    None,
    True,
    False,
    False,
    None,
    None,
    None,
    None,
    None,
    None,
    None)
    
    service = ObservationsService(params)
    repos = service.filter_repositories()
    assert len(repos) == 1
    assert isinstance(repos[0], PayloadRepo)

def test_loading_only_waterfall_repository_types():
    params = ProgramCmd(None, None, None, None, None,
    None,
    False,
    True,
    False,
    None,
    None,
    None,
    None,
    None,
    None,
    None)
        
    service = ObservationsService(params)
    repos = service.filter_repositories()
    assert len(repos) == 1
    assert isinstance(repos[0], WaterfallRepo)

def test_loading_only_Demoddata_repository_types():
    params = ProgramCmd(None, None, None, None, None,
    None,
    False,
    False,
    True,
    None,
    None,
    None,
    None,
    None,
    None,
    None)
            
    service = ObservationsService(params)
    repos = service.filter_repositories()
    assert len(repos) == 1
    assert isinstance(repos[0], DemoddataRepo)


def test_loading_only_Payload_Demoddata_repository_types():
    params = ProgramCmd(None, None, None, None, None,
    None,
    True,
    False,
    True,
    None,
    None,
    None,
    None,
    None,
    None,
    None)
                
    service = ObservationsService(params)
    repos = service.filter_repositories()
    assert len(repos) == 2
    assert isinstance(repos[0], PayloadRepo)
    assert isinstance(repos[1], DemoddataRepo)


def test_loading_only_Waterfall_Demoddata_repository_types():
    params = ProgramCmd(None, None, None, None, None,
    None,
    False,
    True,
    True,
    None,
    None,
    None,
    None,
    None,
    None,
    None)
                    
    service = ObservationsService(params)
    repos = service.filter_repositories()
    assert len(repos) == 2
    assert isinstance(repos[0], WaterfallRepo)
    assert isinstance(repos[1], DemoddataRepo)

def test_default_loading_repository():
    params = ProgramCmd(None, None, None, None, None,
    None,
    False,
    False,
    False,
    None,
    None,
    None,
    None,
    None,
    None,
    None)
                        
    service = ObservationsService(params)
    repos = service.filter_repositories()
    assert len(repos) == 3
    assert isinstance(repos[0], PayloadRepo)
    assert isinstance(repos[1], WaterfallRepo)
    assert isinstance(repos[2], DemoddataRepo)