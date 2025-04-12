# Ableton SMK25 Custom MIDI Script Configuration

Balls.

A custom Ableton MIDI remote script and configuration for the SMK25, tailored for my preferences but also useful for general controls.

**Keywords:** SMK25, M Vave, MVave, M-Vave

---

## Why I Made This
I created this configuration because M-Vave didn't respond to my emails. This setup ensures the M-Vave SMK25 works seamlessly with Ableton. I've shared it to save others from the frustration I experienced.

---

## How to Use This Configuration

1. **Download this configuration.**
2. **Install Midisuite** from the M-Vave website: [https://www.cuvave.com/appdownload](https://www.cuvave.com/appdownload).
3. **Import the configuration:**
   - Open the Midisuite app.
   - Navigate to the "Presets" tab and click the "Import Config" button.
   - Import the `SMK25_Config.mkc` file from the downloaded files.
4. **Save the configuration:**
   - Ensure you save the config. If not, it will revert to default when you restart the SMK25.
5. **Add the MIDI script to Ableton:**
   - Locate your Ableton installation folder (commonly found under `ProgramData`, which is hidden by default on Windows).
   - Navigate to `Resources/Midi Remote Scripts`.
   - Paste the `SMK25` folder into this directory.
6. **Set up MIDI in Ableton:**
   - Open Ableton.
   - Go to **Settings** > **MIDI** and select "SMK25" from the MIDI section.

---

## Button Mappings

### Pads 1-8
| **Pad** | **Color**      | **Function**                     |
|---------|----------------|-----------------------------------|
| 1       | Red            | Undo                             |
| 2       | Green          | Redo                             |
| 3       | Light Blue     | Turn on Metronome                |
| 4       | Purple         | Overdub Recording (red circle)   |
| 5       | Red            | Phase Nudge Down                 |
| 6       | Green          | Phase Nudge Up                   |
| 7       | Light Blue     | Show Devices/Samples View        |
| 8       | Purple         | Clip/MIDI View                   |

### Pads 9-16 (Drum Pad Mode)
Press **PAD-B** on your keyboard to activate. These pads are mapped to Ableton's drum rack:

| **Pad** | **Color** | **Instrument** |
|---------|-----------|----------------|
| 9       | Red       | Kick           |
| 10      | Blue      | Snare          |
| 11      | Yellow    | Hi-hat         |

### Transport Controls
| **Button** | **Function** |
|------------|--------------|
| Play       | Play         |
| Stop       | Stop         |
| Record     | Record       |
The rest are left as is.
---

## Knob Mappings

### Knobs 1-8
| **Knob** | **Function**          |
|----------|-----------------------|
| 1-4      | Volume for Tracks 1-4 |
| 5        | Empty                 |
| 6        | Tempo                 |
| 7        | Empty                 |
| 8        | Master Volume         |

### Knobs 9-16 (Parameter Mode)
Activate with the **KNOB-B** button. These knobs are left empty for custom instrument parameter mapping.

---

## Customization
If you're feeling adventurous, you can modify the configuration using the `MIDI_Map` file and the Midisuite app.

If you make any modifications, please share them with me, Im curious on how you could improve this.

---

## Additional Notes
- **Original Scripts:** Credit to the author of the original scripts that made this possible. The original project is linked below:  
  [https://github.com/laidlaw42/ableton-live-midi-remote-scripts/tree/YourControllerName](https://github.com/laidlaw42/ableton-live-midi-remote-scripts/tree/YourControllerName)
- **My own input on the Play, Stop and Rec buttons**: I found that it was only possible to use them by changing them to CC and modifying the code in SMK25.py. DO NOT CHANGE THEIR MAPPINGS IN MIDI_Map
- **Compatibility:** Tested with Ableton 11 using Python 3. This configuration may not work with earlier versions of Ableton (especially pre-11, which use Python 2).

---

## Final Thoughts
I hope this configuration makes your experience with the SMK25 and Ableton much smoother!
