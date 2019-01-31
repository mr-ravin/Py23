def replace_print(line_data):
  tmp_line=line_data.replace("print","print(")
  line_data=tmp_line.replace("\n"," )\n")
  return line_data

def replace_pickle(line_data):
  return line_data.replace("cPickle","_pickle")

def choice_fn(line_data,index):
  if index==0: ### print -----> print()
    new_line=replace_print(line_data)
    return new_line
  elif index==1: ### cPickle ------> _pickle
    new_line=replace_pickle(line_data)
    return new_line
  else:
    return new_line

def convert(source_file,destination_file=""):
  function_list=["print","cPickle"]
  source_data=open(source_file,"r")
  list_source_data=source_data.readlines()
  each_line=[]
  for line in list_source_data: 
    #count_prev=[0,0] # count for occurance of " '

    for fun_val in function_list:
      if fun_val in line:       
        line=choice_fn(line,function_list.index(fun_val))
    each_line.append(line)
  net_line="".join(each_line)
  source_data.close()

  if destination_file=="":
    des_data=open(source_file,"w")
    des_data.write(net_line)
    des_data.close()
  else:
    des_data=open(destination_file,"w")
    des_data.write(net_line)
    des_data.close()
