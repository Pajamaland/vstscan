import os
import platform
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# get current date and time
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

def get_default_vst_paths():
    # return standard VST paths based on OS
    system = platform.system()
    paths = []
    
    if system == "Windows":
        paths = [
            r"C:\Program Files\Common Files\VST3",
            r"C:\Program Files\VSTPlugins",
            r"C:\Program Files\Steinberg\VSTPlugins",
            r"C:\Program Files\Common Files\VST2",
            r"C:\Program Files (x86)\Common Files\VST3",
            r"C:\Program Files (x86)\VSTPlugins",
            r"C:\Program Files (x86)\Steinberg\VSTPlugins",
        ]
    elif system == "Darwin":  # macOS
        paths = [
            "/Library/Audio/Plug-Ins/VST",
            "/Library/Audio/Plug-Ins/VST3",
            os.path.expanduser("~/Library/Audio/Plug-Ins/VST"),
            os.path.expanduser("~/Library/Audio/Plug-Ins/VST3")
        ]
    else:
        print("unsupported OS for standard paths. please add paths manually.")
        
    return [Path(p) for p in paths if os.path.exists(p)]

def scan_plugins(paths):
    # scan paths and groups plugins by their parent folder
    plugins_by_mfg = defaultdict(set)
    extensions = ['*.vst3', '*.vst', '*.dll']
    
    for base_path in paths:
        for ext in extensions:
            try:
                for file_path in base_path.rglob(ext):
                    # skip files nested inside macOS .vst/.vst3 bundle folders
                    if any(p.suffix.lower() in ['.vst3', '.vst'] for p in file_path.parents):
                        continue
                        
                    plugin_name = file_path.stem
                    plugin_type = file_path.suffix.lower().replace('.', '')
                    
                    # Determine manufacturer by checking folder hierarchy
                    rel_path = file_path.relative_to(base_path)
                    
                    if len(rel_path.parts) > 1:
                        # The first sub-folder in the VST directory is usually the Manufacturer
                        manufacturer = rel_path.parts[0]
                    else:
                        # Loose files in the root VST folder
                        manufacturer = "Uncategorized (Root Folder)"
                        
                    plugins_by_mfg[manufacturer].add(f"{plugin_name} [{plugin_type.upper()}]")
                    
            except PermissionError:
                print(f"skipping a folder in {base_path} due to permission restrictions")
                
    return plugins_by_mfg

def export_list(data, output_filename="installed_VSTs.txt"):
    # format dictionary into readable text file
    if not data:
        print("no plugins found, are they installed in a custom directory?")
        return

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write("++++++++++++++++++++++++\n")
        f.write("vstscan.py by PAJAMALAND\n")
        f.write("++++++++++++++++++++++++\n\n")
        f.write('currently installed VST/VST3 plugins as of ' + dt_string + '\n')
        f.write("\n")
        
        # sort alphabetically, put uncategorized at the end
        manufacturers = sorted(data.keys(), key=lambda x: (x.startswith("Uncategorized"), x.lower()))
        
        total_plugins = 0
        for mfg in manufacturers:
            f.write(f"■ {mfg}\n")
            f.write("-" * (len(mfg) + 2) + "\n")
            
            for plugin in sorted(data[mfg]):
                f.write(f"   • {plugin}\n")
                total_plugins += 1
            f.write("\n")
            
        f.write("==========================\n")
        f.write(f"total plugins found: {total_plugins}\n")
        
    print(f"done! found {total_plugins} plugins. exported to: {output_filename}")

if __name__ == "__main__":
    print("detecting OS and standard VST folders...")
    vst_folders = get_default_vst_paths()
    
    # NOTE: if you install VSTs in a custom path, uncomment and add it here:
    # vst_folders.append(Path(r"D:\Custom\VST\Path"))
    
    print(f"scanning {len(vst_folders)} directories")
    plugin_data = scan_plugins(vst_folders)
    
    export_list(plugin_data)