# This file is a part of the HiRISE DTM Importer for Blender
#
# Copyright (C) 2017 Arizona Board of Regents on behalf of the Planetary Image
# Research Laboratory, Lunar and Planetary Laboratory at the University of
# Arizona.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

"""A HiRISE DTM Importer for Blender"""

bl_info = {
    "name": "HiRISE DTM Importer",
    "author": "Nicholas Wolf (nicwolf@pirl.lpl.arizona.edu) / phaseIV",
    "version": (0, 3, 0),
    "blender": (4, 2, 0),
    "license": "GPL",
    "location": "File > Import > HiRISE DTM (.img)",
    "description": "Import a HiRISE DTM as a mesh",
    "warning": "May consume a lot of memory",
    "category": "Import-Export",
    "wiki_url": "",  # TBD
    "tracker_url": "",  # TBD
    "link": "",  # TBD
}

if "bpy" in locals():
    import importlib
    importlib.reload(importer)
    importlib.reload(terrainpanel)
else:
    from .ui import importer
    from .ui import terrainpanel

import bpy


def menu_import(self, context):
    i = importer.ImportHiRISETerrain
    self.layout.operator(i.bl_idname, text=i.bl_label)


classes = (
    importer.ImportHiRISETerrain,
    terrainpanel.TerrainPanel,
    terrainpanel.ReloadTerrain,
)


def register():
    from bpy.utils import register_class
    from bpy.props import FloatProperty
    for cls in classes:
        register_class(cls)
    bpy.types.TOPBAR_MT_file_import.append(menu_import)

    # Register custom properties on Object (must be done here, not in class body)
    bpy.types.Object.dtm_resolution = FloatProperty(
        subtype="PERCENTAGE",
        name="New Resolution",
        description=(
            "Percentage scale for terrain model resolution. 100% loads the "
            "model at full resolution (one vertex per post) and is "
            "*MEMORY INTENSIVE*. Downsampling uses Nearest Neighbors."
        ),
        min=1.0, max=100.0, default=10.0
    )
    bpy.types.Object.scaled_dtm_resolution = FloatProperty(
        options={'HIDDEN'},
        name="Scaled Terrain Model Resolution",
        get=(lambda self: self.dtm_resolution / 100.0)
    )


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    bpy.types.TOPBAR_MT_file_import.remove(menu_import)

    del bpy.types.Object.dtm_resolution
    del bpy.types.Object.scaled_dtm_resolution


if __name__ == '__main__':
    register()

