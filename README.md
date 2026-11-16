# Cosmos Tour Pro
Pages: `rockets.html` (Rocket Missions: 9 real launch vehicles × 5 real satellites, full launch-to-deploy sequence, new audio) · `index.html` (Cosmos Tour, 14 chapters) · `satellites.html` (Satellite Tour, 9 chapters). Each file is self-contained; keep them in the same folder so the top navigation works.
## Run
1. (Optional, for photographic 8K planets) `python textures/get_textures.py` — needs internet, ~150 MB. Files load 8K → 4K → remote → procedural, so missing files never break anything.
2. `python serve.py` → http://localhost:8000, or upload the folder to any web host.
## Controls
Drag = look · wheel/pinch = zoom · ← → = previous/next · Space = auto/manual · F = full screen · S = sound · **Layers control (Surface · Close · Cutaway · Core), or ↑ ↓, is always manual.**
## Credits
Textures: Solar System Scope (CC BY 4.0), NASA. three.js r128 (MIT) loaded from cdnjs.

`ocean.html` — Ocean Dive: submarine descent through 5 oceans/trenches and 2 rivers. Auto/Manual (↑/↓ or slider). `rockets.html?solo=1&r=0..8` opens one rocket in its own interface.

## Real 3D models
`models/*.glb` are real NASA spacecraft models (NASA 3D Resources, github.com/nasa/NASA-3D-Resources): Hubble, James Webb, Chandra, Parker Solar Probe, Juno, Cassini, Kepler, Landsat 8, LRO, MRO. They load in `rockets.html` (as the deployed payload) and in the new "Real satellite models" viewer in `satellites.html`. Serve with `python serve.py` (browsers block model loading from file://). `vendor/` holds three.js r128 (MIT) and its GLTFLoader so the rocket page works offline.
Ocean Dive now has tide (60 s demo cycle), depth-dependent currents and river flow.


## Ocean Dive upgrade
Harmonic tide (M2/S2/K1/O1, spring/neap) on a 2400x clock, depth-dependent current (mean flow + Ekman turn + tidal stream + bottom boundary layer), animated wave surface, dive speed up to 1500 m/s. Creatures are lofted anatomies with species skins, wet-skin clearcoat, GPU swim cycles and velocity-driven heading. **Photoreal drop-in:** put a GLB (nose along +X) at `models/sea/<species-name>.glb` (e.g. `blue-whale.glb`, `great-white-shark.glb`) and it replaces the procedural body automatically.

## v4.0 Real Asset + Launch Engineering Upgrade
- Run `python tools/fetch_models.py` to fetch NASA rocket/satellite GLBs and licensed marine GLBs.
- Rocket Launch now has a highly visible `LAUNCH NOW` control and an Engineering Details panel.
- The launch is a digital educational simulation with staged ascent, telemetry, engine events and payload separation; it does not control or command a physical rocket.
- Ocean creatures use downloaded GLB assets when available and retain procedural fallback models.

## v4.0 Real Asset + Launch Engineering Upgrade
- Run `python tools/fetch_models.py` to fetch NASA rocket/satellite GLBs and licensed marine GLBs.
- Rocket Launch now has a highly visible `LAUNCH NOW` control and an Engineering Details panel.
- The launch is a digital educational simulation with staged ascent, telemetry, engine events and payload separation; it does not control or command a physical rocket.
- Ocean creatures use downloaded GLB assets when available and retain procedural fallback models.
