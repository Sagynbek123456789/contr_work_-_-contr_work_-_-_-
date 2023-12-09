def task_validate(author, mail, description, status):
    errors = {}
    if not author:
        errors['author'] = 'Обязательно'
    elif len(author) > 60:
        errors['author'] = 'превышает'

    if not description:
        errors['description'] = 'Обязательно'
    elif len(description) > 50:
        errors['description'] = 'превышает'

    if not status:
        errors['status'] = 'Обязательно'

    if not mail:
        errors['mail'] = 'Обязательно'
    elif len(author) > 70:
        errors['author'] = 'превышает'

    return errors

