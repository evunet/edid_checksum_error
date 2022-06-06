Устанавливаем нужные пакеты
apt install read-edid python3 i2c-tools

Получаем информацию по всем подключеным мониторам
get-edid

Находим нужную шину с монитором
"Bus <b>4</b> found"

get-edid -b <b>4</b>|parse-edid
get-edid -b <b>4</b> > /edid.bin

Получаем адрес ошибки контрольной суммы и нужное значение
./edid-checksum.py < /edid.bin

0x50 - адрес I2C шины
0x7f - адрес контрольной суммы
0xb6 - нужное значение контрольной суммы

Получаем текущее значение контрольной суммы
i2cget -y <b>4</b> 0x50 0x7f

Записываем правильное значение контрольной суммы
i2cset -y <b>4</b> 0x50 0x7f 0xb6

/sys/class/drm/card0-HDMI-A-1/edid
/sys/class/drm/card0-HDMI-A-1/modes