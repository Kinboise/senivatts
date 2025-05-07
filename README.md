# Seniva TTS 帜和语朗读程序

*臤徘斯 Kinboise*

此程序用于朗读我的人造语言：帜和语，也可以修改以适配其他语言。

A TTS program for my conlang Seniva. Can be adapted to other languages.

## 安装 Installation

安装 Python3。并安装所需的包：

Requires Python3 and packages:

```
pip install -r requirements.txt
```

安装支持 SAPI5 的音源。我这里使用了 RHVoice.org 的免费音源以及微软 Edge 音源。

Install voice banks that supports SAPI 5. I'm using free voices from RHVoice.org and Microsoft Edge.

下载本仓库至任意文件夹。

Download/Clone this repo.

## 用法 Usage

在本程序的保存路径中用此命令查看帮助：

Use this command for help:

```
python senivatts.py -h
```

## 实例 Examples

使用第二个波兰语音源，1.5倍速朗读 "mi e hafa-gara vol."

Read "mi e hafa-gara vol." with the 2nd Polish voice bank, 1.5x rate.

``` powershell
python senivatts.py -t "mi e hafa-gara vol." -l pl -v 2 -r 1.5
```

使用第一个阿尔巴尼亚语音源朗读文件`soc.txt`的内容，并输出音频文件`soc.wav`

Read the file `soc.txt` with the 1st Albanian voice bank, and output a wave file `soc.wav`

``` powershell
python senivatts.py -f soc.txt -l sq -o soc.wav
```

## 配置文件 Config

`senivatts.yml` 中包含声库注册表路径（部分）、基准语速、帜和语转换规则。如利用塞尔维亚语声库`sr`来朗读帜和语时，输入的文本 "tence Dcanqovi" 会被转为 "тенче џанови" 来朗读。如需适配其他语言，更改各语种的`rules`部分即可。

`senivatts.yml` contains names of the voice banks, the default rate, and the rules to convert Seniva text. Take `sr` Serbian as an example. Seniva text input "tence Dcanqovi" will be converted to "тенче џанови" for the Serbian TTS to read. Change `rules` to adapt to other languages.