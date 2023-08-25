# bilibili_ccconvert
将哔哩哔哩的CC字幕处理成SRT文件

# 以下是使用教程
1.打开需要保存字幕的视频，并确保CC字幕选项为开启。<br>
2.按下键盘的F12打开开发人员工具，切换到网络（Network）选项卡。<br>
3.刷新页面<br>
4.在上方搜索框搜索"json"通常能够看到一个由数字和字母组成的文件名的json，如6127dd8c27b584559388788927ce1267db355259.json<br>
5.双击该文件，在新打开的窗口中点击“响应”选项卡，并复制其中全部内容<br>
你复制下来的内容应该是这样：<br>
```
{
    "font_size": 0.4,
    "font_color": "#FFFFFF",
    "background_alpha": 0.5,
    "background_color": "#9C27B0",
    "Stroke": "none",
    "body": [
        {
            "from": 1.5,
            "to": 6,
            "location": 2,
            "content": "迄今为止我们全都在关注键盘的“键”，"
        },
        {
            "from": 6,
            "to": 12,
            "location": 2,
            "content": "现在终于到了该关注“键”之后是什么的阶段了。"
        },...]
}
```
6.将复制下来的内容粘贴到文本编辑器，保存，编码选择UTF-8<br>
7.打开该脚本，输入文件的绝对路径（如C:\Users\username\Documents\1.json）,然后点击回车<br>
8.会在目录下生成output.srt，处理完成。<br>
