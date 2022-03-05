def make_car(manufacturer, model_name, **kwaugs):
    """Build dict containing everything we know about a car."""
    kwaugs['make'] = manufacturer
    kwaugs['model'] = model_name
    return kwaugs