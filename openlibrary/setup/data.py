from openlibrary.setup.params import FILE_DEVICEKEY, FILE_DEVICEXML, FILE_ACTIVATIONXML
from openlibrary.decrypt.params import KEYPATH

keyContent = b'0\x82\x02\\\x02\x01\x00\x02\x81\x81\x00\xad*E\x8e0\n\x91\xd6\xbaj\xc1t3\xc2R2h\xa6\x18\x063i\xfd\x9bR/e\xa6\xec\x87\xab\x11\n\'\xb7\x93\x14\xb6\xbbm\xfa\xf0\xf4\xe8=\x18\xa6\xe9\x15$\xdao\xb3\x8d\xf5\xddT\n\xf5\t<\xe8\xb2\x93k\x02zi\xe6\x86\x10F\x13\xc9m\xcfZ\x83\xe6=\xd6G\xf2/]3\xff\x8ch#\xea|\xa9I\x9a\xf6\xbf\x19\xd9\x10\xe0\x18\xa1\rb\x801k~\xc03f\x84\x07{v\x88\x18\x9bH\x91+o \x90\x9b\xb7\xf5\x02\x03\x01\x00\x01\x02\x81\x80\x05\xfd\x95\xd3\x886\x9a\xba\x8ck\xc1\xb5\xc21\x86\xab\x1a\xa8^\x1af%\x9b\x8a\xc0\x96\xc6\x10}\xb6\xf6\xeb\x80\xc4R\xc2@\x9d\xf9F\xa1\xf7\xe6\x06jPs\xad\xc3w\xd3\xea\xb7\xca\xec\x03\x17\xcf\xff\x01u\x96\x15\n\x0e&\xb0\xc7\x90F\xc4\xdaZ"\xc1)>\xee\x19\xf6\x05\xa5\xba\x00H)\xa8>\x1fC\x02\xd3\xba\xa8){\x06^D\xb4\xfd"\x05\x05\xec\xef\xdb.tbZ8\xabU<,+\xb6\xfaI\x98\xcc7H\xedr\xa9\xfd\x02A\x00\xc27%\xc5\xa0\xff\xd5l\xaa\x7f=\x1dx\xab?\xd8~\xf7v\x1f!\x0cCh\xc9\xb4\x1a\x8b\xb2\xaeC\xa0\xf9\x91\xcc\x99<\x11\xfbQ\xae\x8fG\xb0\xd1b\x0c=\xebR\x19\xb4\x15\xd4\x1c\xbe\xf4\xc7E\xe8\xea\xe1\xb3\x0b\x02A\x00\xe4@\xcb(\xdd\x04F\xe4jT\xe5a\xaaj\xaf=F\xa1\xaf\x1c\xa6F\x93\xc7V1\xd9\xb1\x96\xdb\x1b\xf5\x86\r\xb11\x10\x12\x18\xc5\xee\xaeD\xa3\xc1/\xe3\xf2\x8f\xaf\xad\xda\xe6\t\x8d\x9d\x99z\x04\xeeK\xdb \xff\x02A\x00\xad_\x9d\x90v\xd0\xeb->f\xa7\xa0\x0f\x80\x90V+\xc1\xac\xe8\xcd\x0f\xad}u\xd2\x19\x80k\xd9\xb4\xf5\x96\xd4\xd8\xd8R\x0f\x9bR\xa7\x89\xb0m\xdf\xfc\xaf\x00\xf7y+\x08\xe0\x13\xa25\xb5=\xce\xe2\xc6\x0b\x05Q\x02@\x18\xee\xf7\x02\\\xbaU\xe0\'\xb9da9\xd3s\x97\x16\xfb\x1c|\xdd\xb1\x01\xfd\x99m\xd2\xa0\xf2\xa0\xb6\xba(M\xa0\x98\x82o\xe7\xa2\xdf\x82\xcb\xde\xb3\x80\xbe\xbe\xc5qdep\x11\x85\x15\xbd)6\x16\xad\xd4\x9f\x13\x02@\x0f\x15\xc1Y"b\x19\x81Q\x81\x8d\x006\xe4\xf0e\xa2\xa7\xb8\x98{\x1c\x12\xe0\nw\xbe\x86A-\xd0\x1c7\xf3\x169\xadd3\x85\xaf\x13\x99\x08\x97e)c\xaf\xb1V\xf1\x15\xf6K\r\x16\xb4\xf9\xd1\x10\xe2\x92\xf9'

