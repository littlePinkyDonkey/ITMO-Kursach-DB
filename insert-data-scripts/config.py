DB_NAME="kursach"
DB_USER="postgres"
DB_PASSWORD=""
DB_PORT=5433
RESULTS_DIR="result_sql_scripts"

TABLE_WORKERS="workers"
TABLE_STORYBOARD_ARTISTS="storyboard_artists"
TABLE_PRODUCERS="producers"
TABLE_AUDIO_SPECIALISTS="audio_specialist"
TABLE_DIGITILIZERS="digitizers"
TABLE_SMOOTHING_SPECIALIST="smoothing_specialist"
TABLE_ART_DIRECTOR="art_director"
TABLE_SCREENWRITERS="screenwriters"
TABLE_DIRECTORS="regisseurs"
TABLE_ROLES_DESIGNERS="roles_designers"
TABLE_RECORDING_ACTORS="recording_actors"
TABLE_EDITORS="editors"
TABLE_ARTISTS="artists"

FUNC_ADD_STORYBOARD_ARTIST="add_storyboard_artist"
FUNC_ADD_PRODUCER="add_producer"
FUNC_ADD_AUDIO_SPECIALIST="add_audio_specialist"
FUNC_ADD_DIGITILIZER="add_digitizer"
FUNC_ADD_SMOOTHING_SPECIALIST="add_smoothing_specialist"
FUNC_ADD_ART_DIRECTOR="add_art_director"
FUNC_ADD_SCREENWRITER="add_screenwriter"
FUNC_ADD_DIRECTOR="add_regisseur"
FUNC_ADD_ROLES_DESIGNER="add_roles_designer"
FUNC_ADD_RECORDING_ACTOR="add_recording_actor"
FUNC_ADD_EDITOR="add_editor"
FUNC_ADD_ARTIST="add_artist"

STORYBOARD_ARTIST_AMOUNT=10
PRODUCER_AMOUNT=15
AUDIO_SPECIALIST_AMOUNT=20
DIGITILIZER_AMOUNT=50
SMOOTHING_SPECIALIST_AMOUNT=14
ART_DIRECTOR_AMOUNT=3
SCREENWRITER_AMOUNT=12
DIRECTOR_AMOUNT=3
ROLES_DESIGNER_AMOUNT=42
RECORDING_ACTOR_AMOUNT=90
EDITOR_AMOUNT=22
ARTIST_AMOUNT=34

TABLE_PROCESSES="processes"
TABLE_STORYBOARD_PROCESSES="storyboard_process"
TABLE_ADVERTISING_PROCESSES="adevertising_process"
TABLE_ADDING_SOUND_PROCESSES="adding_sound_process"
TABLE_DIGITILIZATION_PROCESSES="digitization_process"
TABLE_SMOOTHING_PROCESSES="smoothing_process"
TABLE_REVISION_PROCESSES="revisions_process"
TABLE_COLORING_PROCESSES="coloring_process"
TABLE_ANIMATION_PROCESSES="animation_process"
TABLE_ADDING_EFFECT_PROCESSES="adding_effect_process"
TABLE_LOCATION_DRAWING_PROCESSES="location_drawing_process"
TABLE_BATTLE_DRAWING_PROCESSES="battle_drawing_process"
TABLE_CHARACTER_DRAWING_PROCESSES="character_drawing_process"
TABLE_CHARACTER_SELECT_PROCESSES="character_select_process"
TABLE_VOICE_ACTING_PROCESSES="voice_acting_process"

FUNC_ADD_STORYBOARD_PROCESSES="create_storyboard_process"
FUNC_ADD_ADVERTISING_PROCESSES="create_advertising_process"
FUNC_ADD_ADDING_SOUND_PROCESSES="create_adding_sound_effect_process"
FUNC_ADD_DIGITILIZATION_PROCESSES="create_digitization_process"
FUNC_ADD_SMOOTHING_PROCESSES="create_smoothing_process"
FUNC_ADD_REVISION_PROCESSES="create_revision_process"
FUNC_ADD_COLORING_PROCESSES="create_coloring_process"
FUNC_ADD_ANIMATION_PROCESSES="create_animation_process"
FUNC_ADD_ADDING_EFFECT_PROCESSES="create_adding_effect_process"
FUNC_ADD_LOCATION_DRAWING_PROCESSES="create_location_drawing_process"
FUNC_ADD_BATTLE_DRAWING_PROCESSES="create_battle_drawing_process"
FUNC_ADD_CHARACTER_DRAWING_PROCESSES="create_character_drawing_process"
FUNC_ADD_CHARACTER_SELECT_PROCESSES="create_character_select_process"
FUNC_ADD_VOICE_ACTING_PROCESSES="create_voice_acting_process"

