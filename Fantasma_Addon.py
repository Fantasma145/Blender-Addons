bl_info = {
    "name": "Fantasma's UVs",
    "blender": (2, 82, 0),
    "category": "UV",
}

import bpy
   
class CorrectUvs(bpy.types.Operator):
    bl_idname = 'uv.correct'
    bl_label = 'Add Cube'
    def execute(self,context):
    # Loops through selected objects
        for ob in bpy.context.selected_objects:     
            bpy.context.view_layer.objects.active = ob
            mesh = bpy.context.active_object.data

            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT') # Select all
            bpy.ops.uv.select_all(action='SELECT')

            bpy.ops.uv.average_islands_scale();
            bpy.ops.uv.pack_islands(rotate = 1, margin = 0.05);
            bpy.ops.uv.seams_from_islands()
            return {"FINISHED"}    
            
class CorrectUvsPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_hello_world3"
    bl_label = "Correct UVs"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'

    def draw(self, context):
        self.layout.label(text="Correct Uv's")
    def draw(self, context):
        self.layout.operator("uv.correct", icon='MESH_CUBE', text="Currect UV's")

def register():
    bpy.utils.register_class(CorrectUvs)
    bpy.utils.register_class(CorrectUvsPanel)

def unregister():
    bpy.utils.unregister_class(CorrectUvs)
    bpy.utils.unregister_class(CorrectUvsPanel)
    
#register()