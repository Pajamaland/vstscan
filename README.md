# vstscan
a simple Python script to list all installed VST plugins in a txt file

i made this simple python utility to export a txt file contianing a list of all VST plugins installed on a system (windows/mac only). this is useful for compiling a list of your LEGALLY OBTIANED vst plugins so you can easily reinstall them if you reinstall your OS.

note for mac users: this does NOT scan Audio Unit (AU) plugins. this could easily be implemented since the script itself is so simple, if there's enough demand for it i might do it myself otherwise feel free to either use your brain or your favourite slop machine to add the feature for you

# Usage
simply open a terminal of your choosing and run ``python vstscan.py``. the output will be saved as a text file in the same location as the script.

# Support
short: no

long: fork and fix/improve yourself! open source is awesome

longer: GPLv3, section 15, "disclaimer of warranty"

"THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION."
