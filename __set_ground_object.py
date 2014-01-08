# Blender object alignment tool
# Set Ground Object is Blender(2.69)plug-in that is released under the MIT lisence
#

bl_info = {
	"name": "Set Ground Object",
	"author": "Phiyory",
	"version": (1, 0),
	"blender": (2, 69, 0),
	"location": "View3D > Specials > Set Ground Object",
	"description": "Align the object at the bottom",
	"warning": "",
	"wiki_url": ""\
	"",
	"category": "Object"}

import bpy

class Set_Ground_Object(bpy.types.Operator):
#	bl_idname must be included in bl_info.
	bl_idname = 'object.set_ground_object'
	bl_label = 'SetGroundObject'
	bl_options = {"REGISTER", "UNDO"}
	
	def execute(self, context):
		for i in context.selected_objects:
			i.location[2] = 0
			z = i.dimensions[2]
			i.location[2] += z/2
		return {'FINISHED'}


def menu_func(self, context):
	self.layout.operator(Set_Ground_Object.bl_idname, text=Set_Ground_Object.bl_label)


# register the class
def register():
	bpy.utils.register_module(__name__)
	bpy.types.VIEW3D_MT_object_specials.append(menu_func)

def unregister():
	bpy.utils.unregister_module(__name__)
	bpy.types.VIEW3D_MT_object_specials.remove(menu_func)

if __name__ == "__main__": 
	register()
