import bpy


def main(context):
    ob = context.active_object
    if ob.type == 'FONT':
        bpy.ops.object.convert(target='CURVE')
        oldob = context.active_object
        
        bpy.ops.object.convert(target='GPENCIL')
        newob = context.active_object
        
        newob.location = oldob.location
        newob.rotation_euler = oldob.rotation_euler
        newob.scale = oldob.scale       
        
        
        override = bpy.context.copy()
        override['selected_objects'] = [oldob]
        bpy.ops.object.delete(override)        
            
    else:
        print("Not a Text Object")


class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.text_to_grease"
    bl_label = "Text to Grease Pencil"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(SimpleOperator)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.text_to_grease()
