# Blender-Hirise-DTM-Importer

Modified version of the original Hirise DTM importer addon that will work with Blender 2.8+.  
The original addon is written by Nicholas Wolf and Tim Spriggs.

Instructions can be found [here](https://hemelmechanica.nl/hirise-docs/quickstart.html)

Checkout this great video made by Waylena to see how to use this software.  
[https://fossdome.com/fun-with-blender-and-mars/](https://fossdome.com/fun-with-blender-and-mars/)

---

## Blender 4.2 / 5.0 Compatibility Update

Updated by **C. A. Merriman** to support Blender 4.2+ and Blender 5, including Apple Silicon (M-series) Macs.

### Changes made

- `blender_manifest.toml` added — required by the Blender 4.2+ extension system
- Minimum Blender version updated to `4.2.0`
- Replaced deprecated dict-style context override (`bpy.ops.view3d.view_selected(override)`) with the modern `with context.temp_override(...)` syntax required since Blender 4.0
- Moved `bpy.types.Object` custom property registration (`dtm_resolution`, `scaled_dtm_resolution`) out of the class body and into `register()` / `unregister()` as required by modern Blender
- Replaced `np.fromstring()` (removed in NumPy 2.x, bundled with Blender 5) with `np.frombuffer()` for binary special value parsing
- Replaced `np.NaN` (removed in NumPy 2.x) with `np.nan`
