class ProgramCmd:
    def __init__(self,
    norad_id,
    ground_station_id,
    start_date,
    end_date,
    observation_status,
    working_dir,
    payloads,
    waterfalls,
    demoddata,
    payload_modules,
    demoddata_modules,
    waterfall_modules,
    user,
    transmitter_uuid,
    transmitter_mode,
    transmitter_type,
    frame_modules,
    observer,
    app_source,
    transmitter,
    page_from,
    page_to):
        self.norad_id = norad_id
        self.ground_station_id = ground_station_id
        self.start_date = start_date
        self.end_date = end_date
        self.working_dir = working_dir
        self.payloads = payloads
        self.waterfalls = waterfalls
        self.demoddata = demoddata
        self.payload_modules = payload_modules
        self.demoddata_modules = demoddata_modules
        self.waterfall_modules = waterfall_modules
        self.observation_status = observation_status
        self.user = user
        self.transmitter_uuid = transmitter_uuid
        self.transmitter_mode = transmitter_mode
        self.transmitter_type = transmitter_type
        self.frame_modules = frame_modules
        self.observer = observer
        self.app_source = app_source
        self.transmitter = transmitter
        self.page_from = page_from
        self.page_to = page_to