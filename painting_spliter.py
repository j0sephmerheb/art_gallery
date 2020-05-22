
# coding: utf-8

# ### Students: Anh Tu NGUYEN - Joseph MERHEB - Sita SHRESTHA

# In[13]:


class Reader:
    def __init__(self, input_file):
        self.input_file = input_file;
        self.portrait_list = '';
        self.landscape_list = '';
        self.new_text = '';
        file = open(input_file, "r");
        lines = file.readlines()[1:];
        i = 0;
        for line in lines:
            self.new_text += str(i) + ' ' + line;
            i += 1;
        file.close()
        
    def paint_split(self):
        for line in self.new_text.splitlines():
            pType = line.split(' ')[1];
            if (pType == 'P'):
                self.portrait_list += line + '\n';
            elif (pType == 'L'):
                self.landscape_list += line + '\n';
        result = self.landscape_list + self.portrait_list;
        return result;
    
    def portrait_combiner(self):
        p_list = self.portrait_list.splitlines();
        result = '';
        for line in self.landscape_list.splitlines():
            l_id = line.split(' ')[0];
            result += str(l_id) + ' ';
            tags = line.split(' ')[3:];
            for tag in tags:
                if (tag == tags[-1]):
                    result += tag + '\n'
                else: result += tag + ' ';
        for i in range(0, int(len(p_list)/2)):
            p1_id = p_list[i].split(' ')[0];
            p2_id = p_list[len(p_list)-1-i].split(' ')[0];
            p1_tags = p_list[i].split(' ')[3:];
            p2_tags = p_list[len(p_list)-1-i].split(' ')[3:];
            tag_list = list(set(p1_tags) | set(p2_tags));
            result += str(p1_id) + ',' + str(p2_id) + ' ';
            for tag in tag_list:
                if (tag == tag_list[-1]):
                    result += tag + '\n'
                else: result += tag + ' ';
        file = open("simple_file.txt", "w")
        file.write(result);
        file.close();
        return result;
    
#     Other method for ordering the frameglasses
#     def order_frame(self):
#         full_list = self.portrait_combiner();
#         frame_score_dict = {}
#         frame_list = full_list.splitlines();
#         completed_frame_dict = {};
#         used_frame_list = [];
#         for i in range(0,len(frame_list)):
#             if (i<len(frame_list)-1):
#                 f1_id = frame_list[i].split(' ')[0];
#                 f1_tags = frame_list[i].split(' ')[1:];
#                 for j in range(i+1,len(frame_list)):
#                     f2_id = frame_list[j].split(' ')[0];
#                     f2_tags = frame_list[j].split(' ')[1:];
#                     common_tags = len(set(f1_tags) & set(f2_tags));
#                     f1_tag_only = len(set(f1_tags) - set(f2_tags));
#                     f2_tag_only = len(set(f2_tags) - set(f1_tags));
#                     frame_score = min(common_tags, f1_tag_only, f2_tag_only);
#                     frame_score_dict[f1_id + '-' + f2_id] = frame_score;
#                 max_score_frame = max(frame_score_dict, key=frame_score_dict.get);
#                 max_score = max(frame_score_dict.values());
#                 completed_frame_dict[max_score_frame] = max_score;
#                 for frame in max_score_frame.split('-'):
#                     if ',' in frame:
#                         for f in frame.split(','):
#                             if f not in used_frame_list:
#                                 used_frame_list.append(f);
#                     else:
#                         if frame not in used_frame_list:
#                             used_frame_list.append(frame);
#                 frame_score_dict.clear();

#         output = '';
#         for key in completed_frame_dict.keys():
#             for k in key.split('-'):
#                 if ',' in k:
#                     k = k.replace(',',' ')
#                     if k not in output:
#                         output += k + '\n'
#                 else:        
#                     if k not in output:
#                         output += str(k) + '\n'
#         output = str(output.count('\n')) + '\n' + output
# #         print(output)
#         file = open("output_" + self.input_file, "w")
#         file.write(output);
#         file.close();


# In[15]:


import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str)

    args = parser.parse_args()

    reader = Reader(args.input)
    reader.paint_split();
    reader.portrait_combiner();
#     reader.order_frame();
    
if __name__ == "__main__":
    main()
    
# reader = Reader("../0_example.txt");
# reader.paint_split();
# reader.order_frame();
# print(reader.portrait_list);
# print(reader.portrait_combiner());

