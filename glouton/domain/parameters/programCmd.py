class ProgramCmd:
    def __init__(self,
                 norad_id,
                 ground_station_id,
                 start_date,
                 end_date,
                 observation_status,
                 working_dir,
                 archives,
                 waterfalls,
                 demoddata,
                 archive_modules,
                 demoddata_modules,
                 waterfall_modules,
                 user,
                 transmitter_uuid,
                 transmitter_mode,
                 transmitter_type,
                 frame_modules,
                 observer,
                 app_source,
                 transmitter):
        self.norad_id = norad_id
        self.ground_station_id = ground_station_id
        self.start_date = start_date
        self.end_date = end_date
        self.working_dir = working_dir
        self.archives = archives
        self.waterfalls = waterfalls
        self.demoddata = demoddata
        self.archive_modules = archive_modules
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