STORYBOARD_PROCESSES_AMOUNT = 400
ADVERTISING_PROCESSES_AMOUNT = 400
ADDING_SOUND_PROCESSES_AMOUNT = 400
DIGITILIZATION_PROCESSES_AMOUNT = 400
SMOOTHING_PROCESSES_AMOUNT = 400
REVISION_PROCESSES_AMOUNT = 400
COLORING_PROCESSES_AMOUNT = 400
ANIMATION_PROCESSES_AMOUNT = 400
ADDING_EFFECT_PROCESSES_AMOUNT = 400
LOCATION_DRAWING_PROCESSES_AMOUNT = 400
BATTLE_DRAWING_PROCESSES_AMOUNT = 400
CHARACTER_DRAWING_PROCESSES_AMOUNT = 400
CHARACTER_SELECT_PROCESSES_AMOUNT = 400
VOICE_ACTING_PROCESSES_AMOUNT = 400

TABLE_ABILITY_DESCRIPTION_PROCESSES="ability_description_process"
TABLE_CHARACTER_DESCRIPTION_PROCESSES="character_description_process"
TABLE_LOCATION_DESCRIPTION_PROCESSES="location_description_process"
TABLE_BATTLE_DESCRIPTION_PROCESSES="battle_description_process"
TABLE_PLOT_PROCESSES="plot_process"

FUNC_ADD_ABILITY_DESCRIPTION_PROCESSES="create_ability_description_process"
FUNC_ADD_CHARACTER_DESCRIPTION_PROCESSES="create_character_description_process"
FUNC_ADD_LOCATION_DESCRIPTION_PROCESSES="create_location_description_process"
FUNC_ADD_BATTLE_DESCRIPTION_PROCESSES="create_battle_description_process"
FUNC_ADD_PLOT_PROCESSES="create_plot_process"

ABILITY_DESCRIPTION_PROCESSES_AMOUNT = 200
CHARACTER_DESCRIPTION_PROCESSES_AMOUNT = 200
LOCATION_DESCRIPTION_PROCESSES_AMOUNT = 200
BATTLE_DESCRIPTION_PROCESSES_AMOUNT = 200
PLOT_PROCESSES_AMOUNT = 200

TABLE_ARTIFACTS="artifacts"
TABLE_PLOT="plot"
TABLE_EVENTS="events"
TABLE_LOCATIONS="locations"
TABLE_BATTLE="battle"
TABLE_ABILITIES="abilities"

ARTIFACTS_AMOUNT = 200
PLOT_AMOUNT = 10
EVENTS_AMOUNT = 200
LOCATIONS_AMOUNT = 200
BATTLE_AMOUNT = 20000
ABILITIES_AMOUNT = 200

TABLE_REVISION_STORYBOARDING="revision_storyboarding"
TABLE_REVISION_ADDING_SOUND="revision_adding_sound"
TABLE_REVISION_SMOOTHING="revision_smoothing"
TABLE_REVISION_ADDING_EFFECTS="revision_adding_effects"
TABLE_REVISION_ANIMATION="revision_animation"
TABLE_REVISION_COLORING="revision_coloring"

TABLE_ARTIST_STORYBOARD_PROCESS="artist_storyboard_process"
TABLE_PRODUCER_ADVERTISING_PROCESS="producer_advertising_process"
TABLE_AUDIO_ADDING_PROCESS="audio_adding_process"

TABLE_DIGITILIZERS_DIGITILIZATION_PROCESS="digitizers_digitization_process"
TABLE_SMOOTHER_SMOOTHING_PROCESS="smoother_smoothing_process"
TABLE_ART_DIRECTOR_REVISION_PROCESS="art_director_revision_process"
TABLE_ARTIST_COLORING_PROCESS="artist_coloring_process"
TABLE_ARTIST_ANIMATION_PROCESS="artist_animation_process"
TABLE_ARTIST_EFFECTS_PROCESS="artist_effects_process"

TABLE_ARTIST_LOCATION_DRAWING_PROCESS="artist_location_drawing_process"
TABLE_ARTIST_BATTLE_DRAWING_PROCESS="artist_battle_drawing_process"
TABLE_ARTIST_CHARACTER_DRAWING_PROCESS="artist_character_drawing_process"
TABLE_EDITORS_CHARACTER_PROCESS="editors_character_process"
TABLE_RECORDER_VOICE_ACTING_PROCESS="recorder_voice_acting_process"

TABLE_DESIGNER_ABILITY_PROCESS="designer_ability_process"
TABLE_DESIGNER_CHARACTER_PROCESS="designer_character_process"
TABLE_DIRECTOR_LOCATION_PROCESS="regisseur_location_process"
TABLE_SCREENWRITER_BATTLE_PROCESS="screenwriter_battle_process"
TABLE_DIRECTOR_PLOT_PROCESS="regisseurs_plot_process"
TABLE_SCREENWRITER_PLOT_PROCESS="screenwriter_plot_process"

