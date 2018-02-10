class ProgramCmd:
    def __init__(self, norad_id, ground_station_id, start_date, end_date, working_dir):
        self.norad_id = norad_id
        self.ground_station_id = ground_station_id
        self.start_date = start_date
        self.end_date = end_date
        self.working_dir = working_dir