import os
import shutil
import pdb

for root, folder, files in os.walk('data'):
    for file in files:
        if '.jpg' in file or '.wav' in file or '.gif' in file:
            new_file = file.replace('_Ini0_0', '').replace('_Onlypool_0', '').replace('IsBig_0', '').replace('Try_', '')\
                .replace('num_layer_', 'l_').replace('depth_', 'd_').replace('Adam_', 'A_').replace('_iter', '_i')\
                .replace('Fou_0.0_', '').replace('padtype_zero_', '').replace('step_step_', '').replace('generator_', 'g_')\
                .replace('pyramid', '').replace('inner_', 'in_').replace('l1_0.0_', '').replace('noattention_False_', '')\
                .replace('normal_False_', '').replace('IsMean_', 'M_').replace('False', 'F').replace('sn_F', '').replace('sn_0', '')\
                .replace('Gau', 'G')
            if new_file[0] == '_':
                new_file = new_file[1:]
            if new_file != file:
                if new_file in files:
                    raise ValueError(f'{new_file} exists!' )
                else:
                    # pdb.set_trace()
                    shutil.move(os.path.join(root, file), os.path.join(root, new_file))