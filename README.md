# ableton-smk25-custom-midi-script-configuration
A custom Ableton MIDI remote script and config for the SMK25, tailored for my taste,but good for general controls.

Keywords: SMK25,M Vave,MVave,M-Vave

Balls

I made this thing since M-Vave doesn't reply to my emails.

Its a configuration for the M-Vave SMK25 so it works with Ableton and published it so no one else goes through what hell i went through.


How to use this:

0 Download this configuration

1 Install Midisuite off the M-Vave website: https://www.cuvave.com/appdownload

2 Go to the Presets tab and press the import config button. Import the SMK25_Config.mkc file from the downloaded files.

3 Save the config, if you don't it will return to default the next time you restart your SMK25.

4 Go to your Ableton install (You should find it under ProgramData, this folder is hidden by default on Windows) and find Resources/Midi Remote Scripts.

5 Paste the SMK25 folder in there.

Thats about it, now go in Ableton, go to settings and select the SMK25 from the MIDI section and it should work just fine.



What each button does:

Pads 1-8:

1(Red): Undo
2(Green): Redo
3(Light blue): Turn on Metronome
4(Purple): Turns on Overdub recording (red circle on top)
5(Red): Phase Nudge Down (buttons next to the metronome)
6(Green): Phase Nudge Up
7(Light Blue): See the devices/Samples on the bottom
8(Purple): Clip/MIDI View

Pads 9 to 16 are meant for being used as a drum pad. You can turn them on by pressing PAD-B on your keyboard, they are based on what Ableton usually uses for their drum racks.

The Red one is Kick
Blue is Snare
Yellow is Hihat

Play,Stop,Rec buttons Play,Stop and Record (shockers)


Knobs:

First 4 knobs control the volume of the first 4 tracks

Knob 5 is empty
Knob 6 controls Tempo
Knob 7 is empty
Knob 8 controls Master Volume

Knobs 9-16 (Turn them on with the KNOB-B button) are left empty and meant to be used for parameters of instruments to your liking.


If you are feeling brave, you can make changes to this configuration by going to the MIDI_Map file and the Midisuite app and changing values there. Please let me know if you make any modifications to your files, i am looking for suggestions too.

Credit to the author of the original scripts that made this possible.The original project is linked below

https://github.com/laidlaw42/ableton-live-midi-remote-scripts/tree/YourControllerName


This has been tested with Ableton 11 using Python 3, i do not guarantee that this will work for any other series, especially the ones below 11 since they use Python 2 scripting.


