from glouton.services.observation.observationsService import ObservationsService
from glouton.repositories.archive.archiveRepo import ArchiveRepo
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
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        )

    service = ObservationsService(params)
    repos = service.filter_repositories()
    assert len(repos) == 3
    assert isinstance(repos[0], ArchiveRepo)
    assert isinstance(repos[1], WaterfallRepo)
    assert isinstance(repos[2], DemoddataRepo)


def test_loading_only_archive_repository_types():
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
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        )

    service = ObservationsService(params)
    repos = service.filter_repositories()
    assert len(repos) == 1
    assert isinstance(repos[0], ArchiveRepo)


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
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        )

    service = ObservationsService(params)
    repos = service.filter_repositories()
    assert len(repos) == 1
    assert isinstance(repos[0], WaterfallRepo)


def test_loading_only_demoddata_repository_types():
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
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        )

    service = ObservationsService(params)
    repos = service.filter_repositories()
    assert len(repos) == 1
    assert isinstance(repos[0], DemoddataRepo)


def test_loading_only_archive_demoddata_repository_types():
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
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        )

    service = ObservationsService(params)
    repos = service.filter_repositories()
    assert len(repos) == 2
    assert isinstance(repos[0], ArchiveRepo)
    assert isinstance(repos[1], DemoddataRepo)


def test_loading_only_waterfall_demoddata_repository_types():
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
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        )

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
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        )

    service = ObservationsService(params)
    repos = service.filter_repositories()
    assert len(repos) == 3
    assert isinstance(repos[0], ArchiveRepo)
    assert isinstance(repos[1], WaterfallRepo)
    assert isinstance(repos[2], DemoddataRepo)
