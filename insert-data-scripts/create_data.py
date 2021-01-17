import config
import create_helpers
from random import choice
import os


def repeat(func, times=1):
    for i in range(times):
        func()


def clear_file_and_add_amount(func, table_name, amount):
    create_helpers.clear_file_by_table(table_name)
    repeat(func, amount)


def add_stand_person_func(func_name, table_name, additional_fields=None):
    fields = ['name', 'surname', 'gender', 'age', 'city']
    if (additional_fields):
        fields = [*fields, *additional_fields]

    create_helpers.insert_using_func(
        func_name,
        table_name,
        create_helpers.generate_random_values(fields)
    )


def add_stand_process_func(func_name, table_name, additional_fields=None):
    start_date = create_helpers.generate_random_date('2007-01-01', 365*13)
    deadline_date = create_helpers.generate_random_date(start_date, 120)

    values_generators = {
        'deadline_date': lambda: deadline_date,
        'start_date': lambda: start_date
    }

    fields = ['duration', 'deadline_date', 'description', 'process_status', 'estimation_time', 'start_date']
    if (additional_fields):
        fields = [*fields, *additional_fields]

    create_helpers.insert_using_func(
        func_name,
        table_name,
        create_helpers.generate_random_values(fields, values_generators)
    )


add_storyboard_artist = lambda: add_stand_person_func( config.FUNC_ADD_STORYBOARD_ARTIST, config.TABLE_STORYBOARD_ARTISTS)
add_producer = lambda: add_stand_person_func( config.FUNC_ADD_PRODUCER, config.TABLE_PRODUCERS, ['producer_role'])
add_audio_specialist = lambda: add_stand_person_func( config.FUNC_ADD_AUDIO_SPECIALIST, config.TABLE_AUDIO_SPECIALISTS)
add_digitizer = lambda: add_stand_person_func( config.FUNC_ADD_DIGITILIZER, config.TABLE_DIGITILIZERS)
add_smoothing_specialist = lambda: add_stand_person_func( config.FUNC_ADD_SMOOTHING_SPECIALIST, config.TABLE_SMOOTHING_SPECIALIST)
add_art_director = lambda: add_stand_person_func( config.FUNC_ADD_ART_DIRECTOR, config.TABLE_ART_DIRECTOR)
add_screenwriter = lambda: add_stand_person_func( config.FUNC_ADD_SCREENWRITER, config.TABLE_SCREENWRITERS, ['films_number', 'genres'])
add_director = lambda: add_stand_person_func( config.FUNC_ADD_DIRECTOR, config.TABLE_DIRECTORS , ['films_number', 'genres'])
add_roles_designer = lambda: add_stand_person_func( config.FUNC_ADD_ROLES_DESIGNER, config.TABLE_ROLES_DESIGNERS)
add_recording_actor = lambda: add_stand_person_func( config.FUNC_ADD_RECORDING_ACTOR, config.TABLE_RECORDING_ACTORS , ['recording_actor_position'])
add_editor = lambda: add_stand_person_func( config.FUNC_ADD_EDITOR, config.TABLE_EDITORS , ['genres', 'editor_position'])
add_artist = lambda: add_stand_person_func( config.FUNC_ADD_ARTIST, config.TABLE_ARTISTS , ['artist_type', 'using_technology'])