TABLE_PROCESS_ARTIFACT="process_artifact"
TABLE_EVENTS_PLOTS="events_plots"
TABLE_EVENT_LOCATION="event_location"
TABLE_EVENT_CHARACTERS="events_characters"
TABLE_BATTLE_LOCATION="battle_location"
TABLE_BATTLE_ABILITIES="battle_abilities"
TABLE_BATTLE_CHARACTERS="battle_characters"
TABLE_CHARACTERS_ABILITIES="characters_abilities"

FILE_NAMES="japan_names.csv"
FILE_ANIME_NAMES="anime_names.csv"
FILE_SURNAMES="japan_names.csv"
FILE_CITIES="japan_names.csv"
FILE_ABILITIES="anime_abilities.csv"

PRODUCER_ROLES =  ('producer', 'executive producer', 'co-producer', 'associate producer',
 'assistant producer', 'line producer', 'administrative producer', 'creative producer', 'information producer')
RECORDING_ACTOR_POSITIONS =  ('dubbing', 'voice acting roles', 'music recording')
EDITOR_POSITIONS =  ('literature editor', 'technical editor' , 'art editor', 'main editor')
ARTIST_TYPES =  ('character artist', 'battle artist', 'location artist', 'background artist', 'effect artist',
 'animation artist', 'coloring artist')
PROCESS_STATUS =  ('started', 'in process', 'revision', 'finished')
INSERTION_LOCATIONS =  ('the beginning', 'the middle', 'the end')
SOUND_TYPES =  ('music', 'noises')
DIGITIZATION_TYPES =  ('adding contrast, then scanning', 'scanning, then adding contrast')
REVISION_TYPES =  ('full revision', 'part revision')
COLORING_TYPES =  ('colored', 'black-white')
VOICE_ACTING_TYPES =  ('preliminary', 'follow-up')
PLOT_TYPES =  ('main', 'additional', 'spin-off')
EVENT_TYPES =  ('Up', 'Uprising', 'failed', 'respected', 'bited', 'beated', 'win', 'break', 'walk', 'attack')
LOCATION_TYPES =  ('field', 'forest', 'city', 'village', 'jungle', 'lake', 'mounatains', 'desert', 'cave', 'waterfall', 'castle')
ABILITY_TYPES =  ('attack', 'defence', 'heal', 'chatting')
USING_TECHNOLOGIES =  ('drawings', 'dolls', '3D')
ARTIFACT_TYPES =  ('image', 'video', 'text', 'music', 'sounds')
EFFECT_LEVELS = ('AAA', 'AA', 'A', 'BBB', 'BB', 'B', 'CCC', 'CC', 'C')
RECORDING_ACTORS_POSITIONS = ('main', 'second_role')
ANIMATION_TECHNOLOGIES = ('3D', '3DCG', '2D', 'CGI', '2D+3D')

GENDERS = ('male', 'female')

MIN_AGE = 20
MAX_AGE = 56
RANGE_AGE = tuple(range(MIN_AGE, MAX_AGE))

MIN_FILMS_NUMBER = 0
MAX_FILMS_NUMBER = 20
RANGE_FILMS_NUMBER = tuple(range(MIN_FILMS_NUMBER, MAX_FILMS_NUMBER))

GENRES = ('Action', 'Comedy', 'Slice-of-Life', 'Drama', 'Tragedy', 'Psychological', 'History', 'Mecha', 'Military', 
    'Supernatural', 'Magic', 'Romance', 'Shonen', 'Shoujo', 'Seinen', 'Josei', 'Ecchi', 'Harem', 'Isekai', 'Kodomomuke',
    'Iyashikei')
MIN_GENRES_AMOUNT = 1
MAX_GENRES_AMOUNT = 10
RAGE_GENRES_AMOUNT = tuple(range(MIN_GENRES_AMOUNT, MAX_GENRES_AMOUNT))

MAX_FRAME_NUMBERS=3_000_000
MAX_SKETCH_NUMBERS=5_000_000

HALF_HOUR_S = 30 * 60
WEEK_S = 7 * 24 * 60 * 60
MIN_DURATION_S = HALF_HOUR_S
MAX_DURATION_S = WEEK_S
RANGE_DURATION_S = MAX_DURATION_S - MIN_DURATION_S

MIN_FRAME_RATE=15
MAX_FRAME_RATE=60

MIN_PLOT_PAGES_NUMBER=50
MAX_PLOT_PAGES_NUMBER=1000

MIN_NARRATIVE_PERIOD = 3600
MAX_NARRATIVE_PERIOD = 3600*24

