
def foreachLine(lines):
    # 存储结果
    result = []
    # 遍历每一行
    for line in lines:
        #line = "午夜频道_0000,#genre#"
        # 如果出现特殊字符串，停止并保存结果
        if "密码,#genre#" in line:
            break
        if "#genre#" in line:
            if "_" in line:
                # 替换字符串
                new_line = line.split("_")[0] + "," + line.split(",")[1]
                result.append(new_line)
            else:
                result.append(line)
        else:
            # 否则，直接添加
            result.append(line)

    return result


if __name__ == '__main__':
    print('work start ...\n')
    
    for fileIndex in range(4):
        print(fileIndex)

        # 定义源文件
        src_file = str(fileIndex) +".txt"
        # 定义输出文件
        output_file = "m" + str(fileIndex) +".txt"

        # 读取源文件
        with open(src_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            f.close()
        result = foreachLine(lines) 
        
        # 写入输出文件
        with open(output_file, "w", encoding="utf-8") as f:
            f.writelines(result)
            f.flush()
            f.close()
        
        print('handler file finished: + '+src_file + '\n')

    print("All finished!")
