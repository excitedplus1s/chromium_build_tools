# chromium_build_tools
Configure chromium sourcecode from https://commondatastorage.googleapis.com/chromium-browser-official/

Windows x64 support only

# How to use
Download depot_tools and configure the environment variables according to Chromium's document

copy `*.py *.bat` to depot_tools floder

Download chromium-113.0.5672.126,you can download the version you need

https://commondatastorage.googleapis.com/chromium-browser-official/chromium-113.0.5672.126.tar.xz

upzip it

copy `gclient_conf` to unziped floder `chromium-113.0.5672.126` , rename it to `.gclient`

create a new folder `depend_download` (on the upper level of `chromium-113.0.5672.126`)

copy `.gclient` and `DEPS` to depend_download

run `download_win64_depends`

after the above command is executed, you will see a folder named `src`

copy all files in the `src` folder to the `chromium-113.0.5672.126` folder, and if prompted for duplicate files, choose to overwrite the current file.

cd `chromium-113.0.5672.126`

run `install_win64_hooks`

run `set DEPOT_TOOLS_UPDATE=0`

run `gn gen out\Default`

run `autoninja -C out\Default chrome`


