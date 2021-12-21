#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument('filename')
@click.option("-n", "--name")
@click.option("-g", "--group")
@click.option("-p", "--progress")
def add(filename, name, group, progress):
    """
    Добавление нового студента
    """
    students = open_file(filename)
    students.append(
        {
            'name': name,
            'group': group,
            'progress': progress
        }
    )
    with open(filename, "w", encoding="utf-8") as out:
        json.dump(students, out, ensure_ascii=False, indent=4)


@cli.command()
@click.argument('filename')
def select(filename):
    """
    Выбор студента по успеваемости
    """
    students = open_file(filename)
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Ф.И.О.",
            "Группа",
            "Успеваемость"))
    print(line)
    for pupil in students:
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


@cli.command()
@click.argument('filename')
def display(filename):
    """
    Вывод списка студентов
    """
    students = open_file(filename)
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Ф.И.О.",
            "Группа",
            "Успеваемость"))
    print(line)
    for i, pupil in enumerate(students, 1):
        print(
            '| {:<4} | {:<30} | {:<20} | {:<15} |'.format(
                i,
                pupil.get('name', ''),
                pupil.get('group', ''),
                pupil.get('progress', 0)
            )
        )
    print(line)


def open_file(filename):
    with open(filename, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main():
    cli()


if __name__ == '__main__':
    main()
