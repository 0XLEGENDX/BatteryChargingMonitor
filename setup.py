import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Tells cx_Freeze to not create a visible window


setup(
    name="BatteryReports",
    version="1.0",
    description="This app generates battery reports and charging time.",
    options={"build_exe": {"includes": ["win32timezone"]}},
    executables=[Executable("battery.py")]
)
