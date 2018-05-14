def reference_generator(instance, new_refence=None):
    # if new_refence is None:
    type = instance.type.code
    sphere = instance.sphere
    cylindre = instance.cylindre
    axis = instance.axe_text
    addition = instance.addition_title
    reference = "{type} {sphere} {cylindre} {axis} {addition}".format(type=type, sphere=sphere, cylindre=cylindre, addition=addition, axis=axis)
    return reference