add_storyboard_process = lambda: add_stand_process_func( config.FUNC_ADD_STORYBOARD_PROCESSES ,config.TABLE_STORYBOARD_PROCESSES, ['frame_number'])
add_adevertising_process = lambda: add_stand_process_func( config.FUNC_ADD_ADVERTISING_PROCESSES ,config.TABLE_ADVERTISING_PROCESSES, ['insertion_location'])
add_adding_sound_process = lambda: add_stand_process_func( config.FUNC_ADD_ADDING_SOUND_PROCESSES ,config.TABLE_ADDING_SOUND_PROCESSES, ['sound_type'])
add_digitization_process = lambda: add_stand_process_func( config.FUNC_ADD_DIGITILIZATION_PROCESSES ,config.TABLE_DIGITILIZATION_PROCESSES, ['sketches_number', 'digitization_type'])
add_smoothing_process = lambda: add_stand_process_func( config.FUNC_ADD_SMOOTHING_PROCESSES ,config.TABLE_SMOOTHING_PROCESSES)
add_revisions_process = lambda: add_stand_process_func( config.FUNC_ADD_REVISION_PROCESSES ,config.TABLE_REVISION_PROCESSES, ['revision_type'])
add_coloring_process = lambda: add_stand_process_func( config.FUNC_ADD_COLORING_PROCESSES ,config.TABLE_COLORING_PROCESSES, ['coloring_type'])
add_animation_process = lambda: add_stand_process_func( config.FUNC_ADD_ANIMATION_PROCESSES ,config.TABLE_ANIMATION_PROCESSES, ['frame_rate', 'animation_technology'])
add_adding_effect_process = lambda: add_stand_process_func( config.FUNC_ADD_ADDING_EFFECT_PROCESSES ,config.TABLE_ADDING_EFFECT_PROCESSES, ['effect_level'])
add_location_drawing_process = lambda: add_stand_process_func( config.FUNC_ADD_LOCATION_DRAWING_PROCESSES ,config.TABLE_LOCATION_DRAWING_PROCESSES)
add_battle_drawing_process = lambda: add_stand_process_func( config.FUNC_ADD_BATTLE_DRAWING_PROCESSES ,config.TABLE_BATTLE_DRAWING_PROCESSES)
add_character_drawing_process = lambda: add_stand_process_func( config.FUNC_ADD_CHARACTER_DRAWING_PROCESSES ,config.TABLE_CHARACTER_DRAWING_PROCESSES)
add_character_select_process = lambda: add_stand_process_func( config.FUNC_ADD_CHARACTER_SELECT_PROCESSES ,config.TABLE_CHARACTER_SELECT_PROCESSES)
add_voice_acting_process = lambda: add_stand_process_func( config.FUNC_ADD_VOICE_ACTING_PROCESSES ,config.TABLE_VOICE_ACTING_PROCESSES, ['voice_acting_type'])

add_ability_description_process = lambda: add_stand_process_func( config.FUNC_ADD_ABILITY_DESCRIPTION_PROCESSES ,config.TABLE_ABILITY_DESCRIPTION_PROCESSES)
add_character_description_process = lambda: add_stand_process_func( config.FUNC_ADD_CHARACTER_DESCRIPTION_PROCESSES ,config.TABLE_CHARACTER_DESCRIPTION_PROCESSES)
add_location_description_process = lambda: add_stand_process_func( config.FUNC_ADD_LOCATION_DESCRIPTION_PROCESSES ,config.TABLE_LOCATION_DESCRIPTION_PROCESSES)
add_battle_description_process = lambda: add_stand_process_func( config.FUNC_ADD_BATTLE_DESCRIPTION_PROCESSES ,config.TABLE_BATTLE_DESCRIPTION_PROCESSES)
add_plot_process = lambda: add_stand_process_func( config.FUNC_ADD_PLOT_PROCESSES ,config.TABLE_PLOT_PROCESSES)

def add_plot():
    create_helpers.insert_into_table(
        config.TABLE_PLOT,
        ['PLOT_PROCESS', 'PLOT_NAME', 'PAGES_NUMBER', 'PLOT_TYPE', 'DESCRIPTION', 'NARRATIVE_PERIOD'],
        create_helpers.generate_random_values(
            ['plot_process', 'plot_name', 'plot_pages_number', 'plot_type', 'description', 'narrative_period']
        )
    )


def add_event():
    create_helpers.insert_into_table(
        config.TABLE_EVENTS,
        ['EVENT_NAME', 'DESCRIPTION', 'IMPORTANCE_LEVEL'],
        create_helpers.generate_random_values(
            ['event_name', 'description', 'importance_level']
        )
    )


