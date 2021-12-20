#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import click


def add_student(students, name, group, progress, file_name):
    """
    Добавление нового студента
    """
    students.append(
        {
            'name': name,
            'group': group,
            'progress': progress
        }
    )

    with open(file_name, "w", encoding="utf-8") as file_out:
        json.dump(students, file_out, ensure_ascii=False, indent=4)
    return students


def display_students(line, students):
    """
    Вывод списка студентов
    """
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Ф.И.О..",
            "Группа",
            "Успеваемость"
        )
    )
    print(line)
    # Вывести данные о всех студентах.
    for idx, student in enumerate(students, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                idx,
                student.get('name', ''),
                student.get('group', ''),
                student.get('progress', 0)
            )
        )
    print(line)


def select_students(line, undergraduates):
    """
    Выбор студентов
    """
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Ф.И.О.",
            "Группа",
            "Успеваемость"
        )
    )
    print(line)

    for pupil in undergraduates:
        evaluations = pupil.get('progress')
        list_of_rating = list(evaluations)
        count = 0
        for z in list_of_rating:
            if z == '2':
                count += 1
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                        count,
                        pupil.get('name', ''),
                        pupil.get('group', ''),
                        pupil.get('progress', 0)
                    )
                )
    print(line)


def opening(filename):
    with open(filename, "r", encoding="utf-8") as f_in:
        return json.load(f_in)


@click.command()
@click.option("-c", "--command")
@click.argument('filename')
@click.option("-n", "--name")
@click.option("-g", "--group")
@click.option("-p", "--progress")
def main(command, filename, name, group, progress):
    students = opening(filename)
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    if command == 'add':
        add_student(students, name, group, progress, filename)
        click.secho('Студент добавлен', fg='green')
    elif command == 'display':
        display_students(line, students)
    elif command == 'select':
        select_students(line, students)


if __name__ == '__main__':
    main()
