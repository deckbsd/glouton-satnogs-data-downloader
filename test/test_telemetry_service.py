from glouton.services.telemetry.telemetryService import TelemetryService
from glouton.repositories.frame.frameRepo import FrameRepo
from glouton.domain.parameters.programCmd import ProgramCmd


def test_loading_all_repository_types():
    params = ProgramCmd(None, None, None, None, None,
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

    service = TelemetryService(params)
    repos = service.filter_repositories()
    assert len(repos) == 1
    assert isinstance(repos[0], FrameRepo)
