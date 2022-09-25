from vkwave.bots.utils.keyboards import Template


async def create_carusel(obj, filter=None, add_back=False):
    '''Создание "карусели" Вконтакте.'''
    templates = []
    if not filter:
        items = await obj.query.gino.all()
    else:
        items = await obj.query.where(obj.category_id == filter).gino.all()
    for item in items:
        template = Template(
            title=f'{item.name}',
            description=f'{item.description}',
            photo_id=f'{item.photo_id}',
        )
        template.add_callback_button(
            "Выбрать",
            payload={'button': template.title}
        )
        if add_back:
            template.add_callback_button(
                "Назад",
                payload={'button': 'Назад'}
            )
        templates.append(template)
    return Template.generate_carousel(*templates)
