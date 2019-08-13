import PDB_Synthesizeryt
import numpy as np
import randomgen


repeat = 15
#entries = ["MA0"]*repeat
entries = ["MA0","MB0","MA0","MB0","MB0","MA0","MB0","MB0","MB0","MA0","MA0","MB0","MA0","MB0","MB0"]
#entries = ["MA1","MA0","MB1"]#A0-B1 connects badly, A1-A0 connects well
#entries = ["MA1","MB0","MA1","MB0","MA1","MB0","MA1","MB0","MA1","MB0"]#this one really works for simulation (no crashing)
#entries = ["MA0","MA0","MB0","MA1","MB1","MB0","MA1","MB0","MA1","MB1"]
#entries = ["MB0","MB1","MA0","MB0","MA1","MA0","MB1","MA0","MA1","MB1"]*repeat
output_name= "0-PP75"

#These settings work for intramonomer concatination (between MAs and MBs)
#link_setting = PDB_Synthesizer.LinkSetting(
#       connect_from="C",
#       connect_to="N",
#       #bond_offset=np.array([0., 0.5, -1.5])
#       #The above bond offset for MA0-MA0, MA1-MA1, MA0-MA1, MA1-MA0 concatination
#       bond_offset=np.array([-0.35, 0.6, 1.8])
#       #The above bond offset for MB0-MB0, MB1-MB1, MB0-MB1, MB1-MB0 concatination
#   )

link_setting_strings = ["{}{}".format(entries[i], entries[i+1]) for i in range(len(entries) - 1)]
link_settings = [randomgen.link_setting_map[lss] for lss in link_setting_strings]
print(link_setting_strings)

final_name = "./{}x{}.pdb".format(output_name,repeat)
PDB_Synthesizeryt.construct(
    entries,
    final_name,
    link_settings
)

print(final_name)