def add_location():
    create_helpers.insert_into_table(
        config.TABLE_LOCATIONS,
        ['DESCRIPTION_ID', 'DRAWING_ID', 'LOCATION_NAME', 'AREA', 'LOCATION_TYPE', 'FOR_BATTLE'],
        create_helpers.generate_random_values(
            ['location_description_id', 'location_drawing_id', 'city', 'area', 'location_type', 'importance_level']
        )
    )


def add_battle():
    create_helpers.insert_into_table(
        config.TABLE_BATTLE,
        ['DESCRIPTION_ID', 'DRAWING_ID', 'BATTLE_NAME', 'DURATION'],
        create_helpers.generate_random_values(
            ['battle_description_id', 'battle_drawing_id', 'battle_name', 'for_battle']
        )
    )


def add_abilities():
    create_helpers.insert_into_table(
        config.TABLE_ABILITIES,
        ['DESCRIPTION_ID', 'ABILITY_NAME', 'DESCRIPTION', 'ABILITY_TYPE', 'COMPLEXITY_LEVEL'],
        create_helpers.generate_random_values(
            ['ability_description_id', 'ability_name', 'description', 'ability_type', 'complexity_level']
        )
    )


def add_character():
    birth_date = create_helpers.generate_random_date('2007-01-01', 365*89)

    values_generators = {
        'birth_date': lambda: birth_date
    }

    create_helpers.insert_into_table(
        config.TABLE_ABILITIES,
        ['VOICE_ACTING_ID', 'SELECTION_ID', 'DRAWING_ID', 'DESCRIPTION_ID', 'CHARACTER_NAME', 'GENDER', 'PROTAGONIST', 'POSITIVE', 'AGE', 'BIRTH_DATE'],
        create_helpers.generate_random_values(
            ['voice_acting_id', 'character_selection_id', 'character_drawing_id', 'character_description_id', 'character_name', 'gender', 'protagonist', 'positive', ]
        ),
        values_generators
    )


