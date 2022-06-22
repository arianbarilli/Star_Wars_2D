import cx_Freeze

executables = [cx_Freeze.Executable(
    script="StarWars2D.py", icon="assets/Vader.ico")]

cx_Freeze.setup(
    name="STAR WARS X-WING ATTACK",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets"]
                           }},
    executables = executables
)
