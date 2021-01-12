/*
*создание триггеров и триггерных функций
*/
CREATE OR REPLACE FUNCTION check_if_battle() RETURNS trigger AS
$body$
DECLARE 
    is_for_battle BOOLEAN;
BEGIN
    SELECT l.FOR_BATTLE INTO is_for_battle FROM locations AS l WHERE l.LOCATION_ID = NEW.LOCATION_ID;
    IF is_for_battle IS TRUE THEN
        INSERT INTO trigger_info(TG_OP, TG_RELNAME, TG_NAME, CREATION_TIME) VALUES(TG_OP, TG_RELNAME, TG_NAME, NOW());
        RETURN NEW;
    ELSE
        RETURN NULL;
    END IF;
END
$body$ LANGUAGE plpgsql VOLATILE;
CREATE TRIGGER is_battle_location BEFORE INSERT OR UPDATE ON battle_location FOR EACH ROW EXECUTE PROCEDURE check_if_battle();

CREATE OR REPLACE FUNCTION check_if_character_artist() RETURNS trigger AS
$body$
DECLARE
    artist_type ARTIST_TYPES;
BEGIN
    SELECT a.ARTIST_TYPE INTO artist_type FROM artists AS a WHERE a.WORKER_ID = NEW.WORKER_ID;
    IF artist_type = 'character artist' THEN
        INSERT INTO trigger_info(TG_OP, TG_RELNAME, TG_NAME, CREATION_TIME) VALUES(TG_OP, TG_RELNAME, TG_NAME, NOW());
        RETURN NEW;
    ELSE
        RETURN NULL;
    END IF;
END
$body$ LANGUAGE plpgsql VOLATILE;
CREATE TRIGGER is_character_artist BEFORE INSERT OR UPDATE ON artist_character_drawing_process FOR EACH ROW EXECUTE PROCEDURE check_if_character_artist();

CREATE OR REPLACE FUNCTION check_if_battle_artist() RETURNS trigger AS
$body$
DECLARE
    artist_type ARTIST_TYPES;
BEGIN
    SELECT a.ARTIST_TYPE INTO artist_type FROM artists AS a WHERE a.WORKER_ID = NEW.WORKER_ID;
    IF artist_type = 'battle artist' THEN
        INSERT INTO trigger_info(TG_OP, TG_RELNAME, TG_NAME, CREATION_TIME) VALUES(TG_OP, TG_RELNAME, TG_NAME, NOW());
        RETURN NEW;
    ELSE
        RETURN NULL;
    END IF;
END
$body$ LANGUAGE plpgsql VOLATILE;
CREATE TRIGGER is_battle_artist BEFORE INSERT OR UPDATE ON artist_battle_drawing_process FOR EACH ROW EXECUTE PROCEDURE check_if_battle_artist();

CREATE OR REPLACE FUNCTION check_if_location_artist() RETURNS trigger AS
$body$
DECLARE
    artist_type ARTIST_TYPES;
BEGIN
    SELECT a.ARTIST_TYPE INTO artist_type FROM artists AS a WHERE a.WORKER_ID = NEW.WORKER_ID;
    IF artist_type = 'location artist' THEN
        INSERT INTO trigger_info(TG_OP, TG_RELNAME, TG_NAME, CREATION_TIME) VALUES(TG_OP, TG_RELNAME, TG_NAME, NOW());
        RETURN NEW;
    ELSE
        RETURN NULL;
    END IF;
END
$body$ LANGUAGE plpgsql VOLATILE;
CREATE TRIGGER is_location_artist BEFORE INSERT OR UPDATE ON artist_location_drawing_process FOR EACH ROW EXECUTE PROCEDURE check_if_location_artist();

CREATE OR REPLACE FUNCTION check_if_effect_artist() RETURNS trigger AS
$body$
DECLARE
    artist_type ARTIST_TYPES;
BEGIN
    SELECT a.ARTIST_TYPE INTO artist_type FROM artists AS a WHERE a.WORKER_ID = NEW.WORKER_ID;
    IF artist_type = 'effect artist' THEN
        INSERT INTO trigger_info(TG_OP, TG_RELNAME, TG_NAME, CREATION_TIME) VALUES(TG_OP, TG_RELNAME, TG_NAME, NOW());
        RETURN NEW;
    ELSE
        RETURN NULL;
    END IF;
END
$body$ LANGUAGE plpgsql VOLATILE;
CREATE TRIGGER is_effect_artist BEFORE INSERT OR UPDATE ON artist_effects_process FOR EACH ROW EXECUTE PROCEDURE check_if_effect_artist();

CREATE OR REPLACE FUNCTION check_if_animation_artist() RETURNS trigger AS
$body$
DECLARE
    artist_type ARTIST_TYPES;
BEGIN
    SELECT a.ARTIST_TYPE INTO artist_type FROM artists AS a WHERE a.WORKER_ID = NEW.WORKER_ID;
    IF artist_type = 'animation artist' THEN
        INSERT INTO trigger_info(TG_OP, TG_RELNAME, TG_NAME, CREATION_TIME) VALUES(TG_OP, TG_RELNAME, TG_NAME, NOW());
        RETURN NEW;
    ELSE
        RETURN NULL;
    END IF;
END
$body$ LANGUAGE plpgsql VOLATILE;
CREATE TRIGGER is_animation_artist BEFORE INSERT OR UPDATE ON artist_animation_process FOR EACH ROW EXECUTE PROCEDURE check_if_animation_artist();

CREATE OR REPLACE FUNCTION check_if_coloring_artist() RETURNS trigger AS
$body$
DECLARE
    artist_type ARTIST_TYPES;
BEGIN
    SELECT a.ARTIST_TYPE INTO artist_type FROM artists AS a WHERE a.WORKER_ID = NEW.WORKER_ID;
    IF artist_type = 'coloring artist' THEN
        INSERT INTO trigger_info(TG_OP, TG_RELNAME, TG_NAME, CREATION_TIME) VALUES(TG_OP, TG_RELNAME, TG_NAME, NOW());
        RETURN NEW;
    ELSE
        RETURN NULL;
    END IF;
END
$body$ LANGUAGE plpgsql VOLATILE;
CREATE TRIGGER is_coloring_artist BEFORE INSERT OR UPDATE ON artist_coloring_process FOR EACH ROW EXECUTE PROCEDURE check_if_coloring_artist();