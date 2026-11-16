"""Downloads photographic planet textures (Solar System Scope, CC BY 4.0) and names them as the tour expects.
Run on a computer with internet:  python get_textures.py"""
import os,urllib.request
B='https://www.solarsystemscope.com/textures/download/'
F={'8k_earth_daymap.jpg':'8k_earth.jpg','8k_moon.jpg':'8k_moon.jpg','8k_mercury.jpg':'8k_mercury.jpg','8k_venus_surface.jpg':'8k_venus.jpg','8k_mars.jpg':'8k_mars.jpg','8k_jupiter.jpg':'8k_jupiter.jpg','8k_saturn.jpg':'8k_saturn.jpg','8k_sun.jpg':'8k_sun.jpg','2k_uranus.jpg':'4k_uranus.jpg','2k_neptune.jpg':'4k_neptune.jpg','4k_ceres_fictional.jpg':'4k_ceres.jpg','4k_eris_fictional.jpg':'4k_eris.jpg','4k_haumea_fictional.jpg':'4k_haumea.jpg','4k_makemake_fictional.jpg':'4k_makemake.jpg'}
here=os.path.dirname(os.path.abspath(__file__))
for src,dst in F.items():
    p=os.path.join(here,dst)
    if os.path.exists(p):print('have',dst);continue
    try:
        r=urllib.request.Request(B+src,headers={'User-Agent':'Mozilla/5.0'});open(p,'wb').write(urllib.request.urlopen(r,timeout=180).read());print('ok  ',dst)
    except Exception as e:print('FAIL',src,e)