def main():
    try:
        os.mkdir(config.RESULTS_DIR)
    except:
        pass

    clear_file_and_add_amount(add_storyboard_artist, config.TABLE_STORYBOARD_ARTISTS, config.STORYBOARD_ARTIST_AMOUNT)
    clear_file_and_add_amount(add_producer, config.TABLE_PRODUCERS, config.PRODUCER_AMOUNT)
    clear_file_and_add_amount(add_audio_specialist, config.TABLE_AUDIO_SPECIALISTS, config.AUDIO_SPECIALIST_AMOUNT)
    clear_file_and_add_amount(add_digitizer, config.TABLE_DIGITILIZERS, config.DIGITILIZER_AMOUNT)
    clear_file_and_add_amount(add_smoothing_specialist, config.TABLE_SMOOTHING_SPECIALIST, config.SMOOTHING_SPECIALIST_AMOUNT)
    clear_file_and_add_amount(add_art_director, config.TABLE_ART_DIRECTOR, config.ART_DIRECTOR_AMOUNT)
    clear_file_and_add_amount(add_screenwriter, config.TABLE_SCREENWRITERS, config.SCREENWRITER_AMOUNT)
    clear_file_and_add_amount(add_director, config.TABLE_DIRECTORS, config.DIRECTOR_AMOUNT)
    clear_file_and_add_amount(add_roles_designer, config.TABLE_ROLES_DESIGNERS, config.ROLES_DESIGNER_AMOUNT)
    clear_file_and_add_amount(add_recording_actor, config.TABLE_RECORDING_ACTORS, config.RECORDING_ACTOR_AMOUNT)
    clear_file_and_add_amount(add_editor, config.TABLE_EDITORS, config.EDITOR_AMOUNT)
    clear_file_and_add_amount(add_artist, config.TABLE_ARTISTS, config.ARTIST_AMOUNT)

    clear_file_and_add_amount(add_storyboard_process, config.TABLE_STORYBOARD_PROCESSES, config.STORYBOARD_PROCESSES_AMOUNT)
    clear_file_and_add_amount(add_adevertising_process, config.TABLE_ADVERTISING_PROCESSES, config.ADVERTISING_PROCESSES_AMOUNT)
    clear_file_and_add_amount(add_adding_sound_process, config.TABLE_ADDING_SOUND_PROCESSES, config.ADDING_SOUND_PROCESSES_AMOUNT)
    clear_file_and_add_amount(add_digitization_process, config.TABLE_DIGITILIZATION_PROCESSES, config.DIGITILIZATION_PROCESSES_AMOUNT)
    clear_file_and_add_amount(add_smoothing_process, config.TABLE_SMOOTHING_PROCESSES, config.SMOOTHING_PROCESSES_AMOUNT)
    clear_file_and_add_amount(add_revisions_process, config.TABLE_REVISION_PROCESSES, config.REVISION_PROCESSES_AMOUNT)
    clear_file_and_add_amount(add_coloring_process, config.TABLE_COLORING_PROCESSES, config.COLORING_PROCESSES_AMOUNT)
    clear_file_and_add_amount(add_animation_process, config.TABLE_ANIMATION_PROCESSES, config.ANIMATION_PROCESSES_AMOUNT)
    clear_file_and_add_amount(add_adding_effect_process, config.TABLE_ADDING_EFFECT_PROCESSES, config.ADDING_EFFECT_PROCESSES_AMOUNT)
    clear_file_and_add_amount(add_location_drawing_process, config.TABLE_LOCATION_DRAWING_PROCESSES, config.LOCATION_DRAWING_PROCESSES_AMOUNT)
    clear_file_and_add_amount(add_battle_drawing_process, config.TABLE_BATTLE_DRAWING_PROCESSES, config.BATTLE_DRAWING_PROCESSES_AMOUNT)
    clear_file_and_add_amount(add_character_drawing_process, config.TABLE_CHARACTER_DRAWING_PROCESSES, config.CHARACTER_DRAWING_PROCESSES_AMOUNT)
    clear_file_and_add_amount(add_character_select_process, config.TABLE_CHARACTER_SELECT_PROCESSES, config.CHARACTER_SELECT_PROCESSES_AMOUNT)
    clear_file_and_add_amount(add_voice_acting_process, config.TABLE_VOICE_ACTING_PROCESSES, config.VOICE_ACTING_PROCESSES_AMOUNT)

    clear_file_and_add_amount(add_ability_description_process, config.TABLE_ABILITY_DESCRIPTION_PROCESSES, config.ABILITY_DESCRIPTION_PROCESSES_AMOUNT)
    clear_file_and_add_amount(add_character_description_process, config.TABLE_CHARACTER_DESCRIPTION_PROCESSES, config.CHARACTER_DESCRIPTION_PROCESSES_AMOUNT)
    clear_file_and_add_amount(add_location_description_process, config.TABLE_LOCATION_DESCRIPTION_PROCESSES, config.LOCATION_DESCRIPTION_PROCESSES_AMOUNT)
    clear_file_and_add_amount(add_battle_description_process, config.TABLE_BATTLE_DESCRIPTION_PROCESSES, config.BATTLE_DESCRIPTION_PROCESSES_AMOUNT)
    clear_file_and_add_amount(add_plot_process, config.TABLE_PLOT_PROCESSES, config.PLOT_PROCESSES_AMOUNT)

    clear_file_and_add_amount(add_plot, config.TABLE_PLOT, config.PLOT_AMOUNT)
    clear_file_and_add_amount(add_event, config.TABLE_EVENTS, config.EVENTS_AMOUNT)
    clear_file_and_add_amount(add_location, config.TABLE_LOCATIONS, config.LOCATIONS_AMOUNT)
    clear_file_and_add_amount(add_battle, config.TABLE_BATTLE, config.BATTLE_AMOUNT)
    clear_file_and_add_amount(add_abilities, config.TABLE_ABILITIES, config.ABILITIES_AMOUNT)


if __name__ == '__main__':
    main()










