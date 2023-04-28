import socket
import time

target = ('192.168.10.20', 60008)
peer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def run_test(title, msg, timeout=0):
    if timeout == 0:
        peer.settimeout(5)
    else:
        peer.settimeout(timeout)

    print('[{}]   {}   <---->   '.format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()), msg), end='', flush=True)
    peer.sendto(msg.encode('utf-8'), target)
    try:
        msg, addr = peer.recvfrom(1024)
        print(msg.decode('utf-8'))
    except socket.timeout:
        print('timeout')
    time.sleep(2)


if __name__ == '__main__':
    run_test('query factory mode: | ', '*136 GET Mode TimeOut:5 #', 5)
    # run_test('get burning result: | ', '*136 GET BURNIN 1 TimeOut:5 #', 5)
    # run_test('set rtc:            | ', '*136 SET RTC 1 $(date "+%Y.%m.%d-%H.%M.%S");TimeOut:5 #', 5)
    run_test('enter factory mode: | ', '*136 SET Mode Test #', 5)
    # run_test('get fs version:     | ', '*136 GET FsVer TimeOut:15 #', 5)
    # run_test('get ker version:    | ', '*136 GET KerVer TimeOut:5 #', 5)
    # run_test('get fac version:    | ', '*136 GET FacVer TimeOut:5 #', 5)
    # run_test('set bsn:            | ', '*136 SET BSN F1LS987654320;TimeOut:5 #', 5)
    # run_test('get bsn:            | ', '*136 GET BSN TimeOut:5 #', 5)
    # run_test('set psn:            | ', '*136 SET PSN F1LS987654320;TimeOut:5 #', 5)
    # run_test('get psn:            | ', '*136 GET PSN TimeOut:5 #', 5)
    # run_test('set mac 1:          | ', '*136 SET MAC 1 14144A070902;TimeOut:15 #', 5)
    # run_test('get mac 1:          | ', '*136 GET MAC 1 TimeOut:5 #', 5)
    # run_test('get irtx:           | ', '*136 GET IR 0 key:3;TimeOut:5 #', 5)
    # run_test('get wifi:           | ', '*136 GET WIFI ssid:K-MI;TimeOut:60 #', 5)
    # run_test('get flash:          | ', '*136 GET Flash 1 status:rw;TimeOut:15 #', 5)
    # run_test('get fan 1:          | ', '*136 GET FAN 1 TimeOut:5 #', 5)
    # run_test('get fan 2:          | ', '*136 GET FAN 2 TimeOut:5 #', 5)
    # run_test('get usb 0:          | ', '*136 GET USB 0 status:rw;TimeOut:15 #', 5)
    # run_test('get usb 1:          | ', '*136 GET USB 1 status:rw;TimeOut:15 #', 5)
    # run_test('get usb 2:          | ', '*136 GET USB 2 status:rw;TimeOut:15 #', 5)
    # run_test('get usb 3/2.0:      | ', '*136 GET USB 3 status:rw;TimeOut:15 #', 5)
    # run_test('get usb 3/3.0:      | ', '*136 GET USB 4 status:rw;TimeOut:15 #', 5)
    # run_test('get net 1:          | ', '*136 GET NET 1 type:ping;serverIp:172.16.77.1;TimeOut:20 #', 5)
    # run_test('get rtc:            | ', '*136 GET RTC 1 TimeOut:5 #', 5)
    # run_test('get sata 1:         | ', '*136 GET USB 5 status:rw;TimeOut:5 #', 5)
    # run_test('get sata 2:         | ', '*136 GET USB 6 status:rw;TimeOut:5 #', 5)
    # run_test('get audio 8ch:      | ', '*136 GET Audio 9 left:1000;right:2000;TimeOut:5 #', 5)
    # run_test('get audio in:       | ', '*136 GET Audio_IN 1 left:1000;right:2000;TimeOut:5 #', 5)
    # run_test('get dsp com:        | ', '*136 GET COM 1 TimeOut:5 #', 5)
    # run_test('get cvbs audio in:  | ', '*136 GET Audio_IN 4 left:1000;right:2000;TimeOut:5 #', 5)
    # run_test('get hdmiin:         | ', '*136 GET HDMI_IN 4 TimeOut:5 #', 5)
    # run_test('get cvbsin:         | ', '*136 GET HDMI_IN 5 TimeOut:5 #', 5)
    # run_test('get model:          | ', '*136 GET Model TimeOut:5 #', 5)
