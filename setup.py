from setuptools import setup
APP = ['main.py']
DATA_FILES = ['alarm1.mp3','timer.py','chrono.py','clock.png']
OPTIONS = {
    'argv_emulation': True,
    'site_packages': True,
    'iconfile': 'clock.png',
    'packages': ['tkinter','playsound'],
    'plist': {
        'CFBundleName': 'Cronometro',
    }
}
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)