saltContent = b'\x12\x96E6*7!\x12\xd3\x9b\x18\xba\xfd\xf3\x96\xa9'

devicexmlContent = """<?xml version="1.0"?>
<adept:deviceInfo xmlns:adept="http://ns.adobe.com/adept">
  <adept:deviceType>standalone</adept:deviceType>
  <adept:deviceClass>Desktop</adept:deviceClass>
  <adept:deviceSerial>bc9226e3a1b58113c0856fcae2be8fecb1aeccec</adept:deviceSerial>
  <adept:deviceName>DESKTOP-QJUK0UB</adept:deviceName>
  <adept:version name="hobbes" value="9.3.58046"/>
  <adept:version name="clientOS" value="Windows Vista"/>
  <adept:version name="clientLocale" value="en"/>
  <adept:fingerprint>18wJz7tUeD4LJrQ0vPQONAC2nD0=</adept:fingerprint>
</adept:deviceInfo>
"""

activationContent = """<?xml version="1.0"?>
<activationInfo xmlns="http://ns.adobe.com/adept">
  <adept:activationServiceInfo xmlns:adept="http://ns.adobe.com/adept">
    <adept:authURL>http://adeactivate.adobe.com/adept</adept:authURL>
    <adept:userInfoURL>http://adeactivate.adobe.com/adept</adept:userInfoURL>
    <adept:activationURL>http://adeactivate.adobe.com/adept</adept:activationURL>
    <adept:certificate>MIIEsjCCA5qgAwIBAgIER2q5eDANBgkqhkiG9w0BAQUFADCBhDELMAkGA1UEBhMCVVMxIzAhBgNVBAoTGkFkb2JlIFN5c3RlbXMgSW5jb3Jwb3JhdGVkMRswGQYDVQQLExJEaWdpdGFsIFB1Ymxpc2hpbmcxMzAxBgNVBAMTKkFkb2JlIENvbnRlbnQgU2VydmVyIENlcnRpZmljYXRlIEF1dGhvcml0eTAeFw0wODAxMDkxODM3NDVaFw0xMzAxMDkxOTA3NDVaMH0xCzAJBgNVBAYTAlVTMSMwIQYDVQQKExpBZG9iZSBTeXN0ZW1zIEluY29ycG9yYXRlZDEbMBkGA1UECxMSRGlnaXRhbCBQdWJsaXNoaW5nMSwwKgYDVQQDEyNodHRwOi8vYWRlYWN0aXZhdGUuYWRvYmUuY29tL2FkZXB0LzCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAyXpCCWFh0Q3Bi1S7xf+CJfMd+cZz3HB0NknDScB1Cs8KdU0ygO7iqAgdiAdPliITkUTVEgUPvK+4yYCUderzBjq13/IrKlwEAyWeNgssJekpYgqNywo7Md1OApXzM47wVThNePNydhGYuNEEDDxzO+0JxucfhfArwnp7kIWA6q8CAwEAAaOCAbQwggGwMAsGA1UdDwQEAwIFoDBYBglghkgBhvprHgEESwxJVGhlIHByaXZhdGUga2V5IGNvcnJlc3BvbmRpbmcgdG8gdGhpcyBjZXJ0aWZpY2F0ZSBtYXkgaGF2ZSBiZWVuIGV4cG9ydGVkLjAUBgNVHSUEDTALBgkqhkiG9y8CAQQwgbIGA1UdIASBqjCBpzCBpAYJKoZIhvcvAQIDMIGWMIGTBggrBgEFBQcCAjCBhhqBg1lvdSBhcmUgbm90IHBlcm1pdHRlZCB0byB1c2UgdGhpcyBMaWNlbnNlIENlcnRpZmljYXRlIGV4Y2VwdCBhcyBwZXJtaXR0ZWQgYnkgdGhlIGxpY2Vuc2UgYWdyZWVtZW50IGFjY29tcGFueWluZyB0aGUgQWRvYmUgc29mdHdhcmUuMDEGA1UdHwQqMCgwJqAkoCKGIGh0dHA6Ly9jcmwuYWRvYmUuY29tL2Fkb2JlQ1MuY3JsMB8GA1UdIwQYMBaAFIvu8IFgyaLaHg5SwVgMBLBD94/oMB0GA1UdDgQWBBT9A+kXOPL6N57MN/zovbCGEx2+BTAJBgNVHRMEAjAAMA0GCSqGSIb3DQEBBQUAA4IBAQBVjUalliql3VjpLdT8si7OwPU1wQODllwlgfLH7tI/Ubq5wHDlprGtbf3jZm6tXY1qmh9mz1WnTmQHU3uPk8qgpihrpx4HJTjhAhLP0CXU1rd/t5whwhgT1lYfw77RRG2lZ5BzpHb/XjnY5yc3awd6F3Dli6kTkbcPyOCNoXlW4wiF+jkL+jBImY8xo2EewiJioY/iTYZH5HF+PjHF5mffANiLK/Q43l4f0YF8UagTfAJkD3iQV9lrTOWxKBgpfdyvekGqFCDq9AKzfpllqctxsC29W5bXU0cVYzf6Bj5ALs6tyi7r5fsIPSwszH/i4ixsuD0qccIgTXCwMNbt9zQu</adept:certificate>
    <adept:authenticationCertificate>MIIEYDCCA0igAwIBAgIER2q5eTANBgkqhkiG9w0BAQUFADCBhDELMAkGA1UEBhMCVVMxIzAhBgNVBAoTGkFkb2JlIFN5c3RlbXMgSW5jb3Jwb3JhdGVkMRswGQYDVQQLExJEaWdpdGFsIFB1Ymxpc2hpbmcxMzAxBgNVBAMTKkFkb2JlIENvbnRlbnQgU2VydmVyIENlcnRpZmljYXRlIEF1dGhvcml0eTAeFw0wODAxMDkxODQzNDNaFw0xODAxMzEwODAwMDBaMHwxKzApBgNVBAMTImh0dHA6Ly9hZGVhY3RpdmF0ZS5hZG9iZS5jb20vYWRlcHQxGzAZBgNVBAsTEkRpZ2l0YWwgUHVibGlzaGluZzEjMCEGA1UEChMaQWRvYmUgU3lzdGVtcyBJbmNvcnBvcmF0ZWQxCzAJBgNVBAYTAlVTMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDZAxpzOZ7N38ZGlQjfMY/lfu4Ta4xK3FRm069VwdqGZIwrfTTRxnLE4A9i1X00BnNk/5z7C0pQX435ylIEQPxIFBKTH+ip5rfDNh/Iu6cIlB0N4I/t7Pac8cIDwbc9HxcGTvXg3BFqPjaGVbmVZmoUtSVOsphdA43sZc6j1iFfOQIDAQABo4IBYzCCAV8wEgYDVR0TAQH/BAgwBgEB/wIBATAUBgNVHSUEDTALBgkqhkiG9y8CAQUwgbIGA1UdIASBqjCBpzCBpAYJKoZIhvcvAQIDMIGWMIGTBggrBgEFBQcCAjCBhhqBg1lvdSBhcmUgbm90IHBlcm1pdHRlZCB0byB1c2UgdGhpcyBMaWNlbnNlIENlcnRpZmljYXRlIGV4Y2VwdCBhcyBwZXJtaXR0ZWQgYnkgdGhlIGxpY2Vuc2UgYWdyZWVtZW50IGFjY29tcGFueWluZyB0aGUgQWRvYmUgc29mdHdhcmUuMDEGA1UdHwQqMCgwJqAkoCKGIGh0dHA6Ly9jcmwuYWRvYmUuY29tL2Fkb2JlQ1MuY3JsMAsGA1UdDwQEAwIBBjAfBgNVHSMEGDAWgBSL7vCBYMmi2h4OUsFYDASwQ/eP6DAdBgNVHQ4EFgQU9RP19K+lzF03he+0T47hCVkPhdAwDQYJKoZIhvcNAQEFBQADggEBAJoqOj+bUa+bDYyOSljs6SVzWH2BN2ylIeZKpTQYEo7jA62tRqW/rBZcNIgCudFvEYa7vH8lHhvQak1s95g+NaNidb5tpgbS8Q7/XTyEGS/4Q2HYWHD/8ydKFROGbMhfxpdJgkgn21mb7dbsfq5AZVGS3M4PP1xrMDYm50+Sip9QIm1RJuSaKivDa/piA5p8/cv6w44YBefLzGUN674Y7WS5u656MjdyJsN/7Oup+12fHGiye5QS5mToujGd6LpU80gfhNxhrphASiEBYQ/BUhWjHkSi0j4WOiGvGpT1Xvntcj0rf6XV6lNrOddOYUL+KdC1uDIe8PUI+naKI+nWgrs=</adept:authenticationCertificate>
  </adept:activationServiceInfo>

<adept:credentials xmlns:adept="http://ns.adobe.com/adept">
<adept:user>urn:uuid:a9e3f6ce-2bf8-4a9d-9264-4cb3677204d9</adept:user>
<adept:username method="AdobeID">dummy@mohmal.in</adept:username>
<adept:pkcs12>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</adept:pkcs12>
<adept:licenseCertificate>MIIDGDCCAoGgAwIBAgIGAYZ6dcbmMA0GCSqGSIb3DQEBBQUAMHwxKzApBgNVBAMTImh0dHA6Ly9hZGVhY3RpdmF0ZS5hZG9iZS5jb20vYWRlcHQxGzAZBgNVBAsTEkRpZ2l0YWwgUHVibGlzaGluZzEjMCEGA1UEChMaQWRvYmUgU3lzdGVtcyBJbmNvcnBvcmF0ZWQxCzAJBgNVBAYTAlVTMB4XDTIzMDIyMjE4NDk0NFoXDTMzMDIyMjE4NDk0NFowODE2MDQGA1UEAxMtdXJuOnV1aWQ6YTllM2Y2Y2UtMmJmOC00YTlkLTkyNjQtNGNiMzY3NzIwNGQ5MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCtKkWOMAqR1rpqwXQzwlIyaKYYBjNp/ZtSL2Wm7IerEQont5MUtrtt+vD06D0YpukVJNpvs4313VQK9Qk86LKTawJ6aeaGEEYTyW3PWoPmPdZH8i9dM/+MaCPqfKlJmva/GdkQ4BihDWKAMWt+wDNmhAd7dogYm0iRK28gkJu39QIDAQABo4HoMIHlMIG0BgNVHSMEgawwgamAFPUT9fSvpcxdN4XvtE+O4QlZD4XQoYGKpIGHMIGEMQswCQYDVQQGEwJVUzEjMCEGA1UEChMaQWRvYmUgU3lzdGVtcyBJbmNvcnBvcmF0ZWQxGzAZBgNVBAsTEkRpZ2l0YWwgUHVibGlzaGluZzEzMDEGA1UEAxMqQWRvYmUgQ29udGVudCBTZXJ2ZXIgQ2VydGlmaWNhdGUgQXV0aG9yaXR5ggRHarl5MAkGA1UdEwQCMAAwFAYDVR0lBA0wCwYJKoZIhvcvAgEHMAsGA1UdDwQEAwIFIDANBgkqhkiG9w0BAQUFAAOBgQCOnwqmH+uPv31unc8/kek6ivVGi1RIC8OKkE6tDY5+OvKZe9AAlscekai9NtRhTHJC0/Clpo2JoRxqH8Ok3xd1He/2oQofZSiLyYHbeebeP11BXuMJi7HJLF4vQc8UFuqqcTOrXoH62UaisyeC9KGOYWmH76jGCed05X/OorfOqg==</adept:licenseCertificate>
<adept:privateLicenseKey>MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAK0qRY4wCpHWumrBdDPCUjJophgGM2n9m1IvZabsh6sRCie3kxS2u2368PToPRim6RUk2m+zjfXdVAr1CTzospNrAnpp5oYQRhPJbc9ag+Y91kfyL10z/4xoI+p8qUma9r8Z2RDgGKENYoAxa37AM2aEB3t2iBibSJErbyCQm7f1AgMBAAECgYAF/ZXTiDaauoxrwbXCMYarGqheGmYlm4rAlsYQfbb264DEUsJAnflGoffmBmpQc63Dd9Pqt8rsAxfP/wF1lhUKDiawx5BGxNpaIsEpPu4Z9gWlugBIKag+H0MC07qoKXsGXkS0/SIFBezv2y50Ylo4q1U8LCu2+kmYzDdI7XKp/QJBAMI3JcWg/9Vsqn89HXirP9h+93YfIQxDaMm0GouyrkOg+ZHMmTwR+1Guj0ew0WIMPetSGbQV1By+9MdF6OrhswsCQQDkQMso3QRG5GpU5WGqaq89RqGvHKZGk8dWMdmxltsb9YYNsTEQEhjF7q5Eo8Ev4/KPr63a5gmNnZl6BO5L2yD/AkEArV+dkHbQ6y0+ZqegD4CQVivBrOjND619ddIZgGvZtPWW1NjYUg+bUqeJsG3f/K8A93krCOATojW1Pc7ixgsFUQJAGO73Aly6VeAnuWRhOdNzlxb7HHzdsQH9mW3SoPKgtrooTaCYgm/not+Cy96zgL6+xXFkZXARhRW9KTYWrdSfEwJADxXBWSJiGYFRgY0ANuTwZaKnuJh7HBLgCne+hkEt0Bw38xY5rWQzha8TmQiXZSljr7FW8RX2Sw0WtPnREOKS+Q==</adept:privateLicenseKey>
<adept:authenticationCertificate>MIIEYDCCA0igAwIBAgIER2q5eTANBgkqhkiG9w0BAQUFADCBhDELMAkGA1UEBhMCVVMxIzAhBgNVBAoTGkFkb2JlIFN5c3RlbXMgSW5jb3Jwb3JhdGVkMRswGQYDVQQLExJEaWdpdGFsIFB1Ymxpc2hpbmcxMzAxBgNVBAMTKkFkb2JlIENvbnRlbnQgU2VydmVyIENlcnRpZmljYXRlIEF1dGhvcml0eTAeFw0wODAxMDkxODQzNDNaFw0xODAxMzEwODAwMDBaMHwxKzApBgNVBAMTImh0dHA6Ly9hZGVhY3RpdmF0ZS5hZG9iZS5jb20vYWRlcHQxGzAZBgNVBAsTEkRpZ2l0YWwgUHVibGlzaGluZzEjMCEGA1UEChMaQWRvYmUgU3lzdGVtcyBJbmNvcnBvcmF0ZWQxCzAJBgNVBAYTAlVTMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDZAxpzOZ7N38ZGlQjfMY/lfu4Ta4xK3FRm069VwdqGZIwrfTTRxnLE4A9i1X00BnNk/5z7C0pQX435ylIEQPxIFBKTH+ip5rfDNh/Iu6cIlB0N4I/t7Pac8cIDwbc9HxcGTvXg3BFqPjaGVbmVZmoUtSVOsphdA43sZc6j1iFfOQIDAQABo4IBYzCCAV8wEgYDVR0TAQH/BAgwBgEB/wIBATAUBgNVHSUEDTALBgkqhkiG9y8CAQUwgbIGA1UdIASBqjCBpzCBpAYJKoZIhvcvAQIDMIGWMIGTBggrBgEFBQcCAjCBhhqBg1lvdSBhcmUgbm90IHBlcm1pdHRlZCB0byB1c2UgdGhpcyBMaWNlbnNlIENlcnRpZmljYXRlIGV4Y2VwdCBhcyBwZXJtaXR0ZWQgYnkgdGhlIGxpY2Vuc2UgYWdyZWVtZW50IGFjY29tcGFueWluZyB0aGUgQWRvYmUgc29mdHdhcmUuMDEGA1UdHwQqMCgwJqAkoCKGIGh0dHA6Ly9jcmwuYWRvYmUuY29tL2Fkb2JlQ1MuY3JsMAsGA1UdDwQEAwIBBjAfBgNVHSMEGDAWgBSL7vCBYMmi2h4OUsFYDASwQ/eP6DAdBgNVHQ4EFgQU9RP19K+lzF03he+0T47hCVkPhdAwDQYJKoZIhvcNAQEFBQADggEBAJoqOj+bUa+bDYyOSljs6SVzWH2BN2ylIeZKpTQYEo7jA62tRqW/rBZcNIgCudFvEYa7vH8lHhvQak1s95g+NaNidb5tpgbS8Q7/XTyEGS/4Q2HYWHD/8ydKFROGbMhfxpdJgkgn21mb7dbsfq5AZVGS3M4PP1xrMDYm50+Sip9QIm1RJuSaKivDa/piA5p8/cv6w44YBefLzGUN674Y7WS5u656MjdyJsN/7Oup+12fHGiye5QS5mToujGd6LpU80gfhNxhrphASiEBYQ/BUhWjHkSi0j4WOiGvGpT1Xvntcj0rf6XV6lNrOddOYUL+KdC1uDIe8PUI+naKI+nWgrs=</adept:authenticationCertificate>
</adept:credentials>

<activationToken xmlns="http://ns.adobe.com/adept">
  <device>urn:uuid:961532c7-2cb3-460b-8c73-83a2eec90a5c</device>
  <fingerprint>18wJz7tUeD4LJrQ0vPQONAC2nD0=</fingerprint>
  <deviceType>standalone</deviceType>
  <activationURL>http://adeactivate.adobe.com/adept</activationURL>
  <user>urn:uuid:a9e3f6ce-2bf8-4a9d-9264-4cb3677204d9</user>
  <signature>FgmewBwLcQOj6gQVc+22E2emLf4HFJyNvAi/MWkW0rjQg+m2eGVL5MGCrAUJcHnnTcp6jsAfh2WWvb90eipFsy3pGfp3RX2wnTYX5uYuXYHZVToLILVq3Cb5B+3f47DHTQmM0+fIfr/Vyge0YsLdZdQGW1mkHaCchv2uXwwEV0k=</signature>
</activationToken>
<adept:operatorURLList xmlns:adept="http://ns.adobe.com/adept"><adept:user>urn:uuid:a9e3f6ce-2bf8-4a9d-9264-4cb3677204d9</adept:user><adept:operatorURL>http://lending6.us.archive.org:8080/fulfillment/Fulfill</adept:operatorURL></adept:operatorURLList><adept:licenseServices xmlns:adept="http://ns.adobe.com/adept"><adept:licenseServiceInfo><adept:licenseURL>https://nasigningservice.adobe.com/licensesign</adept:licenseURL><adept:certificate>MIIEvjCCA6agAwIBAgIER2q5ljANBgkqhkiG9w0BAQUFADCBhDELMAkGA1UEBhMCVVMxIzAhBgNVBAoTGkFkb2JlIFN5c3RlbXMgSW5jb3Jwb3JhdGVkMRswGQYDVQQLExJEaWdpdGFsIFB1Ymxpc2hpbmcxMzAxBgNVBAMTKkFkb2JlIENvbnRlbnQgU2VydmVyIENlcnRpZmljYXRlIEF1dGhvcml0eTAeFw0wODA4MTExNjMzNDhaFw0xMzA4MTEwNzAwMDBaMIGIMQswCQYDVQQGEwJVUzEjMCEGA1UEChMaQWRvYmUgU3lzdGVtcyBJbmNvcnBvcmF0ZWQxGzAZBgNVBAsTEkRpZ2l0YWwgUHVibGlzaGluZzE3MDUGA1UEAxMuaHR0cHM6Ly9uYXNpZ25pbmdzZXJ2aWNlLmFkb2JlLmNvbS9saWNlbnNlc2lnbjCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAs9GRZ1f5UTRySgZ2xAL7TaDKQBfdpIS9ei9Orica0N72BB/WE+82G5lfsZ2HdeCFDZG/oz2WPLXovcuUAbFKSIXVLyc7ONOd4sczeXQYPixeAvqzGtsyMArIzaeJcriGVPRnbD/spbuHR0BHhJEakIiDtQLJz+xgVYHlicx2H/kCAwEAAaOCAbQwggGwMAsGA1UdDwQEAwIFoDBYBglghkgBhvprHgEESwxJVGhlIHByaXZhdGUga2V5IGNvcnJlc3BvbmRpbmcgdG8gdGhpcyBjZXJ0aWZpY2F0ZSBtYXkgaGF2ZSBiZWVuIGV4cG9ydGVkLjAUBgNVHSUEDTALBgkqhkiG9y8CAQIwgbIGA1UdIASBqjCBpzCBpAYJKoZIhvcvAQIDMIGWMIGTBggrBgEFBQcCAjCBhhqBg1lvdSBhcmUgbm90IHBlcm1pdHRlZCB0byB1c2UgdGhpcyBMaWNlbnNlIENlcnRpZmljYXRlIGV4Y2VwdCBhcyBwZXJtaXR0ZWQgYnkgdGhlIGxpY2Vuc2UgYWdyZWVtZW50IGFjY29tcGFueWluZyB0aGUgQWRvYmUgc29mdHdhcmUuMDEGA1UdHwQqMCgwJqAkoCKGIGh0dHA6Ly9jcmwuYWRvYmUuY29tL2Fkb2JlQ1MuY3JsMB8GA1UdIwQYMBaAFIvu8IFgyaLaHg5SwVgMBLBD94/oMB0GA1UdDgQWBBSQ5K+bvggI6Rbh2u9nPhH8bcYTITAJBgNVHRMEAjAAMA0GCSqGSIb3DQEBBQUAA4IBAQC0l1L+BRCccZdb2d9zQBJ7JHkXWt1x/dUydU9I/na+QPFE5x+fGK4cRwaIfp6fNviGyvtJ6Wnxe6du/wlarC1o26UNpyWpnAltcy47LpVXsmcV5rUlhBx10l4lecuX0nx8/xF8joRz2BvvAusK+kxgKeiAjJg2W20wbJKh0Otct1ZihruQsEtGbZJ1L55xfNhrm6CKAHuGuTDYQ/S6W20dUaDUiNFhA2n2eEySLwUwgOuuhfVUPb8amQQKbF4rOQ2rdjAskEl/0CiavW6Xv0LGihThf6CjEbNSdy+vXQ7K9wFbKsE843DflpuSPfj2Aagtyrv/j1HsBjsf03e0uVu5</adept:certificate></adept:licenseServiceInfo></adept:licenseServices></activationInfo>
"""

def createDefaultFiles():
  
  with open(KEYPATH,"wb",) as file1: file1.write(keyContent)
  with open(FILE_DEVICEKEY,"wb") as file2: file2.write(saltContent)
  with open(FILE_DEVICEXML,"w",encoding="utf-8") as file3: file3.write(devicexmlContent)
  with open(FILE_ACTIVATIONXML,"w",encoding="utf-8") as file4: file4.write(activationContent)