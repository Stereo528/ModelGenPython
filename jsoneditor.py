#!usr/bin/python3
import json
import PySimpleGUI as sg
import os

#print(f"Using PySimpleGUI Version: {sg.version}")



sg.theme('DarkGrey4')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Parent Model'), sg.InputText("block/cube_all")],
            [sg.Text('Block/Item'), sg.InputText("block")],
            [sg.Text('Name'), sg.InputText("birch_planks")],
            [sg.Text('ModID'), sg.InputText("minecraft")],
            [sg.Checkbox('Auto Save to last used dir'), sg.Button('!')],
            [sg.Button("Save"), sg.Button("Close")]
            ]

# Create the Window
window = sg.Window('Minecraft Model Generator', layout)
# Event Loop to process "events"
while True:             
    event, values = window.read()

    if (event == "!"):
        sg.popup_non_blocking("Only use after you have chosen to save a file, it will save to the current folder otherwise!")

    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Close') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
        openLastDir.close()
        break
    if event == "Save":
        openLastDir = open("lastdir.json", "r")
        lastUsedDir = json.load(openLastDir)
        openLastDir.close()
        #If the checkbox to save directly to last used folder without the popup, is not checked, give the popup, otherwise dont.
        if values[4] == False:
            saveLocation = sg.popup_get_folder(f"Folder to save {values[2]}.json To", title="Save Location", default_path=lastUsedDir["lastFolder"])
        elif values[4] == True:
            saveLocation = lastUsedDir["lastFolder"]

        #Cancel button returns "None", so if there is anything but "None", save the File
        if saveLocation != None:
            with open(f"{saveLocation}/{values[2]}.json", "w") as JsonOpen:
                JsonLayout = {
                        "parent": f"{values[3]}:" f"{values[0]}",
                        "textures": {
                            "all": f"{values[3]}:" f"{values[1]}/{values[2]}"
                        }
                    }
                JsonDump = json.dumps(JsonLayout, indent=4)
                JsonOpen.write(JsonDump)
            sg.popup(f"saved {values[2]}.json")
            print("saved file")

            #Save last used directory to a json, so it auto completes (if the option is enabled)
            #Also really hacky because idk wtf im doing
            with open("lastdir.json", "r") as readDir:
                lastFolder = json.load(readDir)
                if lastFolder["lastFolder"] == saveLocation:
                    sameFolder = True
                else:
                    sameFolder = False
            if sameFolder == False:
                with open("lastdir.json", "w") as writeDir:
                    yep = {
                        "lastFolder":  f"{saveLocation}"
                    }
                    nope = json.dumps(yep)
                    writeDir.write(nope)
                    print("saved last used directory")
            else:
                continue
        else:
            print("Canceling Saving")

window.close()