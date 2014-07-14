##aerogui
=======

GUI do captchy w aero2 napisane w pythonie - testowane na windows i linux

=======

Aby korzystać na windowsie lub linuxie (osx także powinno działac) wystarczy uruchomić główny plik programu.
Funkcja ponownego połączenia dostosowana jest narazie tylko do urządzeń z androidem służących jako modem.
Program zaprojektowany jest jednak tak, żeby każdy łatwo mógł dodać
wsparcie swojego urządzenia poprzez configa (reconnect odbywa się poprzez
wydania polecenia w systemie).
Wystarczy napisać odpowiedni skrypt :)

=======

Wymagania:
- Oczywiście python (pisane pod wersje 2.7) - Ubuntu `sudo apt-get install python`, Windows `https://www.python.org/downloads/windows/`
- Tkinter (domyślnie zainstalowany w Windows, w Ubuntu wydajemy polecenie `sudo apt-get install python-tk python-pmw`)
- PIL (w windows polecam pobrać Pillow - fork PIL'a, w Ubuntu wydajemy polecenie: `sudo apt-get install python-imaging python-imaging-tk`)
