# bililist
自制B站播放列表，可将收藏的视频随机或循环播放
### 支持
此程序仅支持Chrome和FireFox浏览器，仅在win7及win10上测试过。请使用最新版浏览器，我会尽量随着版本更新程序及附件。
### 安装
1.下载程序。右上点击'Clone or download'，点击'Download ZIP'下载。

2.解压到想要的目录，将文件所在目录(即yourdirectory/bililist/)加入环境变量PATH即可。(win10可以直接在小娜搜索框里输入‘环境变量’找到配置窗口)

3.卸载时相应地从PATH中删除，然后删除安装目录即可。
### 使用
1.在urllist中输入视频网址，在timelist对应位置输入希望视频播放的时间。

2.双击bililist.exe,根据提示使用即可。(比较需要注意的是缓冲时间，如果哪里卡住不动了，肯定是缓冲时间设置小了，本人网络ping B站 443端口延迟为50ms，大家可以根据这个时间调整自己的缓冲时间。)
### 文件解释
bililist.exe---------->主程序，配置好后，直接启动即可。

chromedriver.exe-->chrome浏览器驱动。

geckodriver.exe---->firefox浏览器驱动。

urllist.txt------------>B站视频网址。

timelist.txt---------->B站视频播放时间。

bililist.py------------>源文件，可以自己修改使用。

其他文件------------>开发用。
