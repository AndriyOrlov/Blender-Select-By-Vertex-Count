import bpy

active_object = bpy.context.view_layer.objects.active
active_verts = len(active_object.data.vertices)

for all_objects in  bpy.context.view_layer.objects:
    if all_objects.type == 'MESH':
        all_objects_verts = len(all_objects.data.vertices)           
        if all_objects_verts == active_verts:
            all_objects.select_set(state = True)