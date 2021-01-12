from config import *
import subprocess
from random import random
from random import choice
import os
import lorem
from datetime import datetime, timedelta


def clear_file(file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("")


def file_name_by_table(table_name):
    file_name = f"insert_{table_name}.sql"
    path = os.path.abspath(os.path.join(RESULTS_DIR, file_name))
    return path


def clear_file_by_table(table_name):
    clear_file(file_name_by_table(table_name))


def append_to_file(file_name, text):
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(text)


def append_to_table_file(table_name, text):
    append_to_file( file_name_by_table(table_name), text )


def to_sql_str(value):
    value = value.replace("\n", "")
    return f"'{value}'"


def cast_to_type(value, t=None):
    if not t:
        return value

    try:
        t, t_t = t.split(':', 2)
    except:
        t_t = ''

    if t == 'str':
        return to_sql_str(value)
    if t == 'array':
        return [cast_to_type(v, t_t) for v in value]
    return value


def prepare_values_types(values, types=None):
    values = [str(v) for v in values]
    if types:
        for i in range(len(types)):
            values[i] = cast_to_type(values[i], types[i])

    return values


def insert_into_table(table_name, fields, values, types=None):
    values = prepare_values_types(values, types)
    command = f'INSERT INTO {table_name} ({", ".join(fields)}) VALUES ({", ".join(values)});\n'
    append_to_table_file(table_name, command)


def insert_using_func(func_name, table_name, values, types=None):
    # print(f'func: {func_name} table_name: {table_name} values: {values}')
    values = prepare_values_types(values, types)
    command = f"SELECT * FROM {func_name}({', '.join(values)});\n"
    append_to_table_file(table_name, command)


def count_lines(file_name):
    with open(file_name) as f:
        return len([_ for _ in f])


def generate_random_date(start_date, interval_days):
    return (datetime.strptime(start_date, '%Y-%m-%d') + timedelta(days=int(random() * interval_days))).strftime('%Y-%m-%d')


def random_interval_seconds(min_val, max_val):
    return timedelta(seconds=min_val + int(random() * (max_val - min_val))).total_seconds()


class FileRowRandomizer:
    def __init__(self, file_name):
        self.file_name = file_name
        with open(file_name) as f:
            self.lines_amount = count_lines(file_name)

    def get_random_line(self):
        with open(self.file_name) as f:
            line_n = int(random() * self.lines_amount)
            a = ""
            for i in range(line_n):
                a = f.readline()
            return a


names_randomizer = FileRowRandomizer(FILE_NAMES)
amine_names_randomizer = FileRowRandomizer(FILE_ANIME_NAMES)
surnames_randomizer = FileRowRandomizer(FILE_SURNAMES)
cities_randomizer = FileRowRandomizer(FILE_CITIES)
abilities_randomizer = FileRowRandomizer(FILE_ABILITIES)

boolean_randomizer = lambda: choice([True, False])
amount_randomizer = lambda amount: lambda: choice(range(1, amount + 1))

VALUES_GENERATORS = {
    'name': names_randomizer.get_random_line,
    'surname': surnames_randomizer.get_random_line,
    'gender': lambda: choice(GENDERS),
    'age': lambda: choice(RANGE_AGE),
    'city': cities_randomizer.get_random_line,
    'producer_role': lambda: choice(PRODUCER_ROLES),
    'films_number': lambda: choice(RANGE_FILMS_NUMBER),
    'genres': lambda: [ choice(GENRES) for _ in range(choice(RAGE_GENRES_AMOUNT)) ],
    'recording_actor_position': lambda: choice(RECORDING_ACTOR_POSITIONS),
    'editor_position': lambda: choice(EDITOR_POSITIONS),
    'artist_type': lambda: choice(ARTIST_TYPES),
    'using_technology': lambda: choice(USING_TECHNOLOGIES),

    'duration': lambda: choice(range(MIN_DURATION_S, MAX_DURATION_S, 60)),
    'estimation_time': lambda: choice(range(MIN_DURATION_S, MAX_DURATION_S, 60)),
    'process_status': lambda: choice(PROCESS_STATUS),
    'description': lambda: lorem.sentence(),
    'insertion_location': lambda: choice(INSERTION_LOCATIONS),
    'sound_type': lambda: choice(SOUND_TYPES),
    'digitization_type': lambda: choice(DIGITIZATION_TYPES),
    'revision_type': lambda: choice(REVISION_TYPES),
    'coloring_type': lambda: choice(COLORING_TYPES),
    'voice_acting_type': lambda: choice(VOICE_ACTING_TYPES),
    'artifact_type': lambda: choice(ARTIFACT_TYPES),
    'effect_level': lambda: choice(EFFECT_LEVELS),
    'animation_technology': lambda: choice(ANIMATION_TECHNOLOGIES),

    'frame_number': lambda: choice(range(MAX_FRAME_NUMBERS)),
    'sketches_number': lambda: choice(range(MAX_SKETCH_NUMBERS)),
    'frame_rate': lambda: choice(range(MIN_FRAME_RATE, MAX_FRAME_RATE)),

    'plot_type': lambda: choice(PLOT_TYPES),
    'location_type': lambda: choice(LOCATION_TYPES),

    'plot_process': lambda: choice(range(1, PLOT_PROCESSES_AMOUNT + 1)),
    'plot_name': lambda: f'{amine_names_randomizer.get_random_line()} {choice(PLOT_TYPES)}',
    'plot_pages_number': lambda: choice(range(MIN_PLOT_PAGES_NUMBER, MAX_PLOT_PAGES_NUMBER)),
    'narrative_period': lambda: random_interval_seconds(MIN_NARRATIVE_PERIOD, MAX_NARRATIVE_PERIOD),

    'importance_level': lambda: int(random() * 50),
    'event_name': lambda: f'{amine_names_randomizer.get_random_line()} {choice(EVENT_TYPES)}',

    'location_description_id':lambda: choice(range(1, LOCATION_DESCRIPTION_PROCESSES_AMOUNT + 1)),
    'location_drawing_id':lambda: choice(range(1, LOCATION_DRAWING_PROCESSES_AMOUNT + 1)),
    'area':lambda: choice(range(1, 50)),

    'battle_description_id':lambda: choice(range(1, BATTLE_DESCRIPTION_PROCESSES_AMOUNT + 1)),
    'battle_drawing_id':lambda: choice(range(1, BATTLE_DRAWING_PROCESSES_AMOUNT + 1)),
    'for_battle': boolean_randomizer,
    'battle_name': lambda: f'{amine_names_randomizer.get_random_line()} vs {amine_names_randomizer.get_random_line()}',
    'complexity_level': lambda: choice(range(10)),

    'ability_description_id':lambda: choice(range(1, ABILITY_DESCRIPTION_PROCESSES_AMOUNT + 1)),
    'ability_name': lambda: abilities_randomizer.get_random_line()[:32],
    'ability_type': lambda: choice(ABILITY_TYPES),

    'character_name': amine_names_randomizer.get_random_line,
    'positive': boolean_randomizer,
    'protagonist': boolean_randomizer,

    'voice_acting_id': amount_randomizer(VOICE_ACTING_PROCESSES_AMOUNT),
    'character_selection_id': amount_randomizer(CHARACTER_SELECT_PROCESSES_AMOUNT),
    'character_drawing_id': amount_randomizer(CHARACTER_DRAWING_PROCESSES_AMOUNT),
    'character_description_id': amount_randomizer(CHARACTER_DRAWING_PROCESSES_AMOUNT),

}

VALUES_CAST = {
    'name': 'str',
    'surname': 'str',
    'gender': 'str',
    'city': 'str',
    'producer_role': 'str',
    'genres': 'array:str',
    'recording_actor_position': 'str',
    'editor_position': 'str',
    'artist_type': 'str',
    'using_technology': 'str',

    'start_date': 'str',
    'deadline_date': 'str',
    'estimation_time': 'str',
    'process_status': 'str',
    'description': 'str',
    'insertion_location': 'str',
    'sound_type': 'str',
    'digitization_type': 'str',
    'revision_type': 'str',
    'coloring_type': 'str',
    'voice_acting_type': 'str',
    'artifact_type': 'str',
    'animation_technology': 'str',

    'effect_level': 'str',
    'plot_type': 'str',
    'location_type': 'str',
    'ability_type': 'str',
    'narrative_period': 'str',

    'battle_name': 'str',
    'event_name': 'str',
    'ability_name': 'str',
    'character_name': 'str',
}

def get_value_type(value_type):
    if value_type in VALUES_CAST:
        return VALUES_CAST[value_type]
    return None


def generate_random_values(values_types, values_generators=None):
    if values_generators is None:
        values_generators = {}

    # print(f'types: {values_types}')

    values = [
        values_generators[value_type]() if value_type in values_generators else VALUES_GENERATORS[value_type]()
        for value_type in values_types
    ]

    values = prepare_values_types(
        values,
        [ get_value_type(value_type)for value_type in values_types ]
    )

    return values


