#!usr/bin/python3
import json
import PySimpleGUI as sg

print(f"Using PySimpleGUI Version: {sg.version}")

sg.theme('DarkGrey4')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Parent Model'), sg.InputText("block/cube_all")],
            [sg.Text('Block/Item'), sg.InputText("block")],
            [sg.Text('Name'), sg.InputText("birch_planks")],
            [sg.Text('ModID'), sg.InputText("minecraft")],
            [sg.Button("Save"), sg.Button("Close")]]

# Create the Window
window = sg.Window('Minecraft Model Generator', layout)
# Event Loop to process "events"
while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Close'):
        break
    if event in ("Save"):
        saveLocation = sg.popup_get_folder(f"Folder to save {values[2]}.json To", title="Save Location", default_path="", no_window=True)
        with open(f"{saveLocation}/{values[2]}.json", "w") as JsonOpen:
            JsonLayout = {

                #"{\n\"parent\": \"{values[3]}:{values[1]}\",\n\"textures\": {\n\t\"all\": \"{values[3]}:{values[1]}/{values[2]}\"\n}"
                
                    "parent": f"{values[3]}:" f"{values[0]}",
                    "textures": {
                        "all": f"{values[3]}:" f"{values[1]}/{values[2]}"
                    }
                
            }
            
            JsonDump = json.dumps(JsonLayout, indent=4)
            JsonOpen.write(JsonDump)
        
        sg.popup(f"saved {values[2]}.json")

window.close()