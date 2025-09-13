@echo on
setlocal enabledelayedexpansion

:: 注释: Unicode 16位范围内，汉字的主要区块是：
:: 基本的汉字: U+4E00 到 U+9FFF。这个范围包括了常用的 20902 个汉字，这些是最常用的汉字，涵盖了现代中文写作的绝大多数需求。
:: 扩展A: U+3400 到 U+4DBF。这个范围包括了额外的 6582 个汉字，主要是一些较不常用的汉字。

for /L %%i in (0x3400,1,0x4DBF) do (
    set "hex=%%i"
    set "formattedHex=!hex:~-4!"
    potrace -t 1200 -a 10 -O 0.2 -u 1 -q -c ..\pic\uni!formattedHex!.bmp
)

for /L %%i in (0x4E00,1,0x9FFF) do (
    set "hex=%%i"
    set "formattedHex=!hex:~-4!"
    potrace -t 1200 -a 10 -O 0.2 -u 1 -q -c ..\pic\uni!formattedHex!.bmp
)

endlocal
