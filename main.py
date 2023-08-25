import json
import os

def convert_cc_to_srt(cc_file, srt_file):
    with open(cc_file, 'r', encoding='utf-8') as f:
        cc_data = json.load(f)

    with open(srt_file, 'w', encoding='utf-8') as f:
        index = 1
        for subtitle in cc_data['body']:
            start_time = subtitle['from']
            end_time = subtitle['to']
            content = subtitle['content']
            
            start_time_str = format_time(start_time)
            end_time_str = format_time(end_time)

            f.write(f"{index}\n")
            f.write(f"{start_time_str} --> {end_time_str}\n")
            f.write(f"{content}\n")
            f.write("\n")

            index += 1

def format_time(time):
    hours = int(time // 3600)
    minutes = int((time % 3600) // 60)
    seconds = int(time % 60)
    milliseconds = int((time % 1) * 1000)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

cc_file = input("请输入CC字幕文件(.json)文件路径：")
srt_file = 'output.srt'

convert_cc_to_srt(cc_file, srt_file)
os.system("pause")
