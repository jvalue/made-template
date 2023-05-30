    CREATE TABLE IF NOT EXISTS stations (
    EVA_NR int,
    DS100 text,
    IFOPT text,
    NAME text,
    Verkehr text,
    Laenge text,
    Breite text,
    Betreiber_Name text,
    Betreiber_Nr int,
    Status text,
    PRIMARY KEY (EVA_NR)
);
    
CREATE TABLE IF NOT EXISTS train_plan (
    EVA_NR int,
    stop_id text,
    trip_type text,
    train_type text,
    train_number text,
    train_line text,
    platform text,
    next_stations text,
    passed_stations text,
    arrival text,
    departure text,
    FOREIGN KEY (EVA_NR) REFERENCES stations(EVA_NR)
);
   
CREATE TABLE IF NOT EXISTS plan_change(
        EVA_NR int,
        stop_id text,
        next_stations text,
        passed_stations text,
        arrival text,
        departure text,
        platform text,
        FOREIGN KEY (EVA_NR) REFERENCES stations(EVA_NR),
        FOREIGN KEY (stop_id) REFERENCES train_plan(stop_id),
        PRIMARY KEY (EVA_NR, stop_id)
);
