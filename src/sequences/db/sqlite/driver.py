from django.core.management import sql, color
from django.db import connection

def create_sequence(name, initial_value=1, final_value=None):
    model = create_model(name)

    if not sequence_exists(name):
        style = color.no_style()

        cursor = connection.cursor()
        statements, pending = sql.sql_model_create(model, style)
        for sql in statements:
            cursor.execute(sql)

    set_limits(name, initial_value=1, final_value=None)

def sequence_exists(name):
    return name in connection.introspection.table_names()

def create_model(name):
    """
    Create specified model
    """
    class Meta:
        db_table = name
        get_latest_by = "id"

    
    # Set up a dictionary to simulate declarations within a class
    attrs = {'__module__': 'sequences.models', 'Meta': Meta}

    # Create the class, which automatically triggers ModelBase processing
    model = type(name, (models.Model,), attrs)

    return model

def current_value(name):
    model = create_model(name)

    try:
        inst = model.objects.lastest()
    except:
        return 0

    return inst.id

def next_value(name):
    model = create_model(name)
    inst = model()

    inst.save()
    return inst.id

def set_next_value(name, initial_value):
    model = create_model(name)
    model.objects.all().delete()

    if (initial_value > 1):
        inst = model()
        inst.id = initial_value - 1
        inst.save()

def set_limits(name, initial_value=1, final_value=None):
    if (current_value(self.name) < initial_value - 1):
            set_next_value(self.name, initial_value)
    
def reset(name, initial_value = 1):
    set_next_value(name, initial_value)

def delete(name):
    if not sequence_exists(name):
        style = color.no_style()

        cursor = connection.cursor()
        statements, pending = sql.sql_destroy_model(model, [], style)
        for sql in statements:
            cursor.execute(sql)
    
    