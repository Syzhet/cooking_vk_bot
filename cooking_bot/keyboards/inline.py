from vkwave.bots.utils.keyboards import Template


async def create_carusel(obj):
    templates = []
    items = await obj.query.gino.all()
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
        templates.append(template)
    return Template.generate_carousel(*templates)
