import pandas as pd


def rooms_data():
    # Read the Room Timeslot file
    sheet_id = '1YLtL73eIFh_0jYemsBi5cd3lyYYMR5ce'
    url = f'https://docs.google.com/spreadsheets/export?id={sheet_id}&format=xlsx'
    room = pd.read_excel(url, header=None)

    # Extract the specified range
    room_number = room.loc[3:, 0].squeeze().astype(
        int).tolist()  # Room number (integer)
    room_id = room.loc[3:, 1].squeeze().astype(
        str).tolist()  # Room ID (string)
    room_name = room.loc[3:, 2].squeeze().astype(
        str).tolist()  # Room name (string)
    room_capacity = room.loc[3:, 3].squeeze().astype(
        int).tolist()  # Room capacity (integer)
    # Room availability (List of array)
    room_availability = room.loc[3:, 4:23].values.tolist()

    return room_number, room_capacity


def assistants_data():
    # Read the Teaching Assistant Timeslot file
    sheet_id = '1bV0QkqoL1k7QUh3wQTpekC45otwX79o7'
    url = f'https://docs.google.com/spreadsheets/export?id={sheet_id}&format=xlsx'
    ta = pd.read_excel(url, header=None)

    # Extract the specified range
    ta_end_row = 14

    ta_number = ta.loc[3:ta_end_row, 0].squeeze().astype(
        int).tolist()  # Teaching Assistant number (integer)
    ta_sid = ta.loc[3:ta_end_row, 1].squeeze().astype(
        str).tolist()  # Teaching Assistant student ID (string)
    ta_fname = ta.loc[3:ta_end_row, 2].squeeze().astype(
        str).tolist()  # Teaching Assistant full name (string)
    ta_codeboard = ta.loc[3:ta_end_row, 3].squeeze().astype(
        str).tolist()  # Teaching Assistant codeboard (string)
    ta_initial = ta.loc[3:ta_end_row, 4].squeeze().astype(
        str).tolist()  # Teaching Assistant initial (string)
    # Teaching Assistant availability (List of array)
    ta_availability = ta.loc[3:ta_end_row, 5:24].values.tolist()

    return ta_number


def students_data():
    # Read the Student Timeslot file
    sheet_id = '1yo-G9-aeIzc6kXJ4SXR2qHtgU8qHTuxP'
    url = f'https://docs.google.com/spreadsheets/export?id={sheet_id}&format=xlsx'
    student = pd.read_excel(url, header=None)

    # Extract the specified range
    student_end_row = 231

    student_number = student.loc[3:student_end_row, 0].squeeze().astype(
        int).tolist()  # Student number (integer)
    student_sid = student.loc[3:student_end_row, 1].squeeze().astype(
        str).tolist()  # Student ID (string)
    student_fname = student.loc[3:student_end_row, 2].squeeze().astype(
        str).tolist()  # Student full name (string)
    student_class = student.loc[3:student_end_row, 3].squeeze().astype(
        str).tolist()  # Student class (string)
    # Student availability (List of array)
    student_availability = student.loc[3:student_end_row, 4:23].values.tolist()

    return student_number


def timeslots_data():
    timeslots_number = list(range(1, 21))

    return timeslots_number
