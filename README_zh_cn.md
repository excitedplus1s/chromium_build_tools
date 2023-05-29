# chromium_build_tools
配置从 https://commondatastorage.googleapis.com/chromium-browser-official/ 下载的 Chromium 使之可以编译，整体科学上网下载流量不超过300M

由于中国大陆众所周知的原因，不能下载的文件可以通过 Github Action 做中转下载，阅读 download_win64_depends.py 获取更多信息，自己实现

相关脚本仅仅支持了 Windows x64

编译流程和官方略有不同

# How to use
下载 depot_tools.zip,此步骤不需要科学上网，按照官方教程配置相关环境变量

拷贝 `*.py *.bat` 到 depot_tools文件夹

下载 chromium-113.0.5672.126，你可以下载你喜欢的版本（此步需要科学上网下载，约 1.4G）

https://commondatastorage.googleapis.com/chromium-browser-official/chromium-113.0.5672.126.tar.xz

或者使用[Chromium Downloader](https://chromium.msfconsole.cn/)

解压下载的代码

拷贝 `gclient_conf` 到 `chromium-113.0.5672.126` 文件夹下, 将其重命名为 `.gclient`

创建文件夹 `depend_download` (`chromium-113.0.5672.126`的上层文件夹的任意目录均可)

拷贝 `.gclient` 和 `DEPS` 到 `depend_download`

切换到 `depend_download` 文件夹

执行 `download_win64_depends` 命令（此步需要科学上网，下载量约 340M，实际大约155M左右的流量需要科学上网)

命令执行成功后，你会看到一个叫做 `src` 的文件夹

拷贝 `src` 文件夹下面的所有文件及文件夹到 `chromium-113.0.5672.126`,如果提示重复，选择覆盖操作

切换到 `chromium-113.0.5672.126` 文件夹

执行 `install_win64_hooks` 命令（此步不需要科学上网，此步下载文件文件的服务器没有被和谐）

执行 `set DEPOT_TOOLS_UPDATE=0` 命令，目的是避免 `depot_tools` 自动更新

执行 `gn gen out\Default` 命令

执行  `autoninja -C out\Default chrome` 命令，大约3-4个小时的等待，即可编译出来Windows x64 版本的Chromium


